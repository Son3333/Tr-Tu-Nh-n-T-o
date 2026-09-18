"""
model.py - Kiến trúc mạng học sâu MobileNetV2 cho phân loại trái cây
Môn học: Trí tuệ nhân tạo (AI)
"""

import torch
import torch.nn as nn
from torchvision import models

def get_fruit_model(num_classes=10, pretrained=True):
    """
    Xây dựng mô hình Transfer Learning dựa trên MobileNetV2.
    - MobileNetV2 sử dụng các khối Inverted Residuals & Linear Bottlenecks
    - Trọng lượng nhẹ, tốc độ suy luận cực nhanh, phù hợp ứng dụng thực tế.
    """
    try:
        if pretrained:
            weights = models.MobileNet_V2_Weights.DEFAULT
            model = models.mobilenet_v2(weights=weights)
        else:
            model = models.mobilenet_v2(weights=None)
    except Exception:
        model = models.mobilenet_v2(weights=None)

    # Đóng băng (Freeze) các tầng trích xuất đặc trưng ban đầu để giữ tri thức chung
    for param in model.features[:-4].parameters():
        param.requires_grad = False

    # Thay thế phần phân loại (Classifier Head) bằng Custom MLP phù hợp với số lớp trái cây
    in_features = model.classifier[1].in_features  # 1280
    model.classifier = nn.Sequential(
        nn.Dropout(p=0.3),
        nn.Linear(in_features, 256),
        nn.BatchNorm1d(256),
        nn.ReLU(inplace=True),
        nn.Dropout(p=0.2),
        nn.Linear(256, num_classes)
    )

    return model

if __name__ == "__main__":
    net = get_fruit_model(10, pretrained=False)
    dummy_input = torch.randn(2, 3, 224, 224)
    out = net(dummy_input)
    print(f"Kiểm tra thành công! Output shape: {out.shape}")

