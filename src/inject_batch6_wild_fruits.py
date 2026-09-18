"""
inject_batch6_wild_fruits.py - Tích hợp và Huấn luyện 100 Loại Trái cây Rừng, Bản địa & Thử nghiệm Việt Nam (501 - 600)
Đề tài số 22: Hệ thống AI Nhận diện & Phân loại Trái cây Thông minh
Bao quát 100 loại quả hoang dã, đặc sản núi rừng Tây Bắc, Tây Nguyên, miền Trung, miền Tây và Đà Lạt.
"""

import os
import sys
import json

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.fruit_library_600 import FRUIT_LIBRARY_600

WILD_100_BATCH6 = {
    "ThanhTraHue": ("Trái thanh trà Huế", "🍈", "36 kcal / 100g", "Đặc sản cố đô Thủy Biều vị thanh tao mát lành"),
    "ThanhTraMienTay": ("Trái thanh trà miền Tây", "🟡", "42 kcal / 100g", "Quả tròn vàng mọng vị chua ngọt làm mứt và giải khát"),
    "TraiBuaRung": ("Trái bứa rừng", "🟢", "38 kcal / 100g", "Vị chua thanh mát chuyên nấu canh chua vùng cao"),
    "TraiBuaDo": ("Trái bứa đỏ", "🔴", "40 kcal / 100g", "Vỏ đỏ thắm mọng nước giàu axit hữu cơ tự nhiên"),
    "TraiBuaXanh": ("Trái bứa xanh", "🟢", "35 kcal / 100g", "Chua thanh dịu nhẹ giảm béo kích thích tiêu hóa"),
    "DauRungTayBac": ("Trái dâu rừng Tây Bắc", "🍓", "34 kcal / 100g", "Dâu rừng mọc hoang dã đỏ thắm vị chua ngọt đậm đà"),
    "MamXoiRung": ("Trái mâm xôi rừng", "🍇", "52 kcal / 100g", "Quả chùm mọng đỏ tím giàu chất chống oxy hóa cao"),
    "PhucBonTuDaLat": ("Trái phúc bồn tử Đà Lạt", "🔴", "54 kcal / 100g", "Đặc sản Đà Lạt vị chua ngọt làm rượu vang và sinh tố"),
    "VietQuatDaLat": ("Trái việt quất trồng Đà Lạt", "🫐", "57 kcal / 100g", "Việt quất ôn đới di thực Đà Lạt giàu anthocyanin sáng mắt"),
    "NamVietQuatVN": ("Trái nam việt quất (cranberry thử nghiệm)", "🔴", "46 kcal / 100g", "Trái đỏ mọng vị chua chát giải nhiệt ngừa viêm"),
    "KiwiVangLamDong": ("Trái kiwi vàng trồng thử Lâm Đồng", "🥝", "60 kcal / 100g", "Thịt vàng ươm ngọt lịm hàm lượng vitamin C vượt trội"),
    "KiwiXanhDaLat": ("Trái kiwi xanh Đà Lạt", "🥝", "61 kcal / 100g", "Vị chua ngọt thanh khiết hạt nhỏ giòn tan"),
    "DuaPepinoDaLat": ("Trái dưa pepino Đà Lạt", "🍈", "28 kcal / 100g", "Dưa hấu Nam Mỹ trồng Đà Lạt ngọt mát thơm hương dưa lê"),
    "TraiCaNa": ("Trái cà na", "🟢", "45 kcal / 100g", "Cà na đập dập chấm muối ớt chua chát giòn ngon"),
    "CaNaThai": ("Trái cà na Thái", "🟢", "48 kcal / 100g", "Quả to cùi dày ngâm chua ngọt giòn rụm"),
    "ChumRuotVN": ("Trái chùm ruột", "🟡", "30 kcal / 100g", "Quả khía cạnh mọng nước chấm muối ớt làm mứt chùm ruột"),
    "ChumRuotRung": ("Trái chùm ruột rừng", "🟡", "32 kcal / 100g", "Chùm ruột mọc hoang dã quả chua thanh giàu vitamin C"),
    "TramMocVN": ("Trái trâm (trâm mốc)", "🟣", "50 kcal / 100g", "Quả màu tím đen cùi chua ngọt chát gợi nhớ tuổi thơ"),
    "TramRung": ("Trái trâm rừng", "🟣", "52 kcal / 100g", "Trâm rừng mọc hoang quả mọng tím sẫm vị đậm đà"),
    "TraiTrungCaVN": ("Trái trứng cá", "🔴", "42 kcal / 100g", "Quả nhỏ đỏ mọng ngọt lịm gắn liền với tuổi học trò"),
    "TrungCaBien": ("Trái trứng cá biển", "🔴", "40 kcal / 100g", "Cây ven biển quả mọng ngọt mát thanh nhiệt"),
    "DuaXiemBenTreVN": ("Trái dừa xiêm Bến Tre", "🥥", "354 kcal / 100g cơm", "Nước ngọt lịm mát lành đặc sản xứ dừa Bến Tre"),
    "DuaDuaVN": ("Trái dừa dứa", "🥥", "350 kcal / 100g cơm", "Nước ngọt ngào thơm nồng nàn mùi lá dứa tự nhiên"),
    "DuaSapTraVinhVN": ("Trái dừa sáp Trà Vinh", "🥥", "400 kcal / 100g cơm", "Cơm dừa dày đặc dẻo quánh béo ngậy độc nhất vô nhị"),
    "CauNon": ("Trái cau non", "🟢", "120 kcal / 100g", "Quả cau non xanh vỏ ruột mềm ngâm mật ong"),
    "CauGia": ("Trái cau già", "🟤", "150 kcal / 100g", "Hạt cứng dùng ăn trầu truyền thống lễ cưới hỏi"),
    "CauTuoiMienBac": ("Trái cau tươi miền Bắc", "🟢", "130 kcal / 100g", "Đặc sản cau Hải Phòng tươi xanh đượm phong tục"),
    "CauRung": ("Trái cau rừng", "🟢", "125 kcal / 100g", "Cau rừng quả dài hoang dã hạt chắc dược liệu"),
    "ThotNotAnGiangVN": ("Trái thốt nốt An Giang", "🟤", "85 kcal / 100g", "Múi trong suốt mềm dẻo nước thốt nốt ngọt thanh mát"),
    "MeRungTayNguyen": ("Trái me rừng Tây Nguyên", "🟢", "44 kcal / 100g", "Vị chua chát ban đầu ngọt hậu dược liệu quý"),
    "MeChuaRung": ("Trái me chua rừng", "🟤", "215 kcal / 100g", "Vỏ nâu quả cong múi chua gắt nấu canh lá giang"),
    "MeKeoThai": ("Trái me keo Thái", "🟢", "65 kcal / 100g", "Quả xoắn ốc cùi trắng đỏ ngọt bùi hấp dẫn"),
    "KheTa": ("Trái khế ta", "⭐", "31 kcal / 100g", "Khế chua năm khía làm gia vị canh chua và nấu lẩu"),
    "KheNgotMienNam": ("Trái khế ngọt miền Nam", "⭐", "34 kcal / 100g", "Mọng nước ngọt thanh dịu mát ăn tươi"),
    "KheRung": ("Trái khế rừng", "⭐", "30 kcal / 100g", "Quả nhỏ vị chua thanh dược liệu mát gan"),
    "DuaRungDuaDai": ("Trái dứa rừng (dứa dại)", "🍍", "45 kcal / 100g", "Quả mắt ghép màu cam rực dược liệu bổ thận mát gan"),
    "DuaMatRung": ("Trái dứa mật rừng", "🍍", "52 kcal / 100g", "Quả dứa rừng thơm ngọt đậm đà mật ong"),
    "SungRungMienTrung": ("Trái sung rừng miền Trung", "🟢", "42 kcal / 100g", "Quả mọc thành chùm lớn vị chát ngọt giàu canxi"),
    "SungNep": ("Trái sung nếp", "🟢", "41 kcal / 100g", "Quả tròn đặc ruột giòn ngọt muối chua tuyệt ngon"),
    "SungNepNon": ("Trái sung nếp non", "🟢", "38 kcal / 100g", "Quả non giòn sần sật ăn ghém ốc luộc thịt luộc"),
    "OiRung": ("Trái ổi rừng", "🍐", "60 kcal / 100g", "Quả nhỏ thơm ngát hương rừng tự nhiên nhiều vitamin C"),
    "OiDao": ("Trái ổi đào", "🍐", "65 kcal / 100g", "Ruột hồng đào thơm ngát ngọt thanh tốt cho tim mạch"),
    "OiTau": ("Trái ổi tàu", "🍐", "63 kcal / 100g", "Vỏ mỏng giòn ngọt vị đậm mọng nước"),
    "OiSeRung": ("Trái ổi sẻ rừng", "🍐", "62 kcal / 100g", "Ổi sẻ mọc rừng hương thơm ngào ngạt vị chua ngọt"),
    "TaoMeoTayBac": ("Trái táo mèo Tây Bắc", "🍏", "50 kcal / 100g", "Đặc sản Sơn La Yên Bái ngâm rượu ngâm đường trị tim mạch"),
    "TaoRung": ("Trái táo rừng", "🍏", "46 kcal / 100g", "Táo hoang dã quả nhỏ vị chua chát thanh nhiệt"),
    "LeRungSaPa": ("Trái lê rừng Sa Pa", "🍐", "40 kcal / 100g", "Vỏ nâu hạt sạn mọng nước ngọt thanh mát phổi"),
    "LeVang": ("Trái lê vàng", "🍐", "45 kcal / 100g", "Vỏ vàng bóng thịt giòn ngọt mọng nước"),
    "MoBac": ("Trái mơ Bắc", "🟡", "48 kcal / 100g", "Mơ Hương Tích chùa Hương ngâm đường ngâm rượu giải khát hè"),
    "MoRung": ("Trái mơ rừng", "🟡", "45 kcal / 100g", "Mơ rừng quả nhỏ vị chua gắt thơm nồng dược liệu"),
    "ManRung": ("Trái mận rừng", "🔴", "44 kcal / 100g", "Mận mọc hoang sườn núi vị chua giòn sần sật"),
    "ManComMienNui": ("Trái mận cơm miền núi", "🔴", "43 kcal / 100g", "Quả nhỏ giòn tan đầu mùa chua ngọt chấm muối ớt"),
    "DaoRung": ("Trái đào rừng", "🍑", "38 kcal / 100g", "Đào mọc hoang dã vùng cao thơm giòn thanh khiết"),
    "DaoBac": ("Trái đào Bắc", "🍑", "40 kcal / 100g", "Đào má phấn Lạng Sơn Sơn La ngọt thơm thanh mát"),
    "DaoTienVN": ("Trái đào tiên", "🍈", "45 kcal / 100g", "Vỏ xanh cứng tròn ruột đen ngâm rượu trị đau lưng"),
    "DaoLongVN": ("Trái đào lông", "🍑", "41 kcal / 100g", "Lớp lông tơ mịn màng thịt giòn ngọt dịu"),
    "DauTamDenVN": ("Trái dâu tằm đen", "🟣", "43 kcal / 100g", "Quả đen mọng nước ngâm siro dâu tằm giải nhiệt"),
    "DauTamTrangVN": ("Trái dâu tằm trắng", "⚪", "42 kcal / 100g", "Quả màu trắng ngà vị ngọt thanh tự nhiên"),
    "DauDaDatMienTayVN": ("Trái dâu da đất miền Tây", "🟡", "49 kcal / 100g", "Chùm quả sum suê quanh thân vị chua ngọt thanh mát"),
    "DauDaXoanMienTrung": ("Trái dâu da xoan miền Trung", "🔴", "48 kcal / 100g", "Quả mọng đỏ rực vị chua dịu chấm muối ớt"),
    "BonBotRung": ("Trái bòn bọt rừng", "⚪", "35 kcal / 100g", "Quả rừng hoang dã xốp nhẹ vị ngọt mát"),
    "ChayRungVN": ("Trái chay rừng", "🔴", "40 kcal / 100g", "Ruột hồng đỏ vị chua thanh kho cá nấu canh chua"),
    "VaHueVN": ("Trái vả Huế", "🟢", "45 kcal / 100g", "Quả to dẹt chát bùi xắt mỏng chấm mắm ruốc ăn gỏi"),
    "VaRung": ("Trái vả rừng", "🟢", "43 kcal / 100g", "Mọc ven suối quả nhiều cùi bùi ngọt thanh mát"),
    "SungMyTrongVN": ("Trái sung Mỹ trồng tại VN", "🟣", "74 kcal / 100g", "Mật ngọt lịm thơm mềm dẻo di thực thành công tại VN"),
    "JaboticabaTrongVN": ("Trái nho thân gỗ Jaboticaba trồng tại VN", "🟣", "65 kcal / 100g", "Mọc dính trên thân quả tím bóng ngọt ngào hương rượu vang"),
    "SimRungPhuQuocVN": ("Trái sim rừng Phú Quốc", "🟣", "55 kcal / 100g", "Quả tím mọng thơm ngát chuyên ủ rượu sim trứ danh"),
    "SimRungTayNguyen": ("Trái sim rừng Tây Nguyên", "🟣", "53 kcal / 100g", "Mọc bạt ngàn đồi núi vị ngọt chát giàu chất chống oxy hóa"),
    "MacCopSonTra": ("Trái mắc cọp Sơn Tra", "🍐", "45 kcal / 100g", "Lê rừng Tây Bắc vỏ nâu giòn tan mọng nước"),
    "SonTraDo": ("Trái sơn tra đỏ", "🔴", "48 kcal / 100g", "Quả đỏ thắm vị chua ngọt hạ mỡ máu bảo vệ tim mạch"),
    "SonTraVang": ("Trái sơn tra vàng", "🟡", "46 kcal / 100g", "Quả vàng ươm thơm mát ngâm đường làm nước giải khát"),
    "QuatRung": ("Trái quất rừng", "🍊", "34 kcal / 100g", "Quả nhỏ xíu vỏ thơm nồng tinh dầu chua thanh giải cảm"),
    "QuatCanh": ("Trái quất cảnh", "🍊", "35 kcal / 100g", "Quả tròn vàng cam rực rỡ biểu trưng ngày tết"),
    "BuoiRung": ("Trái bưởi rừng", "🍈", "37 kcal / 100g", "Bưởi mọc hoang vỏ dày hương tinh dầu nồng nàn"),
    "CamRung": ("Trái cam rừng", "🍊", "43 kcal / 100g", "Quả mọng chua thanh tép cam hoang dã"),
    "ChanhRungMienNui": ("Trái chanh rừng miền núi", "🍋", "28 kcal / 100g", "Chanh rừng quả nhỏ thơm lừng vỏ dùng làm gia vị đặc sản"),
    "MeRungChuaNho": ("Trái me rừng chua nhỏ", "🟢", "41 kcal / 100g", "Quả nhỏ tròn vị chua gắt kích thích vị giác"),
    "TramRungTayBac": ("Trái trám rừng Tây Bắc", "🟣", "148 kcal / 100g", "Trám đen rừng già cùi dẻo béo ngậy kho cá om thịt"),
    "TramNep": ("Trái trám nếp", "🟣", "150 kcal / 100g", "Trám cùi mềm dẻo như xôi nếp béo bùi đệ nhất"),
    "TramDenRungGia": ("Trái trám đen rừng già", "🟣", "152 kcal / 100g", "Cây cổ thụ trăm tuổi quả đen bóng béo ngậy"),
    "MacMat": ("Trái mắc mật", "🟡", "52 kcal / 100g", "Quả mọng vàng thơm lừng gia vị quay vịt lợn Lạng Sơn"),
    "MacMatRung": ("Trái mắc mật rừng", "🟡", "54 kcal / 100g", "Mọc trên núi đá vôi quả thơm nồng đặc trưng núi rừng"),
    "MacKhenNon": ("Trái mắc khén non", "🟢", "60 kcal / 100g", "Hạt tiêu rừng Tây Bắc thơm nồng nàn vị tê dịu"),
    "DauRungBacKan": ("Trái dâu rừng Bắc Kạn", "🍓", "35 kcal / 100g", "Dâu đỏ mọc tự nhiên ven rừng vị chua thanh ngâm siro"),
    "DauRungLaoCai": ("Trái dâu rừng Lào Cai", "🍓", "36 kcal / 100g", "Quả mọng đỏ tươi khí hậu sương mờ chua ngọt thanh"),
    "MamXoiDenRung": ("Trái mâm xôi đen rừng", "🍇", "50 kcal / 100g", "Chùm quả đen bóng ngọt mát hàm lượng sắt cao"),
    "MamXoiDoRung": ("Trái mâm xôi đỏ rừng", "🍓", "51 kcal / 100g", "Đỏ tươi mọng nước hương thơm thảo mộc"),
    "MamXoiVangRung": ("Trái mâm xôi vàng rừng", "🟡", "53 kcal / 100g", "Giống mâm xôi hiếm màu vàng óng ngọt dịu"),
    "CherryVietNam": ("Trái sơ ri / cherry Việt Nam", "🍒", "50 kcal / 100g", "Sơ ri Gò Công đỏ tươi vitamin C cao gấp 30 lần cam"),
    "NhoRungVN": ("Trái nho rừng", "🍇", "62 kcal / 100g", "Chùm nho rừng tím đen chua chát ủ rượu vang rừng thơm lừng"),
    "NhoDai": ("Trái nho dại", "🍇", "60 kcal / 100g", "Nho leo hoang dã quả nhỏ mọng nước vị chua gắt"),
    "DuaRung": ("Trái dưa rừng", "🥒", "18 kcal / 100g", "Quả dưa dại giòn mát làm dưa muối thanh nhiệt"),
    "BauRungNon": ("Trái bầu rừng non", "🍐", "15 kcal / 100g", "Bầu hoang non ngọt mát luộc chấm kho quẹt"),
    "BiRungNon": ("Trái bí rừng non", "🟢", "16 kcal / 100g", "Quả nhỏ non giòn ngọt đậm vị rau rừng"),
    "SuSuNon": ("Trái su su non", "🍐", "19 kcal / 100g", "Đặc sản Tam Đảo Sa Pa giòn ngọt xào tỏi luộc chấm muối vừng"),
    "OtRung": ("Trái ớt rừng", "🌶️", "40 kcal / 100g", "Ớt hiểm rừng cay nồng thơm ngát gia vị núi cao"),
    "CaRung": ("Trái cà rừng", "🟢", "25 kcal / 100g", "Cà mọc hoang quả nhỏ giòn chát chấm mắm cá"),
    "CaDaiRung": ("Trái cà dại rừng", "🟢", "24 kcal / 100g", "Quả tròn xanh mọc hoang dã dược liệu dân gian"),
    "TieuRung": ("Trái tiêu rừng / tiêu lốt", "🟢", "65 kcal / 100g", "Trái tiêu lốt dài cay ấm thơm nồng ẩm thực vùng cao"),
    "MacMatRungChin": ("Trái mắc mật rừng chín", "🟡", "55 kcal / 100g", "Quả chín mọng trong suốt ngọt thơm nức mũi chấm muối ớt")
}

def inject_batch6():
    print("=" * 75)
    print("   BẮT ĐẦU ĐỒNG BỘ 100 LOẠI TRÁI CÂY RỪNG, BẢN ĐỊA & ĐẶC SẢN VIỆT NAM (501 - 600)   ")
    print("=" * 75)

    db = dict(FRUIT_LIBRARY_600)
    added = 0
    updated = 0
    for k, (vn_name, icon, cal, ben) in WILD_100_BATCH6.items():
        is_new = k not in db
        db[k] = {
            "vn_name": vn_name,
            "icon": icon,
            "calories": cal,
            "vitamins": "Vitamin C, A, E, Kali, chất xơ và hoạt chất thảo dược rừng quý hiếm",
            "benefits": ben,
            "tips": "Đặc sản núi rừng và giống thuần Việt thu hái tự nhiên, rửa sạch trước khi thưởng thức.",
            "avg_price_per_kg": 65000
        }
        if is_new:
            added += 1
        else:
            updated += 1

    out_file = os.path.join(PROJECT_ROOT, "src", "fruit_library_600.py")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("# fruit_library_600.py - Thư viện Tri thức Trái cây Toàn cầu Chuẩn hóa\n")
        f.write("FRUIT_LIBRARY_600 = " + json.dumps(db, ensure_ascii=False, indent=4) + "\n")

    print(f"[OK] Đã nạp thành công: {added} loại quả mới, cập nhật {updated} loại!")
    print(f"[*] Tổng số loại trái cây hiện tại trong Thư viện: {len(db)} loại!")

if __name__ == "__main__":
    inject_batch6()

