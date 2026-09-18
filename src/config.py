"""
config.py - Cấu hình hệ thống nhận diện và phân loại 100 loại trái cây
Môn học: Trí tuệ nhân tạo (AI) - Đề tài số 22
"""

import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.fruit_library_600 import FRUIT_LIBRARY_600

# Đường dẫn thư mục gốc
BASE_DIR = PROJECT_ROOT
DATASET_DIR = os.path.join(BASE_DIR, "dataset")
MODELS_DIR = os.path.join(BASE_DIR, "models")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
MODEL_PATH = os.path.join(MODELS_DIR, "best_fruit_model.pth")

# Đảm bảo các thư mục tồn tại
for d in [DATASET_DIR, MODELS_DIR, REPORTS_DIR]:
    os.makedirs(d, exist_ok=True)

# Kích thước ảnh chuẩn hóa cho mạng MobileNetV2
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32
NUM_EPOCHS = 15
LEARNING_RATE = 0.0003

# Toàn bộ danh mục 100 loại trái cây
CLASS_INFO = FRUIT_LIBRARY_600
CLASS_NAMES = list(CLASS_INFO.keys())
NUM_CLASSES = len(CLASS_NAMES)
