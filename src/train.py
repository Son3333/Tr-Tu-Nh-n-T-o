"""
train.py - Pipeline huấn luyện và đánh giá mô hình MobileNetV2
Môn học: Trí tuệ nhân tạo (AI) - Đề tài 22
"""

import os
import sys
import time

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

# Đảm bảo nhận diện đúng package gốc dù chạy từ đâu
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from src.config import (
    MODEL_PATH, REPORTS_DIR, NUM_EPOCHS, LEARNING_RATE, CLASS_NAMES
)
from src.dataset_builder import get_dataloaders
from src.model import get_fruit_model

def train_and_evaluate():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[*] Thiết bị đang sử dụng để huấn luyện: {device}")

    # 1. Chuẩn bị DataLoader
    print("[*] Đang tải dữ liệu...")
    train_loader, val_loader, class_names = get_dataloaders()
    num_classes = len(class_names)
    print(f"[OK] Số lớp phân loại: {num_classes} ({class_names})")
    print(f"[OK] Số mẫu Train: {len(train_loader.dataset)} | Số mẫu Val: {len(val_loader.dataset)}")

    # 2. Khởi tạo mô hình
    print("[*] Khởi tạo mô hình MobileNetV2 với Transfer Learning...")
    model = get_fruit_model(num_classes=num_classes, pretrained=True)
    model.to(device)

    # 3. Hàm mất mát và Tối ưu hóa
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(filter(lambda p: p.requires_grad, model.parameters()), lr=LEARNING_RATE, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=NUM_EPOCHS)

    # Lịch sử ghi nhận
    history = {
        "train_loss": [],
        "train_acc": [],
        "val_loss": [],
        "val_acc": []
    }

    best_val_acc = 0.0
    start_time = time.time()

    print("\n" + "="*50)
    print(" BẮT ĐẦU QUÁ TRÌNH HUẤN LUYỆN MÔ HÌNH AI ")
    print("="*50)

    for epoch in range(1, NUM_EPOCHS + 1):
        # --- Giai đoạn Train ---
        model.train()
        running_loss = 0.0
        correct_train = 0
        total_train = 0

        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item() * images.size(0)
            _, preds = torch.max(outputs, 1)
            correct_train += torch.sum(preds == labels.data).item()
            total_train += labels.size(0)

        scheduler.step()

        epoch_train_loss = running_loss / total_train
        epoch_train_acc = (correct_train / total_train) * 100.0

        # --- Giai đoạn Validation ---
        model.eval()
        val_loss = 0.0
        correct_val = 0
        total_val = 0

        with torch.no_grad():
            for images, labels in val_loader:
                images, labels = images.to(device), labels.to(device)
                outputs = model(images)
                loss = criterion(outputs, labels)

                val_loss += loss.item() * images.size(0)
                _, preds = torch.max(outputs, 1)
                correct_val += torch.sum(preds == labels.data).item()
                total_val += labels.size(0)

        epoch_val_loss = val_loss / total_val
        epoch_val_acc = (correct_val / total_val) * 100.0

        # Lưu lịch sử
        history["train_loss"].append(epoch_train_loss)
        history["train_acc"].append(epoch_train_acc)
        history["val_loss"].append(epoch_val_loss)
        history["val_acc"].append(epoch_val_acc)

        print(f"Epoch [{epoch:02d}/{NUM_EPOCHS:02d}] - "
              f"Train Loss: {epoch_train_loss:.4f} | Train Acc: {epoch_train_acc:.2f}% | "
              f"Val Loss: {epoch_val_loss:.4f} | Val Acc: {epoch_val_acc:.2f}%")

        # Lưu checkpoint mô hình tốt nhất
        if epoch_val_acc >= best_val_acc:
            best_val_acc = epoch_val_acc
            torch.save(model.state_dict(), MODEL_PATH)
            print(f"  --> [Saved] Mô hình tốt nhất được lưu tại {MODEL_PATH} (Độ chính xác: {best_val_acc:.2f}%)")

    total_time = time.time() - start_time
    print("="*50)
    print(f"[*] Huấn luyện hoàn tất trong {total_time:.1f} giây!")
    print(f"[*] Độ chính xác cao nhất trên tập Validation: {best_val_acc:.2f}%")

    # 4. Vẽ biểu đồ Lịch sử Huấn luyện (Accuracy & Loss)
    plot_training_history(history)

    # 5. Tính toán và vẽ Ma trận Nhầm lẫn (Confusion Matrix)
    plot_confusion_matrix(model, val_loader, class_names, device)

def plot_training_history(history):
    """
    Vẽ và lưu biểu đồ Loss & Accuracy qua các Epoch.
    """
    epochs_range = range(1, len(history["train_loss"]) + 1)
    
    plt.figure(figsize=(12, 5))

    # Biểu đồ Accuracy
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, history["train_acc"], label="Train Accuracy", marker="o", color="#2ecc71")
    plt.plot(epochs_range, history["val_acc"], label="Val Accuracy", marker="s", color="#3498db")
    plt.title("Độ chính xác qua các Epochs (Accuracy)", fontsize=13, fontweight="bold")
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy (%)")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)

    # Biểu đồ Loss
    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, history["train_loss"], label="Train Loss", marker="o", color="#e74c3c")
    plt.plot(epochs_range, history["val_loss"], label="Val Loss", marker="s", color="#f39c12")
    plt.title("Hàm mất mát qua các Epochs (Loss)", fontsize=13, fontweight="bold")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)

    plt.tight_layout()
    chart_path = os.path.join(REPORTS_DIR, "training_history.png")
    plt.savefig(chart_path, dpi=300)
    plt.close()
    print(f"[OK] Đã lưu biểu đồ huấn luyện: {chart_path}")

def plot_confusion_matrix(model, val_loader, class_names, device):
    """
    Tính ma trận nhầm lẫn và lưu biểu đồ Heatmap.
    """
    all_preds = []
    all_labels = []

    model.eval()
    with torch.no_grad():
        for images, labels in val_loader:
            images = images.to(device)
            outputs = model(images)
            _, preds = torch.max(outputs, 1)
            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.numpy())

    num_classes = len(class_names)
    matrix = np.zeros((num_classes, num_classes), dtype=int)
    for t, p in zip(all_labels, all_preds):
        matrix[t, p] += 1

    plt.figure(figsize=(10, 8))
    sns.heatmap(matrix, annot=True, fmt="d", cmap="Blues",
                xticklabels=class_names, yticklabels=class_names)
    plt.title("Ma trận nhầm lẫn (Confusion Matrix)", fontsize=14, fontweight="bold")
    plt.xlabel("Dự đoán (Predicted)")
    plt.ylabel("Thực tế (Ground Truth)")
    plt.xticks(rotation=45, ha="right")
    plt.yticks(rotation=0)

    plt.tight_layout()
    cm_path = os.path.join(REPORTS_DIR, "confusion_matrix.png")
    plt.savefig(cm_path, dpi=300)
    plt.close()
    print(f"[OK] Đã lưu ma trận nhầm lẫn: {cm_path}")

if __name__ == "__main__":
    train_and_evaluate()

