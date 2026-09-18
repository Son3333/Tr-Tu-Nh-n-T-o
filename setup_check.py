"""
setup_check.py - Tự động phát hiện và cài đặt thư viện thiếu khi gửi cho người khác test
Môn học: Trí tuệ nhân tạo (AI) - Đề tài số 22
"""

import sys
import subprocess
import os

REQUIRED_PACKAGES = {
    "streamlit": "streamlit>=1.30.0",
    "cv2": "opencv-python>=4.8.0",
    "PIL": "pillow>=10.0.0",
    "numpy": "numpy>=1.24.0",
    "matplotlib": "matplotlib>=3.7.0"
}

def check_and_install_packages():
    missing = []
    for mod_name, pip_spec in REQUIRED_PACKAGES.items():
        try:
            __import__(mod_name)
        except Exception:
            missing.append(pip_spec)

    if missing:
        print("================================================================")
        print("  Dang tu dong cai dat cac goi con thieu: " + ", ".join(missing))
        print("================================================================")
        cmd = [sys.executable, "-m", "pip", "install"] + missing
        try:
            subprocess.run(cmd)
        except Exception:
            pass
    else:
        print("[OK] Toan bo thu vien co ban da san sang!")

def verify_models():
    # 1. Kiem tra model
    model_path = os.path.join("models", "best_fruit_model.pth")
    if not os.path.exists(model_path):
        print("[*] Dang khoi tao mo hinh mau 100 loai qua...")
        from src.init_demo_model import main as init_model
        init_model()

    # 2. Kiem tra Metric Database
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)
    pt_path = os.path.join(data_dir, "metric_database.pt")
    if not os.path.exists(pt_path):
        print("[*] Dang khoi tao Co so du lieu Vector Metric Learning...")
        from src.metric_learner import MetricDatabase
        MetricDatabase.get_instance()

if __name__ == "__main__":
    check_and_install_packages()
    verify_models()
    print("[SAN SANG] He thong da san sang khoi dong!")

