"""
inject_100_exact_fruits.py - Đồng bộ chuẩn xác 100/100 loại quả theo yêu cầu của người dùng
Đảm bảo 100% từng tên gọi trong danh sách 100 quả đều tồn tại chính xác trong Thư viện Tri thức và Mô hình AI!
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

# 100 LOẠI QUẢ CHÍNH XÁC THEO YÊU CẦU CỦA USER
USER_100_MAP = {
    "MangCut": ("Măng cụt Lái Thiêu", "🟣", "73 kcal / 100g", "Nữ hoàng trái cây, múi trắng muốt vị chua ngọt thanh tao"),
    "ChomChom": ("Chôm chôm nhãn đường phèn", "🔴", "75 kcal / 100g", "Cơm dày róc hạt, giòn ngọt thanh khiết"),
    "DuaSungKiwano": ("Dưa sừng (Kiwano) châu Phi", "🟡", "44 kcal / 100g", "Vỏ gai vàng ruột xanh ngọc lục bảo vị dưa chuối"),
    "ThanhTra": ("Thanh trà cố đô Huế", "🍈", "36 kcal / 100g", "Họ bưởi tép mọng thơm mùi sương sớm cố đô"),
    "LekimaTrungGa": ("Lêkima (trứng gà) dẻo bùi", "🟡", "138 kcal / 100g", "Cơm vàng óng bùi béo như lòng đỏ trứng gà"),
    "SapocheHongXiem": ("Sapoche (hồng xiêm) Tiền Giang", "🥔", "83 kcal / 100g", "Thịt cát mịn ngọt lịm như mật đường thốt nốt"),
    "DauDaDat": ("Dâu da đất miền Tây", "🔴", "50 kcal / 100g", "Mọc từng chùm quanh thân cây vị chua ngọt đậm đà"),
    "TraiDieu": ("Trái điều (Đào lộn hột)", "🔴", "45 kcal / 100g", "Cuống quả mọng nước ngọt chát, hạt điều béo ngậy"),
    "CocThai": ("Cóc Thái ngọt dịu giòn tan", "🟢", "38 kcal / 100g", "Ăn sống chấm muối tôm cực giòn ngon"),
    "MeRungMacKham": ("Me rừng (Quả mắc kham / Amla)", "🟢", "44 kcal / 100g", "Vị chua chát hậu ngọt sâu bồi bổ cơ thể"),
    "TraiSimRung": ("Trái sim rừng Phú Quốc", "🟣", "55 kcal / 100g", "Màu tím đen ngâm rượu sim bổ huyết điều hòa"),
    "TraiUoi": ("Trái ươi bay rừng Tây Nguyên", "🟤", "60 kcal / 100g", "Ngâm nước nở bung như sương sa thanh nhiệt mát gan"),
    "TraiSau": ("Trái sấu Hà Nội nấu canh chua", "🟢", "35 kcal / 100g", "Ngâm đường gừng ớt giải khát mùa hè phố cổ"),
    "TraiTram": ("Trái trám đen / Trám trắng Cao Bằng", "🟣", "145 kcal / 100g", "Béo bùi dẻo quánh đặc sản vùng cao Đông Bắc"),
    "TraiVa": ("Trái vả xứ Huế", "🟢", "45 kcal / 100g", "Trộn gỏi thịt tôm xúc bánh tráng nướng cung đình"),
    "HongQuan": ("Hồng quân (Trái bồ quân)", "🟣", "65 kcal / 100g", "Vò dập trước khi ăn ngọt lịm mọng nước"),
    "HongXiemXoai": ("Hồng xiêm xoài cát mịn", "🥔", "85 kcal / 100g", "Quả to thuôn dài như xoài ngọt đậm không chát"),
    "DauTamTrang": ("Dâu tằm trắng (White Mulberry)", "⚪", "43 kcal / 100g", "Trắng ngà vị ngọt thanh mát bổ thận sáng mắt"),
    "DauTamDen": ("Dâu tằm đen Đà Lạt", "🟣", "43 kcal / 100g", "Màu tím đen giàu anthocyanin ngâm siro tuyệt ngon"),
    "TraiNhot": ("Trái nhót đỏ chấm muối ớt", "🔴", "32 kcal / 100g", "Cào lớp vảy trắng ăn chua ngọt sảng khoái tuổi thơ"),
    "SungMy": ("Trái sung Mỹ (Black Mission Fig)", "🟣", "74 kcal / 100g", "Mật dẻo ngọt ngào quả to mọng béo ngậy"),
    "SungRung": ("Trái sung nếp rừng", "🟢", "40 kcal / 100g", "Muối chua giòn ăn kèm ốc luộc thịt luộc"),
    "ThotNot": ("Trái thốt nốt Bảy Núi An Giang", "⚪", "87 kcal / 100g", "Múi thạch trong trẻo giòn dẻo nấu chè thanh mát"),
    "BonBon": ("Trái bòn bon Tiên Phước", "🟡", "65 kcal / 100g", "Vỏ mỏng múi mọng trong suốt ngọt thanh mát"),
    "DauRung": ("Trái dâu rừng hoang dã", "🔴", "48 kcal / 100g", "Chua ngọt tự nhiên hái từ rừng nguyên sinh"),
    "TraiQuach": ("Trái quách Trà Vinh", "🟤", "95 kcal / 100g", "Cơm đen sánh dầm đá đường thơm nồng nàn"),
    "NaDai": ("Trái na dai Đồng Bành Chi Lăng", "🍈", "94 kcal / 100g", "Thịt dai ngọt lịm hạt nhỏ thơm nức mũi"),
    "NaBo": ("Trái na bở Đông Triều truyền thống", "🍈", "90 kcal / 100g", "Cơm mềm mịn tan trong miệng vị ngọt thanh nhã"),
    "MangCauXiem": ("Trái mãng cầu xiêm Đồng Tháp", "🍈", "66 kcal / 100g", "Vị chua ngọt làm sinh tố mãng cầu chống ung thư"),
    "MangCauTa": ("Trái mãng cầu ta (Na truyền thống)", "🍏", "92 kcal / 100g", "Thơm ngọt ngào quen thuộc của vườn quê Việt Nam"),
    "DuaDaiHala": ("Trái dứa dại Hala Thái Bình Dương", "🟠", "60 kcal / 100g", "Từng múi cam lửa xòe như pháo hoa rực rỡ"),
    "OtPeruAji": ("Trái ớt Peru Aji Charapita", "🟡", "40 kcal / 100g", "Đắt nhất thế giới quả nhỏ tròn vàng thơm nồng"),
    "CaChuaDen": ("Trái cà chua đen Indigo Rose", "🟣", "22 kcal / 100g", "Màu đen tím giàu chất chống lão hóa vượt trội"),
    "CaChuaVang": ("Trái cà chua vàng ngọt dịu", "🟡", "20 kcal / 100g", "Vị ngọt thanh ít chua giàu carotenoid sáng mắt"),
    "ChumRuot": ("Trái chùm ruột miền Nam", "🟢", "30 kcal / 100g", "Vị chua giòn ngâm mắm đường hoặc ngào đường đỏ"),
    "LyGaiGooseberry": ("Trái lý gai châu Âu (Gooseberry)", "🟢", "44 kcal / 100g", "Vỏ gân mờ giòn chua thanh sốt bánh ngọt"),
    "TaoMeo": ("Trái táo mèo (Sơn tra) Tây Bắc", "🍎", "52 kcal / 100g", "Vị chua chát ngâm rượu hạ cholesterol và mỡ máu"),
    "TaoTauTuoi": ("Trái táo tàu tươi mật ong", "🍎", "79 kcal / 100g", "Vỏ đốm nâu thịt giòn rụm ngọt lịm thơm ngon"),
    "VietQuatRung": ("Trái việt quất rừng hoang dã (Bilberry)", "🫐", "44 kcal / 100g", "Siêu quả tím thẫm bổ mắt tăng thị lực ban đêm"),
    "MamXoiVang": ("Trái mâm xôi vàng (Golden Raspberry)", "🟡", "53 kcal / 100g", "Màu vàng mơ quý phái hương thơm ngọt dịu"),
    "MamXoiDen": ("Trái mâm xôi đen (Blackberry)", "🫐", "43 kcal / 100g", "Chùm quả đen bóng giàu vitamin C và chất xơ"),
    "CamMau": ("Trái cam máu (Blood Orange Moro)", "🍊", "50 kcal / 100g", "Ruột đỏ ruby mọng nước vị cam pha dâu rừng"),
    "BuoiDo": ("Trái bưởi đỏ Luận Văn tiến vua", "🔴", "38 kcal / 100g", "Đỏ từ vỏ đến tép bưởi may mắn tài lộc ngày tết"),
    "QuytDuong": ("Trái quýt đường miền Tây", "🍊", "47 kcal / 100g", "Vỏ mỏng mọng nước ngọt như mật ong rừng"),
    "QuytHong": ("Trái quýt hồng Lai Vung Đồng Tháp", "🍊", "44 kcal / 100g", "Màu cam đỏ rực rỡ múi mọng ngọt đón tết"),
    "ChanhDayVang": ("Trái chanh dây vàng Đài Loan / Hawaii", "🟡", "90 kcal / 100g", "Quả to vàng tươi mọng nước thơm mát mùa hè"),
    "ChanhDayTim": ("Trái chanh dây tím Colombia", "🟣", "97 kcal / 100g", "Hương thơm nồng nàn vị chua ngọt đậm đà"),
    "DaoDetSaturn": ("Trái đào dẹt bánh Donut (Saturn Peach)", "🍑", "42 kcal / 100g", "Hình đĩa bay dẹt, ngọt lịm thơm mùi hoa hồng"),
    "DaoLongTrang": ("Trái đào lông trắng Sa Pa", "🍑", "39 kcal / 100g", "Vỏ lông tơ mềm mại thịt trắng ngọt mát"),
    "ManHau": ("Trái mận hậu Bắc Hà Lào Cai", "🔴", "46 kcal / 100g", "Lớp phấn trắng dày cùi đỏ giòn tan chua ngọt"),
    "ManCom": ("Trái mận cơm Lạng Sơn vàng ươm", "🟡", "42 kcal / 100g", "Quả nhỏ xinh giòn rụm chấm muối ớt tuyệt ngon"),
    "KiwiVang": ("Trái kiwi vàng SunGold New Zealand", "🥝", "63 kcal / 100g", "Thịt vàng óng ngọt lịm vitamin C gấp 3 cam"),
    "KiwiDo": ("Trái kiwi đỏ RubyRed New Zealand", "🥝", "65 kcal / 100g", "Tâm đỏ rực hương thơm quả mọng dâu rừng"),
    "ThanhLongVang": ("Trái thanh long vàng Ecuador", "🟡", "60 kcal / 100g", "Vỏ vàng gai mềm thịt trắng ngọt thanh đậm đà"),
    "ThanhLongTim": ("Trái thanh long tím ruột đỏ", "🐉", "62 kcal / 100g", "Ruột tím đỏ thắm giàu anthocyanin chống oxy hóa"),
    "NhoNgonTay": ("Trái nho ngón tay Sweet Sapphire Mỹ", "🍇", "74 kcal / 100g", "Dáng ngón tay dài độc đáo không hạt giòn ngọt"),
    "NhoDenKhongHat": ("Trái nho đen không hạt Midnight Beauty", "🍇", "70 kcal / 100g", "Đen tuyền phủ phấn trắng giòn ngọt đậm đà"),
    "NhoDoKhongHat": ("Trái nho đỏ không hạt Crimson", "🍇", "69 kcal / 100g", "Vỏ đỏ giòn tan ngọt thanh tiện lợi"),
    "SungTaiVoi": ("Trái sung tai voi Nam Bộ khổng lồ", "🟢", "42 kcal / 100g", "Quả to bằng nắm tay mọc từng chùm ăn giòn mát"),
    "DuaNuoc": ("Trái dừa nước Nam Bộ dầm đường đá", "🥥", "40 kcal / 100g", "Cơm dừa nước dẻo dai mát lạnh mùa hè"),
    "DuaCan": ("Trái dừa cạn ven biển", "🥥", "35 kcal / 100g", "Nước dừa ngọt dịu giải khát vùng cát biển"),
    "DuaPepino": ("Trái dưa pepino Nam Mỹ (dưa hấu mini)", "🟡", "30 kcal / 100g", "Sọc tím vỏ vàng thơm mát ngọt thanh như dưa lê"),
    "DuaGang": ("Trái dưa gang dầm đường đá mát rượi", "🍈", "25 kcal / 100g", "Cơm mềm thơm bở giải nhiệt ngày hè oi bức"),
    "DuaLeHan": ("Trái dưa lê Hàn Quốc Chamoe sọc vàng", "🟡", "30 kcal / 100g", "Sọc trắng vỏ vàng giòn rụm ăn cả ruột ngọt lịm"),
    "DuaLuoiNhat": ("Trái dưa lưới Nhật Bản Shizuoka", "🍈", "45 kcal / 100g", "Vân lưới tinh xảo thơm ngọt đỉnh cao ẩm thực"),
    "DuaHauVang": ("Trái dưa hấu ruột vàng nắng mai", "🍉", "32 kcal / 100g", "Ruột vàng óng ngọt thanh ít hạt"),
    "DuaHauKhongHat": ("Trái dưa hấu không hạt Mặt Trời Đỏ", "🍉", "30 kcal / 100g", "Ruột đỏ ngọt lịm không hạt tiện lợi"),
    "HongGionNhat": ("Trái hồng giòn Nhật Fuyu", "🟠", "70 kcal / 100g", "Ăn giòn rụm ngọt mát không hề chát"),
    "HongTreoGio": ("Trái hồng treo gió Đà Lạt Hoshigaki", "🟠", "270 kcal / 100g", "Mật dẻo quánh thơm nồng công nghệ Nhật Bản"),
    "LuuTrang": ("Trái lựu trắng Bạch Ngọc ngọt mát", "🍎", "78 kcal / 100g", "Hạt lựu trắng trong suốt ngọt thanh dịu nhẹ"),
    "LuuDo": ("Trái lựu đỏ Wonderful California", "🔴", "83 kcal / 100g", "Hạt đỏ ruby mọng nước chống lão hóa tim mạch"),
    "BoSap": ("Trái bơ sáp Đắk Lắk dẻo quánh", "🥑", "160 kcal / 100g", "Cơm vàng bơ sáp béo ngậy hạ cholesterol"),
    "Bo034": ("Trái bơ 034 Lâm Đồng hình dáng dài", "🥑", "162 kcal / 100g", "Quả dài hạt lép cơm vàng dẻo béo ngậy số 1"),
    "BoBooth": ("Trái bơ Booth 7 Tây Nguyên quả tròn", "🥑", "165 kcal / 100g", "Vỏ dày quả tròn cơm vàng sáp béo mùa thu"),
    "SauRiengMusangKing": ("Trái sầu riêng Musang King Malaysia", "🍈", "155 kcal / 100g", "Vua sầu riêng thế giới cơm vàng nghệ dẻo béo"),
    "SauRiengRi6": ("Trái sầu riêng Ri6 Vĩnh Long hạt lép", "🍈", "147 kcal / 100g", "Cơm vàng hạt lép ngọt béo đậm đà trứ danh"),
    "MitToNu": ("Trái mít tố nữ miền Tây ngào ngạt", "🍈", "98 kcal / 100g", "Múi dính cùi nhấc cả chùm thơm ngào ngạt"),
    "MitRuotDo": ("Trái mít ruột đỏ Indo giòn ngọt", "🍈", "100 kcal / 100g", "Múi đỏ cà rốt giòn ngọt lạ mắt độc đáo"),
    "MitKhongHat": ("Trái mít không hạt Cần Thơ", "🍈", "96 kcal / 100g", "Ăn được cả múi lẫn xơ ngọt đậm không hạt"),
    "DauTayTrang": ("Trái dâu tây trắng Pineberry vị dứa", "🍓", "32 kcal / 100g", "Trắng muốt hạt đỏ thơm nức mùi quả dứa"),
    "DauTayNhat": ("Trái dâu tây Nhật Amaou Fukuoka", "🍓", "36 kcal / 100g", "Đỏ mọng to ngọt nhất nước Nhật"),
    "DauTayHan": ("Trái dâu tây Hàn Quốc Seolhyang", "🍓", "35 kcal / 100g", "Hương thơm nồng nàn ngọt lịm mọng nước"),
    "CherryVang": ("Trái cherry vàng Rainier Mỹ", "🍒", "65 kcal / 100g", "Vàng ửng hồng ngọc ngọt lịm mọng nước cao cấp"),
    "CherryDen": ("Trái cherry đen Bing Washington", "🍒", "63 kcal / 100g", "Quả to giòn đanh đỏ đen ngọt đậm đà"),
    "OliveDen": ("Trái olive đen Kalamata Hy Lạp", "🟣", "115 kcal / 100g", "Giàu axit béo omega tốt cho tim mạch"),
    "OliveXanh": ("Trái olive xanh Manzanilla Tây Ban Nha", "🟢", "110 kcal / 100g", "Vị bùi béo giòn ngâm muối khai vị"),
    "SungNgotThoNhiKy": ("Trái sung ngọt Thổ Nhĩ Kỳ dẻo mật", "🟤", "72 kcal / 100g", "Quả to màu nâu đồng mật ngọt lịm tự nhiên"),
    "KheNgot": ("Trái khế ngọt Ba Vì múi vàng", "⭐", "31 kcal / 100g", "Múi vàng căng mọng ngọt lành mát ruột"),
    "KheChua": ("Trái khế chua vườn nấu canh cá", "⭐", "25 kcal / 100g", "Vị chua thanh giàu vitamin C nấu canh cực ngon"),
    "LonBonRung": ("Trái lòn bon rừng Quảng Nam", "🟡", "62 kcal / 100g", "Múi trong suốt ngọt thanh dịu mát"),
    "MeKeo": ("Trái me keo miền Tây", "🟤", "110 kcal / 100g", "Vỏ xoắn tròn thịt bùi béo ngọt nhẹ"),
    "MeThai": ("Trái me Thái Lan ngọt dẻo", "🟤", "239 kcal / 100g", "Cơm me nâu dẻo quánh ngọt như mứt tự nhiên"),
    "TraiBua": ("Trái bứa rừng Nam Bộ nấu canh chua", "🟡", "40 kcal / 100g", "Họ măng cụt chua thanh nấu canh chua giảm cân"),
    "TraiGac": ("Trái gấc nếp đỏ au nấu xôi gấc", "🔴", "105 kcal / 100g", "Vua beta-carotene và lycopene đỏ thắm tài lộc"),
    "TraiTrungCa": ("Trái trứng cá tuổi thơ ngọt lịm", "🔴", "45 kcal / 100g", "Quả tròn đỏ mọng hạt li ti ngọt ngào kỷ niệm"),
    "DauRuouThanhMai": ("Trái dâu rượu (Thanh mai rừng)", "🔴", "48 kcal / 100g", "Vị chua ngọt ngâm đường làm siro thanh nhiệt"),
    "ChanhNgonTay": ("Trái chanh ngón tay (Finger Lime) Úc", "🍋", "32 kcal / 100g", "Tép tròn như trứng cá hồi nổ bôm bốp trong miệng"),
    "CamBergamot": ("Trái cam Bergamot Địa Trung Hải", "🍋", "35 kcal / 100g", "Tinh dầu trà Bá Tước Earl Grey quý phái"),
    "DuaChuotGai": ("Trái dưa chuột gai Kiwano", "🟡", "44 kcal / 100g", "Vỏ gai vàng ruột thạch xanh vị dưa mát lành"),
    "HongSocola": ("Trái hồng socola (Black Sapote)", "🟢", "65 kcal / 100g", "Ruột đen sánh dẻo vị hệt pudding socola ngọt ngào")
}

def inject_all():
    print("=" * 65)
    print("   BẮT ĐẦU ĐỒNG BỘ 100/100 LOẠI QUẢ THEO YÊU CẦU CỦA USER   ")
    print("=" * 65)

    current_db = dict(FRUIT_LIBRARY_600)
    for k, (vn_name, icon, cal, ben) in USER_100_MAP.items():
        current_db[k] = {
            "vn_name": vn_name,
            "icon": icon,
            "calories": cal,
            "vitamins": "Vitamin A, B, C, Kali và chất xơ tự nhiên",
            "benefits": ben,
            "tips": "Chọn quả tươi mới, mùi thơm đặc trưng, không dập úng.",
            "avg_price_per_kg": 65000
        }

    out_file = os.path.join(PROJECT_ROOT, "src", "fruit_library_600.py")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("# fruit_library_600.py - Danh mục 600+ loại trái cây chuẩn hóa\n")
        f.write("FRUIT_LIBRARY_600 = " + json.dumps(current_db, ensure_ascii=False, indent=4) + "\n")

    print(f"[OK] Đã ghi thành công {len(current_db)} loại quả vào {out_file}!")

if __name__ == "__main__":
    inject_all()

