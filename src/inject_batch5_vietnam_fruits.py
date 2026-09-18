"""
inject_batch5_vietnam_fruits.py - Tích hợp và Huấn luyện 100 Đặc sản Trái cây Thuần Việt (401 - 500)
Đề tài số 22: Hệ thống AI Nhận diện & Phân loại Trái cây Thông minh
Bao quát toàn diện 100 loại hoa quả đặc sản 3 miền Bắc - Trung - Nam và Tây Nguyên.
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

# 100 ĐẶC SẢN HOA QUẢ VIỆT NAM (401 - 500)
VN_100_BATCH5 = {
    "BuoiDaXanhVN": ("Trái bưởi da xanh Bến Tre", "🍈", "38 kcal / 100g", "Tép hồng đỏ mọng nước vị ngọt thanh không chua chát"),
    "BuoiNamRoiVN": ("Trái bưởi năm roi Vĩnh Long", "🍈", "36 kcal / 100g", "Không hạt khi chín tép vàng đều mọng nước chua ngọt"),
    "BuoiDienVN": ("Trái bưởi Diễn Hà Nội", "🍈", "40 kcal / 100g", "Vỏ vàng ươm để càng héo càng ngọt đậm thơm ngát tết"),
    "CamVinh": ("Trái cam Vinh Nghệ An", "🍊", "45 kcal / 100g", "Vỏ mỏng mọng nước ngọt đậm hương thơm nức tiếng xứ Nghệ"),
    "CamSanhMienTay": ("Trái cam sành miền Tây", "🍊", "46 kcal / 100g", "Vỏ sần sùi dày múi mọng nước chuyên vắt giải khát"),
    "CamDuongCanh": ("Trái cam đường canh Hà Nội", "🍊", "47 kcal / 100g", "Vỏ mỏng dính màu đỏ cam ngọt lịm như đường phèn"),
    "CamXoanLaiVung": ("Trái cam xoàn Lai Vung", "🍊", "48 kcal / 100g", "Đáy có đồng xu tròn ngọt lịm không hề có vị chua"),
    "QuytBacSon": ("Trái quýt Bắc Sơn Lạng Sơn", "🍊", "43 kcal / 100g", "Màu vàng ươm mọc trên thung lũng đá vôi ngọt thơm"),
    "QuytHongLaiVungVN": ("Trái quýt hồng Lai Vung Đồng Tháp", "🍊", "44 kcal / 100g", "Màu cam lửa rực rỡ mọng nước đón tết miền Tây"),
    "QuatTacVN": ("Trái quất (tắc) tươi", "🍊", "35 kcal / 100g", "Vỏ thơm nồng nước chua thanh giải nhiệt trị ho"),
    "ChanhTaVN": ("Trái chanh ta (Chanh tròn xanh)", "🍋", "29 kcal / 100g", "Vỏ mỏng thơm ngát nhiều nước chua thanh tự nhiên"),
    "ChanhDaoVN": ("Trái chanh đào mật ong", "🍋", "30 kcal / 100g", "Ruột hồng đào đẹp mắt ngâm mật ong trị ho cảm"),
    "ChanhKhongHatVN": ("Trái chanh không hạt tứ quý", "🍋", "28 kcal / 100g", "Quả mọng nước dễ vắt tiện lợi xuất khẩu"),
    "ChanhGiayVN": ("Trái chanh giấy truyền thống", "🍋", "29 kcal / 100g", "Vỏ mỏng như giấy tinh dầu thơm ngát bậc nhất"),
    "BoBoothTayNguyen": ("Trái bơ booth Tây Nguyên", "🥑", "165 kcal / 100g", "Quả tròn vỏ dày cơm vàng sáp béo ngậy mùa thu đông"),
    "Bo034LamDong": ("Trái bơ 034 Lâm Đồng dài hạt lép", "🥑", "162 kcal / 100g", "Quả dài 25-35cm cơm vàng dẻo quánh số 1 Việt Nam"),
    "BoSapDakLak": ("Trái bơ sáp Đắk Lắk", "🥑", "160 kcal / 100g", "Bơ sáp béo ngậy ngọt bùi dầm sữa đá tuyệt ngon"),
    "SauRiengRi6VN": ("Trái sầu riêng Ri6 hạt lép", "🍈", "147 kcal / 100g", "Cơm vàng óng hạt lép vị béo ngọt đậm đà danh bất hư truyền"),
    "SauRiengMonthongVN": ("Trái sầu riêng Monthong Dona", "🍈", "150 kcal / 100g", "Cơm dày ráo không nhão vị ngọt thanh hương thơm quyến rũ"),
    "SauRiengChuongBoVN": ("Trái sầu riêng chuồng bò bơ sữa", "🍈", "140 kcal / 100g", "Hạt nhỏ béo ngậy mùi sữa tươi cơm dẻo quánh"),
    "MitToNuVN": ("Trái mít tố nữ miền Tây", "🍈", "98 kcal / 100g", "Múi dính vào cùi xách cả chùm thơm ngào ngạt"),
    "MitThaiSieuSom": ("Trái mít Thái siêu sớm Changai", "🍈", "95 kcal / 100g", "Múi giòn rụm ráo nước ngọt đậm hạt nhỏ"),
    "MitDaiTruyenThong": ("Trái mít dai truyền thống vườn quê", "🍈", "94 kcal / 100g", "Múi vàng dai giòn ngọt sắc đượm hồn quê"),
    "MitNghe": ("Trái mít nghệ cơm vàng", "🍈", "96 kcal / 100g", "Múi to dày màu vàng nghệ ngọt lịm thơm phức"),
    "MitRuotDoVN": ("Trái mít ruột đỏ Indo trồng tại VN", "🍈", "100 kcal / 100g", "Múi đỏ cà rốt giòn ngọt ráo nước độc lạ"),
    "XoaiCatHoaLocVN": ("Trái xoài cát Hòa Lộc Tiền Giang", "🥭", "65 kcal / 100g", "Vua các loại xoài thịt mịn không xơ thơm lừng"),
    "XoaiCatChuVN": ("Trái xoài cát Chu Cao Lãnh", "🥭", "62 kcal / 100g", "Hương thơm vani ngọt ngào thịt mềm mọng nước"),
    "XoaiKeoVN": ("Trái xoài keo giòn rụm", "🥭", "58 kcal / 100g", "Ăn xanh giòn sần sật chấm mắm đường muối tôm"),
    "XoaiTuongVN": ("Trái xoài tượng quả đại", "🥭", "60 kcal / 100g", "Quả to khổng lồ 1kg giòn rụm làm nộm gỏi"),
    "XoaiThaiVN": ("Trái xoài Thái ngọt giòn", "🥭", "63 kcal / 100g", "Vị ngọt lịm ngay từ khi quả còn xanh"),
    "ThanhLongRuotTrang": ("Trái thanh long ruột trắng Bình Thuận", "🐉", "55 kcal / 100g", "Mát lành ngọt dịu thanh nhiệt giải độc cơ thể"),
    "ThanhLongRuotDoVN": ("Trái thanh long ruột đỏ Tiền Giang", "🐉", "60 kcal / 100g", "Ruột đỏ thắm giàu anthocyanin ngọt đậm đà"),
    "ThanhLongTimHong": ("Trái thanh long ruột tím hồng Long An", "🐉", "62 kcal / 100g", "Màu tím hồng quyến rũ vị ngọt lịm thơm ngon"),
    "ChuoiTieuVN": ("Trái chuối tiêu hồng Nam Hà", "🍌", "89 kcal / 100g", "Quả cong dài thơm ngọt ngào giàu kali"),
    "ChuoiSuVN": ("Trái chuối sứ (Chuối xiêm) Bến Tre", "🍌", "88 kcal / 100g", "Luộc dẻo hoặc nướng mỡ hành ngọt bùi tự nhiên"),
    "ChuoiLabaDaLat": ("Trái chuối laba Đà Lạt tiến vua", "🍌", "90 kcal / 100g", "Dẻo quánh thơm nồng hương vị cao nguyên sương mù"),
    "ChuoiCauVN": ("Trái chuối cau quả nhỏ", "🍌", "91 kcal / 100g", "Quả nhỏ tròn mập mạp ngọt sắc đậm đà"),
    "ChuoiNguVN": ("Trái chuối ngự Đại Hoàng tiến vua", "🍌", "92 kcal / 100g", "Vỏ mỏng như lụa hương thơm ngát danh bất hư truyền"),
    "DuaQueenVN": ("Trái dứa (thơm) Queen Kiên Giang", "🍍", "50 kcal / 100g", "Thịt vàng đậm mắt sâu giòn rụm ngọt sắc"),
    "DuaMatVN": ("Trái dứa mật Đơn Dương Lâm Đồng", "🍍", "53 kcal / 100g", "Chảy mật ngọt lịm mọng nước không hề rát lưỡi"),
    "DuaCayenneVN": ("Trái dứa Cayenne quả to mọng nước", "🍍", "48 kcal / 100g", "Quả lớn mắt phẳng chuyên chế biến nước ép"),
    "DuaHauLongAn": ("Trái dưa hấu Long An ngọt lịm", "🍉", "30 kcal / 100g", "Cát mịn ngọt mát giải khát ngày hè oi ả"),
    "DuaHauKhongHatVN": ("Trái dưa hấu không hạt Mặt Trời Đỏ", "🍉", "31 kcal / 100g", "Ruột đỏ tươi không hạt tiện lợi ngọt thanh"),
    "DuaGangVN": ("Trái dưa gang dầm đường đá", "🍈", "25 kcal / 100g", "Bở tơi thơm mát giải nhiệt số 1 mùa hè"),
    "DuaLeVN": ("Trái dưa lê bạch ngọc giòn ngọt", "🍈", "32 kcal / 100g", "Vỏ trắng ngà thơm ngát giòn tan ngọt lành"),
    "DuaLuoiVN": ("Trái dưa lưới Huỳnh Long ruột cam", "🍈", "34 kcal / 100g", "Vân lưới dày thịt cam giòn ngọt thơm mát"),
    "DuaChuotTa": ("Trái dưa chuột ta (Dưa leo nếp)", "🥒", "15 kcal / 100g", "Đặc ruột giòn ngọt thơm mùi lúa nếp non"),
    "DuaChuotRung": ("Trái dưa chuột rừng nhỏ giòn", "🥒", "16 kcal / 100g", "Quả nhỏ xíu giòn đanh vị chua thanh tự nhiên"),
    "CaChuaBiVN": ("Trái cà chua bi giòn ngọt Đà Lạt", "🍅", "27 kcal / 100g", "Quả nhỏ đỏ mọng ăn sống hoặc trộn salad tuyệt ngon"),
    "CaChuaBeef": ("Trái cà chua beef quả to thịt dày", "🍅", "20 kcal / 100g", "Quả khổng lồ thịt dày ít hạt chuyên làm burger"),
    "CaChuaThanGoVN": ("Trái cà chua thân gỗ Tamarillo Đà Lạt", "🔴", "35 kcal / 100g", "Trồng thử nghiệm tại Lâm Đồng vị chua ngọt độc đáo"),
    "OiLeVN": ("Trái ổi lê ruột trắng giòn", "🍐", "68 kcal / 100g", "Cực giòn ngọt thanh vitamin C gấp 4 lần cam"),
    "OiNuHoangVN": ("Trái ổi nữ hoàng ít hạt", "🍐", "70 kcal / 100g", "Thịt dày giòn xốp thơm lừng chất lượng cao"),
    "OiRuotDoVN": ("Trái ổi ruột đỏ xá lị", "🍐", "66 kcal / 100g", "Ruột hồng đỏ giàu lycopene thơm ngát"),
    "OiBoThaiBinh": ("Trái ổi bo Thái Bình cùi dày", "🍐", "65 kcal / 100g", "Quả to sần sùi cùi dày giòn ngọt đặc sản quê lúa"),
    "OiSeVN": ("Trái ổi sẻ vườn quê quả nhỏ", "🍐", "64 kcal / 100g", "Quả nhỏ thơm ngát cả vườn đượm kỷ niệm tuổi thơ"),
    "OiDaiLoanVN": ("Trái ổi Đài Loan giòn ngọt", "🍐", "68 kcal / 100g", "Vỏ xanh sáng thịt giòn ngọt thanh mát quanh năm"),
    "TaoTaXanh": ("Trái táo ta (Táo xanh chua ngọt)", "🍏", "45 kcal / 100g", "Quả tròn xanh giòn tan chấm muối ớt tuyệt cú mèo"),
    "TaoDoMienBac": ("Trái táo đỏ miền Bắc quả nhỏ", "🍎", "48 kcal / 100g", "Màu đỏ mận chín vị chua ngọt thanh mát"),
    "HongGionDaLatVN": ("Trái hồng giòn Đà Lạt Fuyu", "🟠", "70 kcal / 100g", "Giòn sần sật không hề chát ngọt dịu mùa thu"),
    "HongNgamBaoLamVN": ("Trái hồng ngâm Bảo Lâm Lạng Sơn", "🟠", "72 kcal / 100g", "Ngâm nước suối giòn đanh ngọt lịm đặc sản xứ Lạng"),
    "HongVuongDaLat": ("Trái hồng vuông Đà Lạt giòn rụm", "🟠", "71 kcal / 100g", "Quả vuông 4 cạnh giòn tan ngọt ngào thanh khiết"),
    "LuuDoNinhThuan": ("Trái lựu đỏ Ninh Thuận mọng nước", "🔴", "80 kcal / 100g", "Vỏ đỏ hạt mọng nước ngọt thanh chống lão hóa"),
    "LuuTrangNinhThuan": ("Trái lựu trắng Bạch ngọc Ninh Thuận", "🍎", "78 kcal / 100g", "Hạt trắng trong suốt ngọt lịm vị thanh mát"),
    "NhoNinhThuan": ("Trái nho Ninh Thuận truyền thống", "🍇", "65 kcal / 100g", "Chùm nho sai trĩu vị chua ngọt làm vang nho"),
    "NhoXanhNinhThuan": ("Trái nho xanh Ninh Thuận NH01-48", "🍇", "68 kcal / 100g", "Vỏ xanh bóng thịt chắc giòn ngọt mát"),
    "NhoDoNinhThuan": ("Trái nho đỏ Ninh Thuận Red Cardinal", "🍇", "67 kcal / 100g", "Quả tròn đỏ mọng ngọt thanh đặc sản vùng nắng gió"),
    "DauTayDaLatVN": ("Trái dâu tây Đà Lạt đỏ mọng", "🍓", "32 kcal / 100g", "Hái tại vườn đỏ thắm vị chua ngọt làm mứt và sinh tố"),
    "ManHaNoi": ("Trái mận Hà Nội (Mận hậu tươi)", "🔴", "46 kcal / 100g", "Chấm muối ớt giòn rụm chua ngọt phố cổ"),
    "ManBacTamHoa": ("Trái mận Bắc (Mận Tam Hoa Mộc Châu)", "🔴", "45 kcal / 100g", "Vỏ đỏ tím cùi đỏ rực giòn sần sật mùa hè"),
    "ManHauSonLa": ("Trái mận hậu Sơn La phấn trắng", "🔴", "47 kcal / 100g", "Lớp phấn dày quả to cùi đỏ ngọt lịm mọng nước"),
    "DaoSaPaVN": ("Trái đào Sa Pa lông tơ má đào", "🍑", "39 kcal / 100g", "Vỏ má đào ửng hồng thịt giòn ngọt thanh ôn đới"),
    "LeLaoCai": ("Trái lê Lào Cai (Lê tuyết vùng cao)", "🍐", "42 kcal / 100g", "Thịt trắng ngần mọng nước giải nhiệt mùa thu"),
    "LeTaiNung": ("Trái lê Tai Nung Đài Loan trồng Tây Bắc", "🍐", "44 kcal / 100g", "Vỏ nâu cát quả tròn giòn ngọt thanh tao"),
    "MacCaDakLak": ("Trái mắc ca Đắk Lắk tươi vỏ xanh", "🟢", "718 kcal / 100g hạt", "Hoàng đế hạt khô vỏ xanh bọc hạt béo ngậy"),
    "DieuDaoLonHotVN": ("Trái điều (Đào lộn hột) Bình Phước", "🔴", "45 kcal / 100g", "Thủ phủ điều Bình Phước quả mọng ngọt chát"),
    "DieuRungVN": ("Trái điều rừng hoang dã", "🟡", "46 kcal / 100g", "Quả nhỏ màu vàng đỏ mọng nước rừng tự nhiên"),
    "DauDaXoan": ("Trái dâu da xoan chùm quả đỏ", "🔴", "48 kcal / 100g", "Từng chùm đỏ rực vị chua thanh giải khát"),
    "DauDaDatVN": ("Trái dâu da đất Chu Lai Quảng Nam", "🔴", "50 kcal / 100g", "Mọc quanh thân cây vị chua ngọt đậm đà"),
    "DauTamVN": ("Trái dâu tằm tươi Đà Lạt", "🟣", "43 kcal / 100g", "Tím đen ngâm siro mát lạnh giàu chất chống lão hóa"),
    "VaiThieuLucNgan": ("Trái vải thiều Lục Ngạn Bắc Giang", "🔴", "66 kcal / 100g", "Cùi dày trắng ngần hạt tiêu ngọt sắc thơm nức"),
    "NhanLongHungYenVN": ("Trái nhãn lồng Hưng Yên tiến vua", "👁️", "60 kcal / 100g", "Cùi dày múi mọng giòn rụm thơm ngát nức tiếng"),
    "NhanTieuDaBoVN": ("Trái nhãn tiêu da bò miền Tây", "👁️", "59 kcal / 100g", "Vỏ da bò vàng bóng ngọt đậm mọng nước"),
    "ChomChomJavaVN": ("Trái chôm chôm Java cùi giòn", "🔴", "70 kcal / 100g", "Gai dài mềm mại vị chua ngọt thanh mát"),
    "ChomChomNhanVN": ("Trái chôm chôm nhãn đường phèn", "🔴", "75 kcal / 100g", "Cơm tróc róc giòn ngọt như đường phèn"),
    "BonBonQuangNamVN": ("Trái bòn bon (Lòn bon Quảng Nam)", "🟡", "65 kcal / 100g", "Vỏ mỏng múi mọng trong suốt ngọt thanh mát"),
    "MangCutLaiThieuVN": ("Trái măng cụt Lái Thiêu Bình Dương", "🟣", "73 kcal / 100g", "Vỏ mỏng múi trắng ngần chua ngọt thanh tao"),
    "VuSuaLoRenVN": ("Trái vú sữa Lò Rèn Vĩnh Kim", "⚪", "67 kcal / 100g", "Dòng sữa ngọt ngào thơm mùi sữa mẹ mát lịm"),
    "VuSuaTimVN": ("Trái vú sữa tím vỏ bóng", "🟣", "68 kcal / 100g", "Vỏ tím thắm cơm dẻo ngọt béo ngậy"),
    "VuSuaHoangKimVN": ("Trái vú sữa hoàng kim vỏ vàng", "🟡", "70 kcal / 100g", "Vàng óng ả múi trong như thạch dẻo ngọt"),
    "CocThaiVN": ("Trái cóc Thái giòn ngọt", "🟢", "38 kcal / 100g", "Quả nhỏ ăn sống giòn tan quanh năm"),
    "CocTaVN": ("Trái cóc ta quả to chua thanh", "🟢", "35 kcal / 100g", "Quả to chua giòn làm nước ép và gỏi cóc"),
    "XoaiRungVN": ("Trái xoài rừng hoang dã", "🥭", "55 kcal / 100g", "Quả nhỏ thơm ngát mùi cỏ cây rừng chua ngọt"),
    "MeChuaVN": ("Trái me chua nấu canh chua lá giang", "🟤", "210 kcal / 100g", "Gia vị ẩm thực không thể thiếu của miền Nam"),
    "MeThaiVN": ("Trái me Thái ngọt dẻo", "🟤", "239 kcal / 100g", "Cơm me nâu dẻo quánh ngọt như mứt thiên nhiên"),
    "SauHaNoiVN": ("Trái sấu Hà Nội nấu canh chua", "🟢", "35 kcal / 100g", "Ngâm gừng ớt giải nhiệt phố cổ ngày hè"),
    "TramDenVN": ("Trái trám đen Cao Bằng om tương", "🟣", "145 kcal / 100g", "Om tương béo bùi dẻo quánh đặc sản Đông Bắc"),
    "TramTrangVN": ("Trái trám trắng kho thịt", "🟢", "85 kcal / 100g", "Chua chát bùi ngậy gia vị vùng cao"),
    "QuatHongBiVN": ("Trái quất hồng bì trị ho tiêu đờm", "🟡", "50 kcal / 100g", "Vỏ mỏng hạt xanh thịt quả chua ngọt ấm họng"),
    "SungTaVN": ("Trái sung ta muối chua giòn", "🟢", "40 kcal / 100g", "Sung nếp quả tròn muối chua ăn ốc luộc thịt luộc")
}

def inject_batch5():
    print("=" * 70)
    print("   BẮT ĐẦU ĐỒNG BỘ 100 ĐẶC SẢN TRÁI CÂY THUẦN VIỆT (401 - 500)   ")
    print("=" * 70)

    db = dict(FRUIT_LIBRARY_600)
    added = 0
    for k, (vn_name, icon, cal, ben) in VN_100_BATCH5.items():
        db[k] = {
            "vn_name": vn_name,
            "icon": icon,
            "calories": cal,
            "vitamins": "Vitamin C, A, Kali, chất xơ và các khoáng chất thảo mộc bản địa Việt Nam",
            "benefits": ben,
            "tips": "Đặc sản thuần Việt tươi ngon, thưởng thức đúng mùa vụ để đạt vị ngọt đậm đà nhất.",
            "avg_price_per_kg": 50000
        }
        added += 1

    out_file = os.path.join(PROJECT_ROOT, "src", "fruit_library_600.py")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("# fruit_library_600.py - Thư viện Tri thức Trái cây Toàn cầu Chuẩn hóa\n")
        f.write("FRUIT_LIBRARY_600 = " + json.dumps(db, ensure_ascii=False, indent=4) + "\n")

    print(f"[OK] Đã nạp thành công {added} đặc sản trái cây Việt Nam vào Thư viện!")
    print(f"[*] Tổng số loại trái cây hiện tại trong Thư viện: {len(db)} loại!")

if __name__ == "__main__":
    inject_batch5()

