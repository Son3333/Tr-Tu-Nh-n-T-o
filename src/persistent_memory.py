# persistent_memory.py - Bo nho luu tru vinh vien du lieu Active Learning
import os
import json
import time
import hashlib
from PIL import Image
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
MEMORY_FILE = os.path.join(DATA_DIR, 'active_learning_memory.json')
DATASET_TRAIN_DIR = os.path.join(BASE_DIR, 'dataset', 'train')

def _ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
            json.dump({}, f, ensure_ascii=False, indent=2)

def compute_dhash(pil_img):
    try:
        small = pil_img.convert('L').resize((9, 8), Image.Resampling.LANCZOS)
        arr = np.array(small, dtype=np.int32)
        diff = arr[:, 1:] > arr[:, :-1]
        val = 0
        for b in diff.flatten():
            val = (val << 1) | int(b)
        return val
    except Exception:
        return 0

def hamming_distance(h1, h2):
    x = h1 ^ h2
    dist = 0
    while x > 0:
        dist += x & 1
        x >>= 1
    return dist

def compute_image_fingerprint(pil_img):
    dhash = compute_dhash(pil_img)
    # Thumbnail 64x64
    small_rgb = pil_img.convert('RGB').resize((64, 64))
    small_bytes = small_rgb.tobytes()
    md5_hash = hashlib.md5(small_bytes).hexdigest()
    # Average color
    arr = np.array(small_rgb, dtype=np.float32)
    avg_r = float(np.mean(arr[:, :, 0]))
    avg_g = float(np.mean(arr[:, :, 1]))
    avg_b = float(np.mean(arr[:, :, 2]))
    return dhash, md5_hash, (avg_r, avg_g, avg_b)

def load_memory():
    _ensure_data_dir()
    try:
        with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}

def save_memory_entry(pil_img, fruit_class, user_note=''):
    """
    Lưu vĩnh viễn quả vào bộ nhớ JSON và lưu file ảnh vào dataset
    """
    _ensure_data_dir()
    dhash, md5_hash, avg_color = compute_image_fingerprint(pil_img)
    memory = load_memory()

    entry_id = md5_hash
    timestamp_str = time.strftime('%Y-%m-%d %H:%M:%S')

    memory[entry_id] = {
        'fruit_class': fruit_class,
        'dhash': dhash,
        'md5': md5_hash,
        'avg_color': avg_color,
        'user_note': user_note,
        'learned_at': timestamp_str
    }

    with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)

    # Lưu ảnh vào dataset train để sẵn sàng huấn luyện
    fruit_dir = os.path.join(DATASET_TRAIN_DIR, fruit_class)
    os.makedirs(fruit_dir, exist_ok=True)
    save_path = os.path.join(fruit_dir, f'learned_{int(time.time())}_{md5_hash[:6]}.jpg')
    try:
        pil_img.convert('RGB').save(save_path, 'JPEG', quality=95)
    except Exception:
        pass

    return True

def lookup_memory(pil_img):
    """
    Tra cứu trong bộ nhớ vĩnh viễn. Khớp chính xác hoặc tương đồng cao (Hamming dist <= 8)
    """
    memory = load_memory()
    if not memory:
        return None

    dhash, md5_hash, avg_color = compute_image_fingerprint(pil_img)

    # 1. Khớp mã MD5 ảnh thu nhỏ
    if md5_hash in memory:
        return memory[md5_hash]

    # 2. Khớp theo vân tay cảm nhận dHash (cho phép sai số nén JPEG lên đến 8 bit)
    best_match = None
    min_dist = 999
    for entry_id, item in memory.items():
        stored_dhash = item.get('dhash', 0)
        dist = hamming_distance(dhash, stored_dhash)
        stored_color = item.get('avg_color', [0, 0, 0])
        color_diff = np.mean(np.abs(np.array(avg_color) - np.array(stored_color)))
        if dist <= 3 and color_diff < 25 and dist < min_dist:
            min_dist = dist
            best_match = item

    return best_match