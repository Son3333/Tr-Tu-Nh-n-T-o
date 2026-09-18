"""
dataset_builder.py - Quản lý tiền xử lý và tập dữ liệu 100 loại trái cây
Môn học: Trí tuệ nhân tạo (AI)
"""

import os
import sys
import random
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

from PIL import Image, ImageDraw, ImageFilter
import torch
from torchvision import transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader

from src.config import DATASET_DIR, IMAGE_SIZE, BATCH_SIZE, CLASS_NAMES

# Pipeline tăng cường dữ liệu (Data Augmentation) cho tập huấn luyện (Train)
train_transforms = transforms.Compose([
    transforms.Resize(IMAGE_SIZE),
    transforms.RandomResizedCrop(IMAGE_SIZE, scale=(0.8, 1.0)),
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomRotation(degrees=20),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Pipeline chuẩn hóa cho tập kiểm thử/đánh giá (Validation & Test)
val_transforms = transforms.Compose([
    transforms.Resize(IMAGE_SIZE),
    transforms.CenterCrop(IMAGE_SIZE),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

def create_synthetic_fruit_image(class_name, size=(224, 224)):
    """
    Sinh ảnh mô phỏng có màu sắc và hình khối đặc trưng dựa trên class_name.
    """
    bg_val = random.randint(235, 255)
    img = Image.new("RGB", size, (bg_val, bg_val - random.randint(0, 10), bg_val - random.randint(0, 15)))
    draw = ImageDraw.Draw(img)

    w, h = size
    cx = w // 2 + random.randint(-10, 10)
    cy = h // 2 + random.randint(-10, 10)
    r = random.randint(55, 75)

    # Sinh màu sắc hạt giống dựa trên tên quả
    h_val = abs(hash(class_name))
    red_base = (h_val * 7) % 200 + 40
    green_base = (h_val * 13) % 200 + 40
    blue_base = (h_val * 19) % 200 + 40

    r_c = min(255, max(0, red_base + random.randint(-15, 15)))
    g_c = min(255, max(0, green_base + random.randint(-15, 15)))
    b_c = min(255, max(0, blue_base + random.randint(-15, 15)))
    fruit_color = (r_c, g_c, b_c)
    accent_color = (max(0, r_c - 40), max(0, g_c - 40), max(0, b_c - 40))

    shape_type = h_val % 5

    if shape_type == 0:  # Tròn bầu
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fruit_color, outline=accent_color, width=3)
        draw.rectangle([cx - 3, cy - r - 12, cx + 3, cy - r], fill=(100, 60, 20))
        draw.ellipse([cx + 2, cy - r - 15, cx + 18, cy - r - 5], fill=(50, 150, 40))

    elif shape_type == 1:  # Thuôn dài / Chuối / Dưa leo
        draw.ellipse([cx - r + 15, cy - r - 15, cx + r - 15, cy + r + 25], fill=fruit_color, outline=accent_color, width=3)
        draw.rectangle([cx - 3, cy - r - 25, cx + 3, cy - r - 15], fill=(110, 70, 25))

    elif shape_type == 2:  # Chùm / Hạt nhỏ (Nho / Việt quất)
        for ox, oy in [(-16, -16), (0, -20), (16, -16), (-20, 0), (0, 0), (20, 0), (-10, 18), (10, 18), (0, 32)]:
            dx, dy = cx + ox + random.randint(-3, 3), cy + oy + random.randint(-3, 3)
            draw.ellipse([dx - 14, dy - 14, dx + 14, dy + 14], fill=fruit_color, outline=accent_color, width=2)
        draw.line([(cx, cy - 25), (cx + 3, cy - 45)], fill=(90, 60, 30), width=4)

    elif shape_type == 3:  # Hình nón / Dâu tây
        pts = [(cx, cy + r + 8), (cx - r + 10, cy - r + 12), (cx + r - 10, cy - r + 12)]
        draw.polygon(pts, fill=fruit_color, outline=accent_color)
        draw.polygon([(cx, cy - r + 10), (cx - 15, cy - r - 8), (cx + 15, cy - r - 8)], fill=(50, 150, 40))

    else:  # Gai / Sần sùi (Mít / Sầu riêng / Mãng cầu)
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fruit_color, outline=accent_color, width=3)
        for _ in range(25):
            sx = random.randint(cx - r + 8, cx + r - 8)
            sy = random.randint(cy - r + 8, cy + r - 8)
            draw.polygon([(sx, sy - 4), (sx - 3, sy + 3), (sx + 3, sy + 3)], fill=accent_color)

    return img.filter(ImageFilter.SMOOTH_MORE)

def ensure_dataset_ready(samples_per_class=15):
    """
    Đảm bảo có tập dữ liệu cho 100 loại quả.
    """
    train_dir = os.path.join(DATASET_DIR, "train")
    val_dir = os.path.join(DATASET_DIR, "val")
    
    val_samples = 3
    train_samples = samples_per_class - val_samples

    for c in CLASS_NAMES:
        c_train = os.path.join(train_dir, c)
        c_val = os.path.join(val_dir, c)
        os.makedirs(c_train, exist_ok=True)
        os.makedirs(c_val, exist_ok=True)

        if len(os.listdir(c_train)) < 3:
            for i in range(train_samples):
                img = create_synthetic_fruit_image(c)
                img.save(os.path.join(c_train, f"{c}_train_{i+1:03d}.jpg"), quality=95)

        if len(os.listdir(c_val)) < 2:
            for j in range(val_samples):
                img = create_synthetic_fruit_image(c)
                img.save(os.path.join(c_val, f"{c}_val_{j+1:03d}.jpg"), quality=95)

def get_dataloaders():
    ensure_dataset_ready()
    train_dir = os.path.join(DATASET_DIR, "train")
    val_dir = os.path.join(DATASET_DIR, "val")

    train_dataset = ImageFolder(train_dir, transform=train_transforms)
    val_dataset = ImageFolder(val_dir, transform=val_transforms)

    train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=0)
    val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False, num_workers=0)

    return train_loader, val_loader, train_dataset.classes
