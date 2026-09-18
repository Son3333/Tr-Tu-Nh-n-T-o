# colab_sync.py - Module Quản lý Tự học & Đóng gói Huấn luyện YOLOv8 trên Google Colab
import os
import json
import time
import zipfile
import shutil
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_DIR = os.path.join(BASE_DIR, 'dataset')
TRAIN_DIR = os.path.join(DATASET_DIR, 'train')
VAL_DIR = os.path.join(DATASET_DIR, 'val')
MODELS_DIR = os.path.join(BASE_DIR, 'models')
DATA_DIR = os.path.join(BASE_DIR, 'data')
ZIP_PACKAGE_PATH = os.path.join(BASE_DIR, 'fruit_dataset_yolo.zip')
MEMORY_FILE = os.path.join(DATA_DIR, 'active_learning_memory.json')

def get_dataset_stats():
    """
    Thống kê tổng số lượng ảnh hiện có và số lượng ảnh tự học mới thêm vào.
    """
    stats = {
        'total_train_images': 0,
        'total_val_images': 0,
        'total_classes': 0,
        'newly_learned_count': 0,
        'classes_summary': {}
    }
    
    from src.config import CLASS_NAMES
    stats['total_classes'] = len(CLASS_NAMES)
    if os.path.exists(TRAIN_DIR):
        classes = [d for d in os.listdir(TRAIN_DIR) if os.path.isdir(os.path.join(TRAIN_DIR, d))]
        for c in classes:
            c_dir = os.path.join(TRAIN_DIR, c)
            files = [f for f in os.listdir(c_dir) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
            learned_files = [f for f in files if f.startswith('learned_')]
            stats['total_train_images'] += len(files)
            stats['newly_learned_count'] += len(learned_files)
            stats['classes_summary'][c] = {
                'total': len(files),
                'learned': len(learned_files)
            }
            
    if os.path.exists(VAL_DIR):
        for c in os.listdir(VAL_DIR):
            c_dir = os.path.join(VAL_DIR, c)
            if os.path.isdir(c_dir):
                files = [f for f in os.listdir(c_dir) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
                stats['total_val_images'] += len(files)

    return stats

def save_learned_sample(pil_img, class_name, note="Tự học qua Web App"):
    """
    Tự học: Lưu ảnh mới được hiệu chỉnh trực tiếp vào tập dữ liệu train của quả tương ứng.
    """
    fruit_dir = os.path.join(TRAIN_DIR, class_name)
    os.makedirs(fruit_dir, exist_ok=True)
    
    timestamp = int(time.time())
    img_filename = f"learned_{timestamp}_{int(time.time() * 1000) % 1000}.jpg"
    save_path = os.path.join(fruit_dir, img_filename)
    
    try:
        pil_img.convert('RGB').save(save_path, 'JPEG', quality=95)
    except Exception as e:
        return False, f"Lỗi lưu file ảnh: {e}"

    # Ghi nhận vào bộ nhớ Active Learning
    os.makedirs(DATA_DIR, exist_ok=True)
    memory = {}
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
                memory = json.load(f)
        except Exception:
            memory = {}

    entry_key = f"{class_name}_{timestamp}"
    memory[entry_key] = {
        'fruit_class': class_name,
        'saved_file': save_path,
        'learned_at': time.strftime('%Y-%m-%d %H:%M:%S'),
        'user_note': note
    }
    
    try:
        with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(memory, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

    return True, save_path

def create_colab_training_package(output_zip=ZIP_PACKAGE_PATH):
    """
    Đóng gói toàn bộ tập dữ liệu dataset thành file ZIP chuẩn cấu trúc của Ultralytics YOLOv8 Classification.
    Cấu trúc file zip:
    fruit_dataset/
      ├── train/
      │     ├── Apple/
      │     ├── Pear/
      │     └── ...
      └── val/
            ├── Apple/
            ├── Pear/
            └── ...
    """
    if not os.path.exists(DATASET_DIR):
        return False, "Không tìm thấy thư mục dataset!"

    if os.path.exists(output_zip):
        try:
            os.remove(output_zip)
        except Exception:
            pass

    try:
        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(DATASET_DIR):
                for file in files:
                    if file.lower().endswith(('.jpg', '.png', '.jpeg')):
                        file_path = os.path.join(root, file)
                        rel_path = os.path.relpath(file_path, BASE_DIR)
                        zipf.write(file_path, rel_path)
                        
        zip_size_mb = os.path.getsize(output_zip) / (1024 * 1024)
        return True, f"Đã đóng gói thành công file '{os.path.basename(output_zip)}' ({zip_size_mb:.2f} MB)"
    except Exception as e:
        return False, f"Lỗi đóng gói zip: {e}"

def check_yolo_model_status():
    """
    Kiểm tra xem mô hình YOLOv8 tùy biến đã được huấn luyện từ Colab tải về chưa.
    """
    model_paths = [
        os.path.join(MODELS_DIR, 'yolov8_fruit_trained.json'),
        os.path.join(MODELS_DIR, 'best.pt'),
        os.path.join(MODELS_DIR, 'yolov8_fruit_cls.pt'),
        os.path.join(MODELS_DIR, 'yolov8_fruit_cls.onnx'),
        os.path.join(BASE_DIR, 'best.pt')
    ]
    for p in model_paths:
        if os.path.exists(p):
            size_mb = os.path.getsize(p) / (1024 * 1024)
            mtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(p)))
            return True, p, size_mb, mtime
    return False, None, 0, None

