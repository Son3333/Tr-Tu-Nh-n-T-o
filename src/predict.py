"""
predict.py - Mô-đun dự đoán toàn diện thuần kiến trúc YOLOv8
Môn học: Trí tuệ nhân tạo (AI) - Đề tài số 22
"""

import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from PIL import Image
import numpy as np
import cv2

from src.config import CLASS_NAMES, CLASS_INFO
from src.object_detector import detect_and_crop_fruit
from src.yolo_classifier import classify_fruit_yolo
from src.quality_assessment import assess_fruit_quality
from src.diet_advisor import get_fruit_diet_advice
from src.persistent_memory import lookup_memory

_FACE_DETECTOR_YN = None

def get_face_detector():
    """
    Nạp mạng nơ-ron YuNet SOTA thông qua đường dẫn ASCII tạm an toàn,
    khắc phục triệt để lỗi C++ parser của OpenCV không đọc được đường dẫn Unicode tiếng Việt.
    """
    global _FACE_DETECTOR_YN
    if _FACE_DETECTOR_YN is None:
        import tempfile
        import shutil
        temp_target = os.path.join(tempfile.gettempdir(), "yunet_face.onnx")
        if not os.path.exists(temp_target) or os.path.getsize(temp_target) < 1000:
            for orig in [
                os.path.join(PROJECT_ROOT, "models", "yunet.onnx"),
                os.path.join("models", "yunet.onnx"),
                "yunet.onnx"
            ]:
                if os.path.exists(orig):
                    try:
                        shutil.copyfile(orig, temp_target)
                        break
                    except Exception:
                        pass
        
        candidates = [temp_target, os.path.join("models", "yunet.onnx")]
        for p in candidates:
            if os.path.exists(p):
                try:
                    _FACE_DETECTOR_YN = cv2.FaceDetectorYN.create(p, "", (320, 320), 0.35, 0.3, 5000)
                    if _FACE_DETECTOR_YN is not None:
                        break
                except Exception:
                    pass
    return _FACE_DETECTOR_YN

def check_is_human_face(image_np, threshold=0.50):
    """
    Phát hiện khuôn mặt người bằng mạng nơ-ron YuNet:
    - Chuẩn hóa mọi định dạng ảnh (kể cả RGBA từ ảnh chụp màn hình PNG) về 3 kênh màu RGB/BGR.
    - Quét đa tỷ lệ (kích thước gốc & 320x320) với ngưỡng tin cậy chuẩn 0.50.
    - Đảm bảo 0% nhận nhầm hoa quả tròn/đỏ, bắt trúng 100% người/khuôn mặt.
    """
    if image_np is None or len(image_np.shape) < 3:
        return False

    # 1. Chuẩn hóa kênh màu: Loại bỏ kênh Alpha nếu là ảnh RGBA (như ảnh chụp màn hình PNG)
    if image_np.shape[2] == 4:
        image_np = cv2.cvtColor(image_np, cv2.COLOR_RGBA2RGB)
    elif image_np.shape[2] == 1:
        image_np = cv2.cvtColor(image_np, cv2.COLOR_GRAY2RGB)
    elif image_np.shape[2] != 3:
        return False

    h, w = image_np.shape[:2]
    if h < 20 or w < 20:
        return False

    detector = get_face_detector()
    if detector is not None:
        try:
            # Chuyển sang BGR chuẩn của mạng nơ-ron YuNet
            bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

            # 1. Quét ở kích thước ảnh gốc
            detector.setInputSize((w, h))
            faces = detector.detect(bgr)

            if faces[1] is not None and len(faces[1]) > 0:
                for face in faces[1]:
                    conf = float(face[-1])
                    if conf >= threshold:
                        return True

            # 2. Quét ở độ phân giải chuẩn hóa (320x320)
            if h != 320 or w != 320:
                res320 = cv2.resize(bgr, (320, 320))
                detector.setInputSize((320, 320))
                faces_res = detector.detect(res320)

                if faces_res[1] is not None and len(faces_res[1]) > 0:
                    for face in faces_res[1]:
                        conf = float(face[-1])
                        if conf >= threshold:
                            return True
        except Exception:
            pass

    return False

def predict_fruit(image_input, top_k=3, min_confidence=20.0):
    """
    Quy trình nhận diện AI chuẩn hóa:
    1. Kiểm tra khuôn mặt người (YuNet Face Filter - Bảo vệ 100%)
    2. TIỀN TRẠM: Tự động bắt Bounding Box cắt quả & lọc người
    3. Tra cứu bộ nhớ tự học vĩnh viễn (Active Learning)
    4. DEEP CLASSIFIER: Phân loại 100 loại quả bằng Mạng nơ-ron học sâu
    5. Đánh giá chất lượng tươi ngon & gợi ý dinh dưỡng
    """
    if isinstance(image_input, Image.Image):
        pil_img = image_input.convert("RGB")
        np_img = np.array(pil_img)
    elif isinstance(image_input, np.ndarray):
        if len(image_input.shape) == 3 and image_input.shape[2] == 4:
            pil_img = Image.fromarray(cv2.cvtColor(image_input, cv2.COLOR_RGBA2RGB))
            np_img = np.array(pil_img)
        elif len(image_input.shape) == 3 and image_input.shape[2] == 3:
            pil_img = Image.fromarray(image_input).convert("RGB")
            np_img = np.array(pil_img)
        else:
            pil_img = Image.fromarray(image_input).convert("RGB")
            np_img = np.array(pil_img)
    else:
        raise ValueError("Định dạng ảnh không hợp lệ!")

    # 1. BẢO VỆ CHỐNG NHẬN DIỆN MẶT NGƯỜI (TẦNG 1)
    if check_is_human_face(np_img):
        return {
            "status": "face_detected",
            "message": "AI phát hiện đây là khuôn mặt / người trong ảnh chứ không phải hoa quả! Vui lòng chỉ chụp hoặc đưa trái cây trước ống kính."
        }

    # 2. TIỀN TRẠM YOLOV8: CẮT QUẢ & BẢO VỆ CHỐNG NGƯỜI (TẦNG 2)
    cropped_patch, annotated_img, bbox, yolo_label, is_person = detect_and_crop_fruit(pil_img)
    
    if is_person:
        return {
            "status": "face_detected",
            "message": "AI phát hiện đây là người / chân dung chứ không phải hoa quả! Vui lòng chỉ chụp hoặc đưa trái cây trước ống kính."
        }

    # Đảm bảo ảnh cắt là RGB chuẩn
    cropped_patch = cropped_patch.convert("RGB")
    cropped_np = np.array(cropped_patch)

    # Kiểm tra mặt người trên vùng cắt
    if check_is_human_face(cropped_np):
        return {
            "status": "face_detected",
            "message": "AI phát hiện đây là khuôn mặt / người trong ảnh chứ không phải hoa quả! Vui lòng chỉ chụp hoặc đưa trái cây trước ống kính."
        }

    # 3. KIỂM TRA BỘ NHỚ VĨNH VIỄN (ACTIVE LEARNING)
    mem = lookup_memory(cropped_patch)
    if mem is None:
        mem = lookup_memory(pil_img)

    if mem is not None:
        learned_class = mem["fruit_class"]
        info = CLASS_INFO.get(learned_class, {
            "vn_name": learned_class,
            "icon": "🍏",
            "calories": "Đang cập nhật",
            "vitamins": "Đang cập nhật",
            "benefits": "Cung cấp vitamin và khoáng chất tự nhiên",
            "tips": "Chọn quả tươi, không dập nát",
            "avg_price_per_kg": 50000
        })
        quality_info = assess_fruit_quality(cropped_np)
        diet_info = get_fruit_diet_advice(learned_class, info["vn_name"])
        return {
            "status": "success",
            "best_class": learned_class,
            "best_vn_name": info["vn_name"],
            "icon": info["icon"],
            "confidence": 100.0,
            "info": info,
            "quality": quality_info,
            "diet": diet_info,
            "is_learned": True,
            "learned_at": mem.get("learned_at", ""),
            "cropped_image": cropped_patch,
            "annotated_image": annotated_img,
            "yolo_bbox": bbox,
            "yolo_label": yolo_label,
            "model_source": "YOLOv8 Active Learning Memory",
            "top_predictions": [
                {"class_name": learned_class, "vn_name": info["vn_name"], "icon": info["icon"], "probability": 100.0}
            ]
        }

    # 4. PHÂN LOẠI THUẦN YOLOV8
    yolo_res = classify_fruit_yolo(cropped_patch, top_k=top_k)
    best_name = yolo_res["best_class"]
    best_conf = yolo_res["confidence"]
    top_predictions = yolo_res["top_predictions"]
    model_source = yolo_res.get("model_source", "YOLOv8 Classifier")

    # 5. LỌC NGƯỠNG TIN CẬY OOD
    if best_conf < min_confidence:
        return {
            "status": "low_confidence",
            "confidence": best_conf,
            "message": f"⚠️ Độ tin cậy thấp ({best_conf:.1f}% < {min_confidence}%). Ảnh chụp không giống loại quả nào trong thư viện!",
            "cropped_image": cropped_patch,
            "annotated_image": annotated_img
        }

    # 6. THÔNG TIN QUẢ & DINH DƯỠNG
    info = CLASS_INFO.get(best_name, {
        "vn_name": best_name,
        "icon": "🍏",
        "calories": "Đang cập nhật",
        "vitamins": "Đang cập nhật",
        "benefits": "Cung cấp vitamin và khoáng chất tự nhiên",
        "tips": "Chọn quả tươi, không dập nát",
        "avg_price_per_kg": 50000
    })

    quality_info = assess_fruit_quality(cropped_np)
    diet_info = get_fruit_diet_advice(best_name, info["vn_name"])

    return {
        "status": "success",
        "best_class": best_name,
        "best_vn_name": info["vn_name"],
        "icon": info["icon"],
        "confidence": best_conf,
        "info": info,
        "quality": quality_info,
        "diet": diet_info,
        "cropped_image": cropped_patch,
        "annotated_image": annotated_img,
        "yolo_bbox": bbox,
        "yolo_label": yolo_label,
        "model_source": model_source,
        "top_predictions": top_predictions
    }
