"""
fruit_chatbot.py - Bộ xử lý ngôn ngữ tự nhiên & Cập nhật quả tức thì (Active Learning)
Môn học: Trí tuệ nhân tạo (AI)
Hỗ trợ cả tiếng Việt có dấu, KHÔNG DẤU, viết tắt, gõ lỗi telex.
Khi người dùng bảo quả gì -> Đổi ngay sang quả đó, không lải nhải lan man.
"""

import re
import unicodedata
from src.config import CLASS_INFO, CLASS_NAMES

def strip_accents(text):
    """Bỏ dấu tiếng Việt: 'Lê' -> 'le', 'Đào' -> 'dao', 'Dừa' -> 'dua'"""
    t = unicodedata.normalize('NFD', text)
    t = re.sub(r'[\u0300-\u036f]', '', t)
    t = t.replace('đ', 'd').replace('Đ', 'd')
    return t.lower()

def normalize_text(text):
    """Chuẩn hóa viết tắt, lỗi telex phổ biến"""
    t = text.lower().strip()
    typo_map = {
        r"\bqua\s+r\b": "quả",
        r"\bqua\b": "quả",
        r"\btrie\b": "trái",
        r"\btrai\b": "trái",
        r"\bko\b": "không",
        r"\bk\b": "không",
        r"\bk\s+phai\b": "không phải",
        r"\bdeo\b": "đéo",
        r"\bhem\b": "không",
        r"\bhong\b": "không",
        r"\bđou\b": "đâu",
        r"\bchớ\b": "chứ",
        r"\bnhung\b": "nhưng",
        r"\bnoa\b": "nó",
        r"\bno\b": "nó",
    }
    for p, r_str in typo_map.items():
        t = re.sub(p, r_str, t)
    return t

def find_fruits_in_text(text):
    """
    Tìm kiếm quả trong câu người dùng, hỗ trợ CẢ CÓ DẤU LẪN KHÔNG DẤU.
    Ví dụ: 'le', 'qua le', 'lê', 'qua r lê', 'pear' đều tìm ra 'Pear'.
    """
    norm_text = normalize_text(text)
    unacc_text = strip_accents(norm_text)
    found = []

    # Sắp xếp theo độ dài tên giảm dần để ưu tiên tên dài trước
    sorted_items = sorted(CLASS_INFO.items(), key=lambda x: len(x[1]["vn_name"]), reverse=True)

    for c_key, data in sorted_items:
        vn_name = data["vn_name"].lower()
        clean_vn = re.sub(r"^(quả|trái)\s+", "", vn_name)

        unacc_vn = strip_accents(vn_name)
        unacc_clean = strip_accents(clean_vn)
        en_name = c_key.lower()

        # 1. Tìm trên văn bản có dấu
        patterns_acc = [
            r"\b" + re.escape(vn_name) + r"\b",
            r"\b" + re.escape(clean_vn) + r"\b",
            r"\b" + re.escape(en_name) + r"\b"
        ]
        matched = False
        for pat in patterns_acc:
            m = re.search(pat, norm_text)
            if m:
                found.append((c_key, data["vn_name"], m.start(), m.end()))
                matched = True
                break

        # 2. Tìm trên văn bản không dấu nếu chưa match
        if not matched:
            patterns_unacc = [
                r"\b" + re.escape(unacc_vn) + r"\b",
                r"\b" + re.escape(unacc_clean) + r"\b"
            ]
            for pat in patterns_unacc:
                m = re.search(pat, unacc_text)
                if m:
                    found.append((c_key, data["vn_name"], m.start(), m.end()))
                    break

    return found

def generate_ai_chat_response(user_message, current_fruit_result=None):
    """
    Xử lý thông minh hội thoại người dùng:
    - Nếu người dùng nhắc đến tên quả (lê, táo, xoài... kể cả không dấu 'le', 'qua le') -> ĐỔI NGAY.
    - Trả lời ngắn gọn, trực diện, không dài dòng văn vở.
    """
    raw_msg = user_message.strip()
    norm_msg = normalize_text(raw_msg)
    unacc_msg = strip_accents(norm_msg)

    current_vn = current_fruit_result.get("best_vn_name", "") if current_fruit_result else ""
    current_class = current_fruit_result.get("best_class", "") if current_fruit_result else ""
    current_info = current_fruit_result.get("info", {}) if current_fruit_result else {}

    fruits_mentioned = find_fruits_in_text(raw_msg)
    target_fruit_key = None

    # 1. Nếu có nhắc đến quả trong câu
    if fruits_mentioned:
        # Trường hợp phủ định: "lê chứ không phải dừa", "không phải dừa, là lê", "lê chứ dừa gì"
        negation_match = re.search(r"(.+?)\s+(không phải|ko phai|chứ không phải|chứ ko phải|chứ)\s+(.+)", unacc_msg)
        if negation_match:
            pos_part = negation_match.group(1)
            neg_part = negation_match.group(3)
            pos_fruits = find_fruits_in_text(pos_part)
            if pos_fruits:
                target_fruit_key = pos_fruits[0][0]
            else:
                neg_fruits = find_fruits_in_text(neg_part)
                if neg_fruits and ("ma la" in neg_part or "la" in neg_part):
                    target_fruit_key = neg_fruits[0][0]

        # Trường hợp "không phải [B] mà là [A]"
        if not target_fruit_key:
            neg_first = re.search(r"(không phải|ko phai|chẳng phải)\s+(.+?)\s+(mà là|là|nó là|no la)\s+(.+)", unacc_msg)
            if neg_first:
                pos_fruits = find_fruits_in_text(neg_first.group(4))
                if pos_fruits:
                    target_fruit_key = pos_fruits[0][0]

        # Trường hợp người dùng nói quả khác với quả hiện tại
        if not target_fruit_key:
            for f_key, f_vn, _, _ in fruits_mentioned:
                if f_key != current_class:
                    target_fruit_key = f_key
                    break

        # Nếu vẫn chưa gán, lấy quả đầu tiên được tìm thấy
        if not target_fruit_key and fruits_mentioned:
            target_fruit_key = fruits_mentioned[0][0]

    # NẾU XÁC ĐỊNH ĐƯỢC QUẢ CẦN ĐỔI -> CẬP NHẬT NGAY LẬP TỨC
    if target_fruit_key:
        c_info = CLASS_INFO[target_fruit_key]
        return {
            "type": "correction",
            "message": f"✅ **Đã đổi kết quả nhận diện sang quả: {c_info['icon']} {c_info['vn_name']} ({target_fruit_key})**.",
            "updated_fruit": {
                "best_class": target_fruit_key,
                "best_vn_name": c_info["vn_name"],
                "icon": c_info["icon"],
                "confidence": 99.9,
                "info": c_info
            }
        }

    # 2. CHỈ TRẢ LỜI CÂU HỎI KHI NGƯỜI DÙNG THỰC SỰ HỎI
    f_name = current_vn if current_vn else "trái cây"

    if any(k in unacc_msg for k in ["calo", "beo", "map", "giam can", "nang luong", "kcal"]):
        cal = current_info.get("calories", "khoảng 50 kcal / 100g")
        return {
            "type": "chat",
            "message": f"⚡ Quả **{f_name}** chứa **{cal}**."
        }

    if any(k in unacc_msg for k in ["gia", "bao nhieu tien", "tien"]):
        price = current_info.get("avg_price_per_kg", 0)
        return {
            "type": "chat",
            "message": f"💰 Giá tham khảo của **{f_name}** là **{price:,} đ/kg**."
        }

    if any(k in unacc_msg for k in ["tieu duong", "duong huyet", "ngot"]):
        return {
            "type": "chat",
            "message": f"🩺 Người tiểu đường có thể ăn **{f_name}** với lượng vừa phải (100 - 150g/ngày)."
        }

    if any(k in unacc_msg for k in ["bao quan", "tu lanh", "de duoc bao lau"]):
        tips = current_info.get("tips", "Nên bảo quản ngăn mát.")
        return {
            "type": "chat",
            "message": f"❄️ Bảo quản **{f_name}** ở ngăn mát tủ lạnh 4°C - 8°C (giữ được 5 - 7 ngày). {tips}"
        }

    # 3. NẾU NGƯỜI DÙNG BẢO SAI MÀ CHƯA NÓI QUẢ GÌ
    if any(k in unacc_msg for k in ["sai", "nham", "khong dung", "bay", "tao lao", "nham roi"]):
        return {
            "type": "chat",
            "message": f"👉 Bạn hãy gõ tên quả chuẩn (ví dụ: *'lê'*, *'táo'*, *'xoài'*...) hoặc dùng ô chọn quả ở ngay phía trên để đổi ngay lập tức nhé."
        }

    # 4. MẶC ĐỊNH NGẮN GỌN (TUYỆT ĐỐI KHÔNG XỔ DINH DƯỠNG)
    return {
        "type": "chat",
        "message": f"Bạn muốn đổi sang quả nào? Hãy gõ tên quả (ví dụ: *'lê'*, *'cam'*, *'dưa hấu'*...) hoặc chọn ở danh sách phía trên để đổi ngay."
    }
