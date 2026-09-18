"""
quality_assessment.py - Đánh giá chất lượng trái cây: Tươi vs Dập nát/Hỏng (Fresh vs Rotten)
Môn học: Trí tuệ nhân tạo (AI) - Thị giác máy tính ứng dụng
"""

import numpy as np
import cv2
from PIL import Image

def assess_fruit_quality(image_input):
    """
    Phân tích chất lượng bề mặt quả dựa trên phân bố màu sắc, đốm đen, và tỷ lệ thâm dập.
    Trả về:
    - quality_status: 'Fresh' (Tươi), 'Ripe' (Chín già), 'Rotten' (Dập/Hỏng)
    - freshness_score: Điểm độ tươi (0 - 100%)
    - badge_color: Màu huy hiệu giao diện
    - message: Lời khuyên tiêu dùng chi tiết
    """
    if isinstance(image_input, Image.Image):
        np_img = np.array(image_input.convert("RGB"))
    else:
        np_img = image_input

    # Chuyển sang không gian màu HSV để phân tích độ bão hòa và độ sáng
    hsv = cv2.cvtColor(np_img, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(hsv)

    # 1. Phát hiện các vùng sẫm màu/thâm đen (đốm thối rữa)
    # Giá trị V (độ sáng) thấp và S (độ bão hòa) trung bình thấp
    dark_blemish_mask = cv2.inRange(hsv, np.array([0, 20, 0]), np.array([180, 255, 65]))
    blemish_ratio = np.sum(dark_blemish_mask > 0) / (np_img.shape[0] * np_img.shape[1])

    # 2. Phân tích độ đồng nhất màu sắc bề mặt (Surface Uniformity)
    std_color = np.std(s) + np.std(v)

    # 3. Tính toán điểm độ tươi (Freshness Score)
    base_score = 95.0
    penalty_blemish = blemish_ratio * 200.0  # Phạt nặng nếu diện tích thâm đen lớn
    penalty_variance = (std_color / 128.0) * 15.0

    freshness_score = max(15.0, min(99.0, base_score - penalty_blemish - penalty_variance))

    # Phân loại trạng thái
    if freshness_score >= 78.0:
        status = "Fresh"
        status_vn = "🟢 TƯƠI NGON (LOẠI 1)"
        badge_color = "#2e7d32"
        advice = "Quả đạt độ tươi xuất sắc! Vỏ căng bóng, không phát hiện vết dập nát. Bảo quản ngăn mát 4-8°C."
    elif freshness_score >= 55.0:
        status = "Ripe"
        status_vn = "🟡 CHÍN GIÀ / XUỐNG NƯỚC (LOẠI 2)"
        badge_color = "#f57f17"
        advice = "Quả đã chín già, bắt đầu xuất hiện vài điểm màu sẫm nhẹ. Khuyên dùng trong vòng 24-48 giờ hoặc làm sinh tố."
    else:
        status = "Rotten"
        status_vn = "🔴 CÓ DẤU HIỆU DẬP NÁT / HỎNG"
        badge_color = "#c62828"
        advice = "Phát hiện diện tích thâm đen, đốm sâu hoặc dấu hiệu úng dập lớn. Không nên sử dụng để bảo vệ tiêu hóa!"

    return {
        "status": status,
        "status_vn": status_vn,
        "score": round(freshness_score, 1),
        "badge_color": badge_color,
        "advice": advice,
        "blemish_percentage": round(blemish_ratio * 100, 2)
    }

