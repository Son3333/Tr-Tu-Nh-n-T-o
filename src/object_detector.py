# object_detector.py - Tiền trạm YOLOv8 nhận diện vật thể & phân định người vs trái cây
import os
import cv2
import numpy as np
from PIL import Image

_DETECTOR_MODEL = None
_YOLO_LOADED = False

# Các nhãn COCO liên quan đến thực phẩm, trái cây hoặc vật thể hình cầu hữu cơ
FRUIT_COCO_CLASSES = {
    46: 'banana',
    47: 'apple',
    49: 'orange',
    50: 'broccoli',
    51: 'carrot',
    52: 'hot dog',
    53: 'pizza',
    54: 'donut',
    55: 'cake',
    32: 'sports ball',  # YOLO thường nhận diện quả lê, bưởi, dưa tròn thành sports ball
    45: 'bowl',         # Đĩa/bát đựng trái cây
}

def get_yolo_detector():
    global _DETECTOR_MODEL, _YOLO_LOADED
    if not _YOLO_LOADED:
        _YOLO_LOADED = True
        try:
            from ultralytics import YOLO
            model_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'yolov8n.pt')
            if not os.path.exists(model_path):
                model_path = 'yolov8n.pt'
            if os.path.exists(model_path):
                _DETECTOR_MODEL = YOLO(model_path)
        except Exception:
            _DETECTOR_MODEL = None
    return _DETECTOR_MODEL

def detect_and_crop_fruit(pil_image, conf_threshold=0.25):
    """
    Tiền trạm YOLOv8 thông minh:
    - Bắt chính xác vùng trái cây thật, loại bỏ mặt bàn, ngón tay.
    - Phát hiện nếu đối tượng là người (person - class 0) để chặn triệt để, không cho nhận nhầm thành hoa quả.
    - Loại bỏ triệt để các box nhiễu quá nhỏ (như false alarm boat, clock, car,...).
    """
    w, h = pil_image.size
    total_area = float(w * h)
    np_img = np.array(pil_image.convert('RGB'))
    model = get_yolo_detector()
    
    try:
        results = model.predict(np_img, conf=conf_threshold, verbose=False)
    except Exception:
        crop_fallback = pil_image.crop((int(w * 0.03), int(h * 0.03), int(w * 0.97), int(h * 0.97)))
        return crop_fallback, pil_image, None, 'direct', False

    best_box = None
    best_area = 0
    best_label = 'fruit'
    is_person_detected = False
    person_box_area = 0

    if results and len(results) > 0:
        boxes = results[0].boxes
        for box in boxes:
            cls_id = int(box.cls[0].item())
            conf_val = float(box.conf[0].item())
            xyxy = box.xyxy[0].cpu().numpy().astype(int)
            bx1, by1, bx2, by2 = xyxy
            bw = bx2 - bx1
            bh = by2 - by1
            area = bw * bh

            # Kiểm tra xem có người không (COCO class 0: person)
            if cls_id == 0:
                if conf_val >= 0.30 and area >= 0.12 * total_area:
                    is_person_detected = True
                    person_box_area = max(person_box_area, area)
                continue

            # LỌC BỎ NHIỄU: Chỉ chấp nhận các lớp thực phẩm / quả / hình cầu hoặc box hợp lệ
            if cls_id not in FRUIT_COCO_CLASSES:
                # Nếu là các vật thể vô lý (thuyền, xe cộ, đồng hồ, máy tính...), bỏ qua ngay!
                continue

            # Lọc kích thước tối thiểu: Quả phải chiếm tối thiểu 10% chiều rộng/dài và >2% diện tích ảnh
            if bw < max(25, int(w * 0.10)) or bh < max(25, int(h * 0.10)) or area < 0.02 * total_area:
                continue

            # Tính điểm ưu tiên cho trái cây COCO
            priority_score = area * (2.0 if cls_id in [46, 47, 49, 32] else 1.0)

            if priority_score > best_area:
                best_area = priority_score
                best_box = (bx1, by1, bx2, by2)
                best_label = FRUIT_COCO_CLASSES.get(cls_id, 'fruit')

    # Nếu phát hiện người mà KHÔNG có vùng trái cây cụ thể nào bên trong/bên cạnh
    if is_person_detected and best_box is None:
        # Bức ảnh này là con người!
        annotated_np = np_img.copy()
        cv2.putText(annotated_np, 'DETECTED: PERSON / HUMAN', (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2, cv2.LINE_AA)
        return None, Image.fromarray(annotated_np), None, 'person', True

    # Nếu có quả được YOLO bắt trúng
    if best_box is not None:
        bx1, by1, bx2, by2 = best_box
        bw = bx2 - bx1
        bh = by2 - by1

        pad_x = int(bw * 0.08)
        pad_y = int(bh * 0.08)

        cx1 = max(0, bx1 - pad_x)
        cy1 = max(0, by1 - pad_y)
        cx2 = min(w, bx2 + pad_x)
        cy2 = min(h, by2 + pad_y)

        cropped_patch = pil_image.crop((cx1, cy1, cx2, cy2))

        annotated_np = np_img.copy()
        cv2.rectangle(annotated_np, (cx1, cy1), (cx2, cy2), (0, 220, 100), 3)
        label_text = f'YOLO: {best_label}'
        cv2.putText(annotated_np, label_text, (cx1, max(25, cy1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 220, 100), 2, cv2.LINE_AA)

        annotated_pil = Image.fromarray(annotated_np)
        return cropped_patch, annotated_pil, (cx1, cy1, cx2, cy2), best_label, False

    # Trường hợp ảnh quả chiếm toàn khung (như ảnh trong dataset hoặc chụp cận cảnh)
    # Cắt viền 4% nhẹ để loại viền đen camera
    crop_fallback = pil_image.crop((int(w * 0.03), int(h * 0.03), int(w * 0.97), int(h * 0.97)))
    return crop_fallback, pil_image, None, 'full_frame', False
