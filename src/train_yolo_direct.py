"""
train_yolo_direct.py - Huấn luyện Trực tiếp Mô hình Deep Learning YOLOv8 trên máy
Đề tài số 22: Hệ thống AI Nhận diện & Phân loại Trái cây Thông minh
Tự động huấn luyện mô hình YOLOv8 Classification chính thức, xuất weights best.pt và ONNX.
"""

import os
import sys
import shutil
import time

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

DATASET_DIR = os.path.join(PROJECT_ROOT, "dataset")
MODELS_DIR = os.path.join(PROJECT_ROOT, "models")
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports")
RUNS_DIR = os.path.join(PROJECT_ROOT, "runs", "classify", "yolo_direct_train")

os.makedirs(MODELS_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

def train_yolo_direct(epochs=5, imgsz=128, batch=64):
    print("=" * 75)
    print("   KHỞI CHẠY HUẤN LUYỆN TRỰC TIẾP MÔ HÌNH HỌC SÂU YOLOV8 CHÍNH THỨC   ")
    print("=" * 75)
    t0 = time.time()

    print(f"[*] Cấu hình huấn luyện: Epochs={epochs} | ImgSize={imgsz}x{imgsz} | BatchSize={batch}")
    print("[*] Đang tải mạng nơ-ron YOLOv8 Nano Classifier...")
    try:
        from ultralytics import YOLO
        model = YOLO("yolov8n-cls.pt")
    except Exception as e:
        print(f"[!] Không thể nạp PyTorch/Ultralytics trực tiếp ({e}). Chuyển sang huấn luyện engine đặc trưng...")
        from src.train_600_engine import train_600_fruit_model
        train_600_fruit_model()
        return

    print("[*] Bắt đầu quá trình huấn luyện chuyển giao (Transfer Learning)...")
    results = model.train(
        data=DATASET_DIR,
        epochs=epochs,
        imgsz=imgsz,
        batch=batch,
        device="cpu",
        project=os.path.join(PROJECT_ROOT, "runs", "classify"),
        name="yolo_direct_train",
        exist_ok=True,
        workers=0,
        verbose=True
    )

    best_pt_source = os.path.join(PROJECT_ROOT, "runs", "classify", "yolo_direct_train", "weights", "best.pt")
    target_pt = os.path.join(MODELS_DIR, "yolov8_fruit_cls.pt")
    target_best = os.path.join(MODELS_DIR, "best.pt")

    if os.path.exists(best_pt_source):
        shutil.copy(best_pt_source, target_pt)
        shutil.copy(best_pt_source, target_best)
        print(f"[OK] Đã lưu trọng số YOLOv8 tốt nhất vào: {target_pt}")
        print(f"[OK] Đã đồng bộ sang: {target_best}")

        # Xuất sang file ONNX
        try:
            print("[*] Đang xuất mô hình sang định dạng ONNX...")
            trained_model = YOLO(target_pt)
            trained_model.export(format="onnx")
            onnx_path = target_pt.replace(".pt", ".onnx")
            if os.path.exists(onnx_path):
                print(f"[OK] Đã xuất thành công mô hình ONNX: {onnx_path}")
        except Exception as e:
            print(f"[!] Bỏ qua xuất ONNX: {e}")

    # Copy biểu đồ kết quả nếu có
    results_png = os.path.join(PROJECT_ROOT, "runs", "classify", "yolo_direct_train", "results.png")
    if os.path.exists(results_png):
        shutil.copy(results_png, os.path.join(REPORTS_DIR, "yolo_results.png"))
        print(f"[OK] Đã lưu biểu đồ huấn luyện YOLOv8 vào: {os.path.join(REPORTS_DIR, 'yolo_results.png')}")

    elapsed = time.time() - t0
    print("=" * 75)
    print(f"[THÀNH CÔNG RỰC RỠ] Quá trình huấn luyện YOLOv8 trực tiếp hoàn tất trong {elapsed:.1f} giây!")
    print("=" * 75)

if __name__ == "__main__":
    train_yolo_direct(epochs=5, imgsz=128, batch=64)

