"""
diet_advisor.py - Trợ lý thực đơn & chế độ ăn thông minh từ trái cây nhận diện
Môn học: Trí tuệ nhân tạo (AI)
"""

DIET_DATABASE = {
    "WeightLoss": {
        "title": "Chế độ Giảm cân & Giữ dáng",
        "description": "Ưu tiên quả ít calo, giàu chất xơ và nước, chỉ số đường huyết (GI) thấp.",
        "best_fruits": ["Apple", "Grapefruit", "Watermelon", "Strawberry", "Guava", "Blueberry", "Lemon", "Kiwi"]
    },
    "GymFitness": {
        "title": "Chế độ Tập Gym & Tăng cơ",
        "description": "Bổ sung năng lượng tức thì, Kali chống chuột rút và chất béo lành mạnh.",
        "best_fruits": ["Banana", "Avocado", "Coconut", "Mango", "Date", "Durian"]
    },
    "HealthyGlow": {
        "title": "Dưỡng da & Trẻ hóa (Chống lão hóa)",
        "description": "Dồi dào Vitamin C và chất chống oxy hóa Anthocyanin kích thích tạo Collagen.",
        "best_fruits": ["Strawberry", "Orange", "Cherry", "Pomegranate", "Blueberry", "Peach", "Papaya", "Acerola"]
    }
}

def get_fruit_diet_advice(class_name, vn_name=None):
    """Gợi ý món ăn và chế độ dinh dưỡng tương thích cho loại quả được quét"""
    if vn_name is None:
        from src.config import CLASS_INFO
        vn_name = CLASS_INFO.get(class_name, {}).get("vn_name", class_name)
    # Gợi ý món ngon
    recipes = [
        f"🥤 Sinh tố {vn_name} thanh mát kết hợp sữa tươi ít đường & hạt chia.",
        f"🥗 Salad rau xanh trộn {vn_name} tươi sốt sữa chua Hy Lạp.",
        f"🥣 Bát yến mạch ngâm qua đêm (Overnight Oats) phủ lát {vn_name} giòn ngọt.",
        f"🍹 Nước ép Detox {vn_name} thanh lọc gan và giải nhiệt cơ thể."
    ]

    # Kiểm tra phù hợp chế độ nào
    tags = []
    for mode, data in DIET_DATABASE.items():
        if class_name in data["best_fruits"]:
            tags.append(data["title"])

    if not tags:
        tags.append("Chế độ ăn lành mạnh hằng ngày")

    return {
        "recipes": recipes[:2],
        "suitable_diets": tags,
        "glycemic_index": "Thấp - Trung bình (An toàn cho sức khỏe)"
    }

