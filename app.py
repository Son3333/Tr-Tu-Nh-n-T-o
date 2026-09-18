"""
app.py - Ứng dụng Giao diện Web Nhận diện và Phân loại 100 Loại Trái Cây
Đề tài số 22 - Môn học: Trí tuệ nhân tạo (AI)
Công nghệ: PyTorch, MobileNetV2 (100 Classes), Streamlit, OpenCV
"""

import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = CURRENT_DIR
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

import streamlit as st
from PIL import Image
import numpy as np

from src.config import CLASS_NAMES, CLASS_INFO, REPORTS_DIR, MODELS_DIR, DATASET_DIR
from src.predict import predict_fruit

# Cấu hình trang Streamlit
st.set_page_config(
    page_title="Hệ thống Nhận diện 100 Loại Trái Cây - Đề tài 22",
    page_icon="🍎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Tùy biến CSS chuyên nghiệp, tinh giản
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1b4332;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #2d6a4f;
        text-align: center;
        margin-bottom: 25px;
    }
    .result-card {
        background: linear-gradient(135deg, #e8f5e9, #c8e6c9);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.06);
        border: 2px solid #81c784;
        margin-bottom: 20px;
    }
    .fruit-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1b5e20;
        margin-bottom: 10px;
    }
    .metric-badge {
        display: inline-block;
        background-color: #2e7d32;
        color: white;
        padding: 6px 14px;
        border-radius: 25px;
        font-size: 1rem;
        font-weight: 600;
        margin-right: 10px;
    }
    .price-badge {
        display: inline-block;
        background-color: #f57f17;
        color: white;
        padding: 6px 14px;
        border-radius: 25px;
        font-size: 1rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Tiêu đề ứng dụng
st.markdown("<div class='main-header'>🍎 CHƯƠNG TRÌNH NHẬN DIỆN & PHÂN LOẠI 600 LOẠI TRÁI CÂY 🍌</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Đề tài số 22 | Môn học: Trí tuệ nhân tạo (AI) | Thư viện: 600 Loại Trái Cây Việt Nam & Thế Giới | Mô hình: YOLOv8 AI</div>", unsafe_allow_html=True)

# Thanh điều hướng bên trái (Sidebar)
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1610832958506-aa56368176cf?w=400&q=80", use_container_width=True)
    st.markdown("### ℹ️ Thông tin đề tài")
    st.markdown(f"""
    * **Môn học**: Trí tuệ nhân tạo (AI)
    * **Đề tài**: Nhận diện & phân loại hình ảnh trái cây
    * **Kiến trúc AI**: **YOLOv8** Vision Classifier
    * **Quy mô**: **{len(CLASS_NAMES)} loại trái cây (Việt Nam & Toàn Cầu)**
    * **Trường phái**: Học có giám sát (Supervised) & Tự học (Active Learning)
    """)
    st.divider()
    
    # Cho 100 loại quả vào thư viện thu gọn, không chiếm diện tích màn hình
    with st.expander(f"📚 Thư viện {len(CLASS_NAMES)} loại quả (Bấm để xem)", expanded=False):
        search_fruit = st.text_input("🔍 Tìm nhanh quả trong thư viện:", placeholder="Nhập tên quả...")
        filtered_fruits = [c for c in CLASS_NAMES if search_fruit.lower() in CLASS_INFO[c]['vn_name'].lower() or search_fruit.lower() in c.lower()]
        
        st.caption(f"Tìm thấy {len(filtered_fruits)} / {len(CLASS_NAMES)} loại:")
        for c in filtered_fruits[:30]:
            f_item = CLASS_INFO[c]
            st.write(f"{f_item['icon']} **{f_item['vn_name']}** ({c})")
        if len(filtered_fruits) > 30:
            st.caption("...và nhiều loại quả khác.")
    
    st.divider()
    st.caption("🎯 Chế độ quét: Quét trúng quả nào chỉ hiển thị duy nhất quả đó!")

# Hàm hiển thị: Quét ra quả nào thì hiện DUY NHẤT quả đấy
from src.persistent_memory import save_memory_entry
from src.colab_sync import (
    get_dataset_stats,
    save_learned_sample,
    create_colab_training_package,
    check_yolo_model_status,
    ZIP_PACKAGE_PATH
)

# Hàm hiển thị kết quả nhận diện & tích hợp Active Learning
def render_detected_fruit_only(result, source_img=None, key_prefix="tab"):
    status = result.get("status", "success")

    # 1. TRƯỜNG HỢP PHÁT HIỆN MẶT NGƯỜI / CHÂN DUNG
    if status == "face_detected":
        st.error(f"👤 **CẢNH BÁO: PHÁT HIỆN CON NGƯỜI / KHUÔN MẶT**\n\n{result.get('message')}")
        st.info("💡 **Hệ thống từ chối phân loại:** AI đã được trang bị cơ chế bảo vệ kép (YuNet Face Detector & YOLOv8 Person Filter) để chặn triệt để việc nhầm lẫn khuôn mặt người với hoa quả. Hãy hướng camera vào quả trái cây bạn nhé!")
        return

    # 2. TRƯỜNG HỢP ĐỘ TIN CẬY QUÁ THẤP (OOD)
    if status == "low_confidence":
        st.warning(f"⚠️ **ĐỘ TIN CẬY THẤP:**\n\n{result.get('message')}")
        st.info("💡 Bức ảnh không giống rõ nét loại quả nào trong thư viện 100 loại quả. Bạn có thể kéo xuống dưới để dạy AI ghi nhớ loại quả này.")

    best_name = result.get("best_vn_name", "Không xác định")
    best_class = result.get("best_class", "Unknown")
    icon = result.get("icon", "🍏")
    conf = result.get("confidence", 0.0)
    info = result.get("info", {})
    model_source = result.get("model_source", "YOLOv8")

    is_learned = result.get("is_learned", False)
    learned_badge = "<span style='background-color:#6a1b9a; color:white; padding:4px 10px; border-radius:15px; font-size:0.85rem; font-weight:bold; margin-left:10px;'>🧠 ĐÃ GHI NHỚ VĨNH VIỄN (ACTIVE LEARNING)</span>" if is_learned else ""

    st.markdown(f"""
    <div class='result-card'>
        <div class='fruit-title'>{icon} {best_name} <span style='font-size: 1.4rem; color: #388e3c; font-weight: 500;'>({best_class})</span>{learned_badge}</div>
        <div style='margin-bottom: 16px;'>
            <span class='metric-badge'>🎯 Độ tin cậy AI: {conf:.2f}%</span>
            <span class='price-badge'>💰 Giá tham khảo: {info.get('avg_price_per_kg', 50000):,} VNĐ/kg</span>
            <span style='background:#0284c7; color:white; padding:6px 12px; border-radius:25px; font-size:0.9rem; font-weight:600;'>⚙️ {model_source}</span>
        </div>
        <hr style='border: 1px solid #a5d6a7; margin: 15px 0;'>
        <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 15px;'>
            <div>
                <p><strong>⚡ Lượng Calo:</strong> {info.get('calories', 'Đang cập nhật')}</p>
                <p><strong>💊 Vitamin & Khoáng chất:</strong> {info.get('vitamins', 'Đang cập nhật')}</p>
            </div>
            <div>
                <p><strong>❤️ Lợi ích sức khỏe:</strong> {info.get('benefits', 'Tốt cho sức khỏe')}</p>
                <p><strong>💡 Mẹo chọn quả tươi ngon:</strong> {info.get('tips', 'Chọn quả tươi ngon')}</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Hiển thị thanh đo độ tin cậy
    st.progress(min(1.0, max(0.0, conf / 100.0)))

    # Tùy chọn xem chi tiết phân phối xác suất
    if "top_predictions" in result:
        with st.expander("🔍 Chi tiết phân phối xác suất (Dành cho kiểm tra mô hình)", expanded=False):
            for item in result["top_predictions"]:
                p = item["probability"]
                st.write(f"{item['icon']} **{item['vn_name']}** ({item['class_name']}): `{p:.2f}%`")
                st.progress(min(1.0, max(0.0, p / 100.0)))

    # KHU VỰC ACTIVE LEARNING: DẠY AI GHI NHỚ KHI ĐOÁN SAI
    with st.expander("💡 Kết quả chưa chính xác? Hãy dạy AI ghi nhớ ngay (Active Learning)", expanded=False):
        st.write("Nếu đây là quả của bạn nhưng AI đoán chưa đúng (ví dụ quả Lê bị nhầm sang quả khác), hãy chọn đúng tên quả để AI lưu vĩnh viễn:")
        
        target_img = result.get("cropped_image", source_img)
        fruit_options = [f"{CLASS_INFO[c]['icon']} {CLASS_INFO[c]['vn_name']} ({c})" for c in CLASS_NAMES]
        
        # Mặc định gợi ý quả Lê nếu người dùng hay gặp
        default_idx = 0
        if "Pear" in CLASS_NAMES:
            default_idx = CLASS_NAMES.index("Pear")

        col_l1, col_l2 = st.columns([3, 1])
        with col_l1:
            corrected_choice = st.selectbox(
                "Chọn loại quả chính xác:", 
                options=fruit_options, 
                index=default_idx,
                key=f"{key_prefix}_correct_select"
            )
        with col_l2:
            st.write("")
            st.write("")
            if st.button("💾 Dạy AI nhớ ngay", key=f"{key_prefix}_learn_btn"):
                c_class = corrected_choice.split("(")[-1].replace(")", "").strip()
                if target_img is not None:
                    # 1. Tự học: Lưu ảnh vào tập train để sẵn sàng huấn luyện lại bằng YOLOv8
                    save_learned_sample(target_img, c_class, note="Người dùng hiệu chỉnh qua Web App")
                    # 2. Lưu vào bộ nhớ vân tay vĩnh viễn (Active Learning Memory)
                    save_memory_entry(target_img, c_class, user_note="Người dùng hiệu chỉnh qua Web App")
                    c_vn = CLASS_INFO[c_class]["vn_name"]
                    st.success(f"🎉 Đã lưu vĩnh viễn! AI đã nạp ảnh này vào tập dữ liệu huấn luyện quả **{c_vn}** ({c_class})!")
                    st.rerun()

# 5 Tab chức năng
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📸 Nhận diện từ Ảnh", 
    "📹 Quét qua Camera", 
    "🛒 Quầy tính tiền (100 loại quả)", 
    "🚀 Tự học & Huấn luyện Colab (YOLOv8)",
    "🎓 Lý thuyết Giáo trình & Báo cáo AI"
])

# ----------------------------------------------------
# TAB 1: NHẬN DIỆN QUA ẢNH TẢI LÊN
# ----------------------------------------------------
with tab1:
    st.markdown("### 📤 Tải ảnh trái cây để nhận diện")
    uploaded_file = st.file_uploader(
        "Kéo thả hoặc bấm chọn ảnh quả cần nhận diện (JPG, PNG, JPEG):", 
        type=["jpg", "png", "jpeg"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        c1, c2 = st.columns([1, 1])
        with c1:
            st.image(image, caption="Ảnh quả bạn đã tải lên", use_container_width=True)
        with c2:
            with st.spinner("🧠 AI đang phân tích và nhận diện..."):
                result = predict_fruit(image)
                render_detected_fruit_only(result, source_img=image, key_prefix="upload")
    else:
        st.info("💡 Hướng dẫn: Chọn ảnh bất kỳ trong 100 loại quả, hệ thống sẽ tự động quét và chỉ hiển thị thông tin quả đó!")

# ----------------------------------------------------
# TAB 2: QUÉT TRỰC TIẾP QUA CAMERA
# ----------------------------------------------------
with tab2:
    st.markdown("### 📷 Quét trực tiếp qua Camera / Webcam")
    st.write("Đưa trái cây trước ống kính máy tính và bấm nút chụp để nhận diện ngay lập tức:")
    camera_photo = st.camera_input("Chụp ảnh từ camera máy tính")

    if camera_photo is not None:
        cam_image = Image.open(camera_photo)
        c1, c2 = st.columns([1, 1])
        with c1:
            st.image(cam_image, caption="Ảnh vừa chụp từ Camera", use_container_width=True)
        with c2:
            with st.spinner("🧠 AI đang trích xuất đặc trưng..."):
                res_cam = predict_fruit(cam_image)
                render_detected_fruit_only(res_cam, source_img=cam_image, key_prefix="cam")

# ----------------------------------------------------
# TAB 3: QUẦY THU NGÂN TÍNH TIỀN THÔNG MINH
# ----------------------------------------------------
with tab3:
    st.markdown(f"### 🛒 Quầy thu ngân thông minh ({len(CLASS_NAMES)} loại trái cây)")
    st.write("Tra cứu đơn giá và tính tiền tự động theo trọng lượng:")

    col_select, col_calc = st.columns([1, 1])
    with col_select:
        fruit_options = [f"{CLASS_INFO[c]['icon']} {CLASS_INFO[c]['vn_name']} ({c})" for c in CLASS_NAMES]
        selected_option = st.selectbox("Chọn loại trái cây trong thư viện:", options=fruit_options)
        
        # Trích xuất class name
        raw_name = selected_option.split("(")[-1].replace(")", "").strip()
        f_info = CLASS_INFO[raw_name]

        weight_kg = st.number_input("Khối lượng cân được (kg):", min_value=0.1, max_value=100.0, value=1.0, step=0.1)

    with col_calc:
        unit_price = f_info["avg_price_per_kg"]
        total_price = int(unit_price * weight_kg)

        st.markdown(f"""
        <div class='result-card'>
            <h3>{f_info['icon']} Hóa đơn tạm tính</h3>
            <p><strong>Tên mặt hàng:</strong> {f_info['vn_name']} ({raw_name})</p>
            <p><strong>Đơn giá niêm yết:</strong> {unit_price:,} VNĐ / kg</p>
            <p><strong>Khối lượng:</strong> {weight_kg:.2f} kg</p>
            <hr style='border: 1px solid #81c784;'>
            <h2 style='color:#1b5e20;'>TỔNG TIỀN: {total_price:,} VNĐ</h2>
        </div>
        """, unsafe_allow_html=True)
        st.button("🖨️ Xuất hóa đơn bán lẻ (Mô phỏng)")

# ----------------------------------------------------
# TAB 4: TỰ HỌC & HUẤN LUYỆN YOLOV8 TRÊN GOOGLE COLAB
# ----------------------------------------------------
with tab4:
    st.markdown("### 🚀 Tự học & Huấn luyện Siêu tốc trên Google Colab (YOLOv8)")
    st.write("Hệ thống tự động tích lũy các bức ảnh mới bạn tải lên hoặc chỉnh sửa. Khi cần, bạn có thể đóng gói dữ liệu và chạy huấn luyện trên Colab chỉ trong 3 phút!")

    col_s1, col_s2, col_s3 = st.columns(3)
    stats = get_dataset_stats()
    with col_s1:
        st.metric("Tổng số lớp trái cây", f"{stats['total_classes']} loại")
    with col_s2:
        st.metric("Tổng số ảnh huấn luyện", f"{stats['total_train_images']} ảnh")
    with col_s3:
        st.metric("Ảnh tự học mới tích lũy", f"+{stats['newly_learned_count']} ảnh", delta=f"{stats['newly_learned_count']} ảnh mới")

    st.divider()

    # Trạng thái mô hình YOLOv8
    has_model, model_file, size_mb, mtime = check_yolo_model_status()
    if has_model:
        st.success(f"✅ **ĐANG SỬ DỤNG MÔ HÌNH YOLOV8 ĐÃ HUẤN LUYỆN:** `{os.path.basename(model_file)}` ({size_mb:.2f} MB - Cập nhật: {mtime})")
    else:
        st.info("ℹ️ **ĐANG DÙNG MÔ HÌNH YOLOV8 BASELINE:** Bạn có thể bấm nút huấn luyện ngay bên dưới hoặc chạy Colab!")

    col_tr1, col_tr2 = st.columns([2, 1])
    with col_tr1:
        st.write(f"💡 Huấn luyện cập nhật lại toàn bộ **{len(CLASS_NAMES)}** phân lớp trái cây trực tiếp trên máy tính chỉ trong 2-3 giây:")
    with col_tr2:
        if st.button("⚡ Huấn luyện lại ngay (1-Click)", use_container_width=True):
            with st.spinner(f"Đang đồng bộ và huấn luyện toàn bộ {len(CLASS_NAMES)} loại quả..."):
                from src.train_600_engine import train_600_fruit_model
                train_600_fruit_model()
                st.success("🎉 Đã huấn luyện xong toàn bộ các phân lớp thành công!")
                st.rerun()

    yolo_chart_path = os.path.join(REPORTS_DIR, "yolo_results.png")
    training_chart_path = os.path.join(REPORTS_DIR, "training_history.png")
    if os.path.exists(yolo_chart_path):
        st.image(yolo_chart_path, caption="📊 Biểu đồ Huấn luyện Trực tiếp Mô hình Học sâu YOLOv8 (Loss & Top-1 / Top-5 Accuracy)", use_container_width=True)
    elif os.path.exists(training_chart_path):
        st.image(training_chart_path, caption="📊 Biểu đồ Hàm mất mát (Loss) và Độ chính xác (Accuracy) của Mô hình đã Huấn luyện", use_container_width=True)

    st.markdown("---")
    st.markdown("#### 📦 Bước 1: Đóng gói tập dữ liệu để huấn luyện Colab")
    col_pack1, col_pack2 = st.columns([2, 1])
    with col_pack1:
        st.write("Bấm nút bên cạnh để tự động đóng gói toàn bộ kho dữ liệu trái cây (bao gồm cả các ảnh bạn vừa dạy AI) thành file `fruit_dataset_yolo.zip` chuẩn cấu trúc YOLOv8:")
    with col_pack2:
        if st.button("📦 Đóng gói Dataset (.zip)", use_container_width=True):
            with st.spinner("Đang nén dữ liệu..."):
                ok, msg = create_colab_training_package()
                if ok:
                    st.success(f"🎉 {msg}")
                else:
                    st.error(msg)

    if os.path.exists(ZIP_PACKAGE_PATH):
        with open(ZIP_PACKAGE_PATH, "rb") as f:
            st.download_button(
                label="⬇️ Tải file 'fruit_dataset_yolo.zip' về máy",
                data=f,
                file_name="fruit_dataset_yolo.zip",
                mime="application/zip",
                use_container_width=True
            )

    st.markdown("---")
    st.markdown("#### ⚡ Bước 2: Huấn luyện trên Google Colab với GPU T4 miễn phí")
    st.markdown("""
    1. Mở trang **[Google Colab](https://colab.research.google.com/)** -> Bấm **Tải lên sổ tay (Upload notebook)** -> Chọn file `YOLOv8_Fruit_Training_Colab.ipynb` có sẵn trong thư mục dự án này.
    2. Chọn menu **Thời gian chạy (Runtime)** -> **Thay đổi loại thời gian chạy (Change runtime type)** -> Chọn **T4 GPU** -> Bấm **Lưu (Save)**.
    3. Tải file `fruit_dataset_yolo.zip` lên thanh tệp bên trái Colab và bấm **Chạy tất cả (Run all)**.
    4. Quá trình huấn luyện chỉ mất **2 - 4 phút**. Sau khi xong, Colab sẽ tự động tải file `best.pt` về máy cho bạn.
    """)

    st.markdown("---")
    st.markdown("#### 📥 Bước 3: Nạp mô hình vừa huấn luyện vào ứng dụng")
    uploaded_model = st.file_uploader("Kéo thả file 'best.onnx' (Khuyên dùng) hoặc 'best.pt' vừa tải từ Colab vào đây để kích hoạt ngay:", type=["onnx", "pt"])
    if uploaded_model is not None:
        fname = uploaded_model.name.lower()
        if fname.endswith(".onnx"):
            save_dest = os.path.join(MODELS_DIR, "best.onnx")
            with open(save_dest, "wb") as f:
                f.write(uploaded_model.getbuffer())
            save_cls = os.path.join(MODELS_DIR, "yolov8_fruit_cls.onnx")
            with open(save_cls, "wb") as f:
                f.write(uploaded_model.getbuffer())
            st.success("🎉 Nạp mô hình ONNX thành công! Mô hình đã được nạp trực tiếp vào bộ suy luận OpenCV DNN siêu tốc!")
        else:
            save_dest = os.path.join(MODELS_DIR, "best.pt")
            with open(save_dest, "wb") as f:
                f.write(uploaded_model.getbuffer())
            save_cls = os.path.join(MODELS_DIR, "yolov8_fruit_cls.pt")
            with open(save_cls, "wb") as f:
                f.write(uploaded_model.getbuffer())
            st.success("🎉 Nạp mô hình PyTorch (.pt) thành công! Ứng dụng đã tự động lưu trữ mô hình mới!")
        st.rerun()

# ----------------------------------------------------
# TAB 5: LÝ THUYẾT GIÁO TRÌNH AI & PHÂN TÍCH MÔ HÌNH
# ----------------------------------------------------
with tab5:
    st.markdown("### 🎓 Cơ sở Lý thuyết Giáo trình Trí tuệ Nhân tạo & Đánh giá Mô hình")

    html_report_path = os.path.join(PROJECT_ROOT, "Bao_Cao_Ly_Thuyet_AI_De_Tai_22.html")
    if os.path.exists(html_report_path):
        with open(html_report_path, "r", encoding="utf-8") as f:
            html_data = f.read()
        col_rep1, col_rep2 = st.columns([3, 1])
        with col_rep1:
            st.info("📄 **Báo cáo Lý thuyết & Kiến trúc Hệ thống chuẩn học thuật:** Bản chất bài toán, Mô hình sử dụng, Trường phái có giám sát, Độ phức tạp không gian/thời gian, I/O và Luồng 7 bước.")
        with col_rep2:
            st.download_button(
                label="⬇️ Tải Báo Cáo (.HTML)",
                data=html_data,
                file_name="Bao_Cao_Ly_Thuyet_AI_De_Tai_22.html",
                mime="text/html",
                use_container_width=True
            )

    with st.expander("📚 1. BẢN CHẤT BÀI TOÁN TRONG GIÁO TRÌNH AI: ĐÂY LÀ DẠNG HỌC GÌ?", expanded=True):
        st.markdown("""
        Trong giáo trình chuẩn môn **Trí tuệ nhân tạo (AI)**, các thuật toán học máy được chia làm 3 trường phái chính:
        """)
        c_theo1, c_theo2, c_theo3 = st.columns(3)
        with c_theo1:
            st.success("""
            **1. HỌC CÓ GIÁM SÁT (Supervised Learning)**  
            👉 **CHÍNH LÀ ĐỀ TÀI NÀY!**  
            * **Dữ liệu:** Mỗi bức ảnh $X$ đều có nhãn tên quả $y$ (Cặp dữ liệu $X, y$).
            * **Nhiệm vụ:** Tìm hàm ánh xạ $f: X \\rightarrow y$ để khi gặp ảnh mới, mô hình dự đoán chính xác tên quả.
            * **Kỹ thuật:** Deep Convolutional Neural Network (MobileNetV2).
            """)
        with c_theo2:
            st.info("""
            **2. HỌC KHÔNG GIÁM SÁT ("Tự học" - Unsupervised)**  
            * **Dữ liệu:** Chỉ có ảnh, **KHÔNG có nhãn** tên quả.
            * **Nhiệm vụ:** Tự tìm sự tương đồng để gom cụm (K-Means, PCA).
            * *Hạn chế:* Máy chỉ biết gom nhóm A và nhóm B, chứ không biết quả nào là Táo, Cam hay Chuối.
            """)
        with c_theo3:
            st.warning("""
            **3. HỌC TĂNG CƯỜNG (Reinforcement Learning)**  
            * **Cơ chế:** Tác nhân (Agent) nhận thưởng (Reward) hoặc phạt (Penalty) khi hành động trong môi trường (xe tự hành, chơi game cờ vây).
            """)

    with st.expander("🔬 2. CÁC CÔNG THỨC TOÁN HỌC CỐT LÕI CỦA MẠNG HỌC SÂU (DEEP LEARNING)", expanded=False):
        st.markdown(r"""
        * **Phép tích chập (2D Convolution):**  
          $$S(i, j) = (I * K)(i, j) = \sum_{m} \sum_{n} I(i - m, j - n) K(m, n)$$
        * **Hàm kích hoạt phi tuyến tính ReLU:**  
          $$f(x) = \max(0, x)$$
        * **Hàm phân phối xác suất Softmax:**  
          $$P(y = c \mid x) = \frac{e^{z_c}}{\sum_{j=1}^{C} e^{z_j}} \quad (C = 100 \text{ loại quả})$$
        * **Hàm mất mát Cross-Entropy Loss:**  
          $$\mathcal{L}_{CE} = -\sum_{c=1}^{C} y_c \log(\hat{y}_c)$$
        * **Thuật toán tối ưu hóa lan truyền ngược (Adam Optimizer):**  
          $$\theta_{t+1} = \theta_t - \frac{\alpha}{\sqrt{\hat{v}_t} + \epsilon} \hat{m}_t$$
        """)

    st.markdown("---")
    st.markdown("### 📊 Biểu đồ Thực nghiệm Huấn luyện & Ma trận Nhầm lẫn")
    col_rpt1, col_rpt2 = st.columns(2)
    history_img_path = os.path.join(REPORTS_DIR, "training_history.png")
    cm_img_path = os.path.join(REPORTS_DIR, "confusion_matrix.png")

    with col_rpt1:
        st.markdown(f"#### 1. Biểu đồ Accuracy & Loss ({len(CLASS_NAMES)} loại quả)")
        if os.path.exists(history_img_path):
            st.image(history_img_path, use_container_width=True)
    with col_rpt2:
        st.markdown("#### 2. Ma trận nhầm lẫn đại diện (Confusion Matrix)")
        if os.path.exists(cm_img_path):
            st.image(cm_img_path, use_container_width=True)

    st.markdown("---")
    st.markdown("#### ⚙️ Bảng tổng hợp tham số Học sâu:")
    st.markdown(f"""
| Thành phần Giáo trình AI | Cơ chế áp dụng trong bài |
| :--- | :--- |
| **Trường phái học máy** | Học có giám sát (Supervised Learning) |
| **Kiến trúc mạng nơ-ron** | Deep CNN & YOLOv8 phân loại {len(CLASS_NAMES)} lớp |
| **Kỹ thuật tối ưu hóa** | AdamW Optimizer (lr=0.0003, Cosine Annealing) |
| **Hàm mục tiêu (Loss)** | Cross-Entropy Loss đa lớp |
| **Hàm phi tuyến & Xác suất** | ReLU / SiLU tại ẩn & Softmax tại ngõ ra |
| **Chiến lược chống Overfitting** | Dropout (0.3), Data Augmentation, Batch Normalization |
""")

