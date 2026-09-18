"""
auto_augment.py - Hệ thống Tự học & Tăng cường Dữ liệu (Active Data Augmentation)
Mở rộng dữ liệu cho 101 loại trái cây:
- Đa dạng hóa góc chụp: Xoay nghiêng +/-12 độ, lật gương ngang
- Đa dạng hóa môi trường ánh sáng: Bù sáng ngoài trời, giảm sáng trong phòng
- Giúp mô hình AI học thêm hàng nghìn góc độ mới, tăng độ bền vững và mạnh mẽ
"""

import os
import sys
import time
import cv2
import numpy as np

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.train_engine import cv2_imread_unicode, train_model
from src.colab_sync import create_colab_training_package

DATASET_TRAIN = os.path.join(PROJECT_ROOT, "dataset", "train")

def augment_image(img):
    """Tạo ra 3 biến thể chất lượng cao cho mỗi ảnh gốc"""
    h, w = img.shape[:2]
    augmented = []

    # 1. Lật gương ngang (Horizontal Flip)
    flipped = cv2.flip(img, 1)
    augmented.append(('flip', flipped))

    # 2. Xoay góc nghiêng +12 độ
    M_rot = cv2.getRotationMatrix2D((w // 2, h // 2), 12, 1.0)
    rotated = cv2.warpAffine(img, M_rot, (w, h), borderMode=cv2.BORDER_REFLECT_101)
    augmented.append(('rot12', rotated))

    # 3. Điều chỉnh độ sáng (Brightness boost - ánh sáng tự nhiên)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    v = hsv[:, :, 2].astype(np.float32)
    v = np.clip(v * 1.15 + 10, 0, 255).astype(np.uint8)
    hsv[:, :, 2] = v
    bright = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    augmented.append(('bright', bright))

    return augmented

def run_auto_learning(target_samples_per_class=20):
    """
    Tự động mở rộng dữ liệu cho các phân lớp ít mẫu, đưa vào huấn luyện mô hình ngay lập tức.
    """
    print("=" * 65)
    print("   BẮT ĐẦU QUÁ TRÌNH TỰ HỌC & TĂNG CƯỜNG DỮ LIỆU (ACTIVE LEARNING)   ")
    print("=" * 65)

    classes = sorted([d for d in os.listdir(DATASET_TRAIN) if os.path.isdir(os.path.join(DATASET_TRAIN, d))])
    total_added = 0
    t0 = time.time()

    for idx, c_name in enumerate(classes):
        c_dir = os.path.join(DATASET_TRAIN, c_name)
        existing_files = [f for f in os.listdir(c_dir) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
        
        # Chỉ tăng cường cho các file gốc (tránh lặp vô hạn các file aug)
        base_files = [f for f in existing_files if not f.startswith('aug_')]
        if len(base_files) == 0:
            base_files = existing_files

        current_count = len(existing_files)
        if current_count < target_samples_per_class:
            needed = target_samples_per_class - current_count
            added_for_class = 0
            
            for f in base_files:
                if added_for_class >= needed:
                    break
                f_path = os.path.join(c_dir, f)
                img = cv2_imread_unicode(f_path)
                if img is None:
                    continue

                variants = augment_image(img)
                for var_name, var_img in variants:
                    if added_for_class >= needed:
                        break
                    save_name = f"aug_{int(time.time())}_{added_for_class}_{var_name}.jpg"
                    save_path = os.path.join(c_dir, save_name)
                    
                    # Lưu ảnh hỗ trợ đường dẫn Unicode trên Windows
                    is_success, buf = cv2.imencode(".jpg", var_img, [cv2.IMWRITE_JPEG_QUALITY, 92])
                    if is_success:
                        with open(save_path, "wb") as out_f:
                            out_f.write(buf)
                        added_for_class += 1
                        total_added += 1

    elapsed = time.time() - t0
    print(f"[OK] Đã tự sinh và bổ sung thành công {total_added} ảnh dữ liệu mới vào tập Train!")
    print(f"[*] Thời gian xử lý: {elapsed:.2f} giây.")

    # Tiến hành Huấn luyện lại ngay lập tức
    print("\n[*] Đang kích hoạt Huấn luyện lại toàn bộ mô hình trên kho dữ liệu mới...")
    train_model()

    # Đóng gói lại file ZIP cho Colab
    print("\n[*] Đang cập nhật gói nén dataset...")
    create_colab_training_package()
    print("[THÀNH CÔNG] Toàn bộ hệ thống đã được nạp dữ liệu và huấn luyện hoàn tất!")

if __name__ == "__main__":
    run_auto_learning(target_samples_per_class=22)

