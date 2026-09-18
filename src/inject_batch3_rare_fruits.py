"""
inject_batch3_rare_fruits.py - Tích hợp và Huấn luyện 100 Loại Quả Quý Hiếm Toàn Cầu (201 - 300)
Đề tài số 22: Hệ thống AI Nhận diện & Phân loại Trái cây Thông minh
Bổ sung đầy đủ 100 loại quả nhiệt đới, hoang dã, dược liệu quý theo danh sách 201-300.
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

# DANH MỤC 100 LOẠI QUẢ ĐẶC SẮC (201 - 300)
RARE_100_BATCH3 = {
    "TraiAmbarella": ("Trái ambarella (Cóc tây / cóc ngọt)", "🟢", "48 kcal / 100g", "Quả mọng giòn tan chấm muối ớt giải khát giàu vitamin C"),
    "AraucariaChile": ("Trái araucaria (Hạt thông Chile Piñón)", "🌰", "210 kcal / 100g", "Hạt nón khổng lồ luộc ăn bùi ngậy như hạt dẻ rừng"),
    "TraiBael": ("Trái bael (Mộc táo thảo dược Ấn Độ)", "🟤", "134 kcal / 100g", "Thảo dược linh thiêng Ayurveda thanh lọc tiêu hóa"),
    "TraiBignay": ("Trái bignay (Quả chòi mòi rừng)", "🟣", "52 kcal / 100g", "Từng chùm quả đổi từ đỏ sang tím đen ủ rượu vang thơm ngon"),
    "TraiBiriba": ("Trái biriba (Na gai vàng Rollinia Amazon)", "🟡", "80 kcal / 100g", "Vỏ gai mềm vàng ruột kem sữa ngọt thơm mùi chanh vani"),
    "BreadfruitSaKe": ("Trái breadfruit (Xa-kê bánh mì)", "🍈", "103 kcal / 100g", "Chiên giòn bùi béo hệt như khoai tây chiên giòn"),
    "BushTomato": ("Trái bush tomato (Cà chua bụi sa mạc Úc)", "🟠", "42 kcal / 100g", "Vị khô bùi thơm mùi caramel và hạt nướng gia vị"),
    "CacaoTrang": ("Trái cacao trắng (Theobroma grandiflorum)", "🟤", "90 kcal / 100g", "Thịt quả trắng ngần béo thơm làm bơ cupuacu quý giá"),
    "TraiCalabash": ("Trái calabash (Quả đào tiên phong thủy)", "🟢", "40 kcal / 100g", "Quả tròn nhẵn ngâm rượu bổ dưỡng an thần nhuận tràng"),
    "CamSanhDo": ("Trái cam sành đỏ ruột gấc", "🍊", "48 kcal / 100g", "Vỏ sần múi đỏ rực giàu lycopene chống ung thư"),
    "TraiCapulin": ("Trái capulin (Cherry anh đào Mexico)", "🍒", "58 kcal / 100g", "Quả đỏ đen mọng nước ngọt thanh mọc vùng cao nguyên"),
    "CashewAppleDo": ("Trái cashew apple đỏ (Đào lộn hột đỏ)", "🔴", "45 kcal / 100g", "Mọng nước vị ngọt chát hạt điều béo ngậy treo bên dưới"),
    "CashewAppleVang": ("Trái cashew apple vàng (Đào lộn hột vàng)", "🟡", "46 kcal / 100g", "Quả vàng mọng nước giàu vitamin C gấp 5 lần cam"),
    "CedarBayCherry": ("Trái cedar bay cherry nước Úc", "🔴", "48 kcal / 100g", "Quả nhỏ đỏ tươi vị ngọt thơm hương vị rừng mưa"),
    "TraiCempedak": ("Trái cempedak (Mít tố nữ Mã Lai)", "🍈", "115 kcal / 100g", "Múi vàng dẻo quánh hương thơm nồng nàn hơn mít"),
    "TraiChalta": ("Trái chalta (Quả sổ bà Ấn Độ Elephant apple)", "🟢", "55 kcal / 100g", "Lá đài mọng dày nấu cà ri và làm mứt chua ngọt"),
    "ChayoteFruit": ("Trái chayote fruit (Su su quả già)", "🟢", "19 kcal / 100g", "Chứa nhiều folate và chất xơ xào thịt bò thanh mát"),
    "TraiCloudberry": ("Trái cloudberry (Mâm xôi vàng Bắc Cực)", "🟠", "51 kcal / 100g", "Hổ phách vàng quý hiếm từ đầm lầy tuyết Scandinavia"),
    "CockyApple": ("Trái cocky apple (Táo mào rừng Úc)", "🟢", "46 kcal / 100g", "Thảo dược truyền thống thổ dân giải nhiệt kháng viêm"),
    "CoralBerry": ("Trái coral berry (Quả san hô đỏ)", "🔴", "38 kcal / 100g", "Từng chùm hạt đỏ tươi lấp lánh như chuỗi ngọc"),
    "DesertQuandong": ("Trái desert quandong (Đào sa mạc Tây Úc)", "🔴", "75 kcal / 100g", "Quả đỏ thẫm giàu vitamin C và chất chống gốc tự do"),
    "DurianDoSabah": ("Trái durian đỏ (Sầu riêng ruột đỏ Sabah)", "🔴", "165 kcal / 100g", "Ruột đỏ như gấc vị bùi béo đậm đà quý hiếm đảo Borneo"),
    "TraiEggfruit": ("Trái eggfruit (Lêkima / Quả trứng gà)", "🟡", "138 kcal / 100g", "Thịt vàng ươm dẻo quánh bùi ngậy như lòng đỏ trứng"),
    "EmuApple": ("Trái emu apple (Táo đà điểu Úc)", "🟣", "50 kcal / 100g", "Quả đốm tím vị chua thanh ngọt hậu thảo mộc"),
    "FalseMastic": ("Trái false mastic rừng nhiệt đới", "🟠", "60 kcal / 100g", "Quả vàng cam dẻo ngọt thức ăn của muông thú rừng"),
    "FigDoSweet": ("Trái fig đỏ (Sung ngọt đỏ Địa Trung Hải)", "🔴", "74 kcal / 100g", "Mật dẻo quánh thơm lừng thịt đỏ hồng ngọt lịm"),
    "FigXanhKadota": ("Trái fig xanh (Sung ngọt Kadota vỏ xanh)", "🟢", "72 kcal / 100g", "Vỏ xanh ruột vàng hổ phách ngọt thanh mọng nước"),
    "GacFruitChin": ("Trái gac fruit chín (Quả gấc nếp đỏ au)", "🔴", "105 kcal / 100g", "Vua hàm lượng lycopene và beta-carotene tự nhiên"),
    "GiantGranadilla": ("Trái giant granadilla (Chanh dây khổng lồ)", "🟢", "55 kcal / 100g", "Quả nặng 1-2kg cùi dày ngọt mát hạt bọc thạch"),
    "GoldenApple": ("Trái golden apple (Cóc ngọt Nam Bộ)", "🟡", "48 kcal / 100g", "Vỏ vàng ươm giòn tan ngọt thanh mùa thu"),
    "GovernorsPlum": ("Trái governor’s plum (Mận rừng Madagascar)", "🟣", "50 kcal / 100g", "Quả tím đỏ vị chua ngọt làm mứt và thạch quả"),
    "TraiGreengage": ("Trái greengage (Mận xanh Reine Claude)", "🟢", "50 kcal / 100g", "Mận quý tộc Pháp ngọt như mật ong không hề chát"),
    "Guavaberry": ("Trái guavaberry (Rumberry Caribbean)", "🟤", "65 kcal / 100g", "Ngâm rượu rum hương vị giáng sinh vùng Saint Martin"),
    "HardyKiwi": ("Trái hardy kiwi (Kiwi berry tí hon không lông)", "🥝", "55 kcal / 100g", "Ăn cả vỏ như quả nho ngọt lịm mọng nước"),
    "HogBerry": ("Trái hog berry rừng nhiệt đới", "🔴", "45 kcal / 100g", "Quả nhỏ đỏ mọng giàu khoáng chất vi lượng"),
    "IllawarraPlum": ("Trái illawarra plum (Thông mận Úc)", "🟣", "42 kcal / 100g", "Thịt quả mọng tím mọc trên đế hạt thông độc đáo"),
    "IndianFig": ("Trái Indian fig (Lưỡi long xương rồng Ấn Độ)", "🟣", "41 kcal / 100g", "Ngọt mát như dưa hấu hạ đường huyết hữu hiệu"),
    "IndianJujube": ("Trái Indian jujube (Táo ta giòn ngọt)", "🟢", "45 kcal / 100g", "Quả tròn xanh giòn tan chấm muối ớt quen thuộc"),
    "JungleJalebi": ("Trái jungle jalebi (Me nước / Quả me keo)", "🟤", "110 kcal / 100g", "Vỏ xoắn tròn thịt trắng bùi béo ngọt thanh"),
    "TraiKabosu": ("Trái kabosu Nhật Bản chua dịu", "🍋", "32 kcal / 100g", "Vắt lên sashimi và cá nướng thơm mát thanh nhã"),
    "KaffirLimeBerry": ("Trái kaffir lime berry (Quả chúc chín mọng)", "🍋", "32 kcal / 100g", "Tinh dầu nồng nàn thảo mộc Đông Nam Á"),
    "TraiKaronda": ("Trái karonda (Quả si-rô ngâm đường)", "🔴", "54 kcal / 100g", "Đỏ hồng rực rỡ làm siro đỏ thắm giải khát ngày hè"),
    "TraiKetembilla": ("Trái ketembilla (Mận Ceylon Sri Lanka)", "🟣", "48 kcal / 100g", "Vỏ nhung tím thịt mọng đỏ làm thạch tuyệt ngon"),
    "TraiKokum": ("Trái kokum (Măng cụt Garcinia Ấn Độ)", "🟣", "60 kcal / 100g", "Vỏ tím phơi khô nấu nước mát Kokum Sharbat hạ sốt"),
    "TraiKorlan": ("Trái korlan (Trường chua rừng Tây Bắc)", "🔴", "68 kcal / 100g", "Họ chôm chôm quả nhỏ gai mềm chua ngọt đậm đà"),
    "LangsatRung": ("Trái langsat rừng hoang dã", "🟡", "60 kcal / 100g", "Từng chùm múi trong suốt thanh mát mọc tự nhiên"),
    "LemonDropMangosteen": ("Trái lemon drop mangosteen (Măng cụt chanh)", "🟡", "55 kcal / 100g", "Vàng tươi vị chua ngọt sảng khoái mùi chanh bơ"),
    "LillyPilly": ("Trái lilly pilly (Sim nước Úc)", "🟣", "45 kcal / 100g", "Hồng tím giòn rụm chua thanh làm mứt bushfood"),
    "LonganRung": ("Trái longan rừng (Nhãn rừng hạt to)", "👁️", "55 kcal / 100g", "Cùi mỏng vị ngọt dịu hái từ rừng đại ngàn"),
    "LoquatDo": ("Trái loquat đỏ (Tỳ bà ruột đỏ)", "🟠", "49 kcal / 100g", "Ruột cam đỏ ngọt đậm bổ phổi giảm ho"),
    "LucumaVang": ("Trái lucuma vàng tươi Peru", "🟡", "99 kcal / 100g", "Siêu thực phẩm vàng vị kem bơ phong mạch nha"),
    "MacadamiaFruit": ("Trái macadamia fruit (Mắc ca quả tươi)", "🟢", "718 kcal / 100g hạt", "Vỏ xanh bọc hạt hoàng đế béo ngậy giàu Omega-7"),
    "TraiMadrono": ("Trái madrono chanh bơ Colombia", "🟡", "65 kcal / 100g", "Họ măng cụt múi trắng vị chua ngọt thơm lừng"),
    "MalabarPlum": ("Trái malabar plum (Trâm mốc Java mọng nước)", "🟣", "60 kcal / 100g", "Tím đen mọng nước nhuộm tím đầu lưỡi tuổi thơ"),
    "TraiMamoncillo": ("Trái mamoncillo (Genip quả xanh)", "🟢", "58 kcal / 100g", "Vỏ mỏng ruột cam dẻo ngậm chua ngọt giải khát"),
    "TraiMangaba": ("Trái mangaba thơm nức Brazil", "🟡", "60 kcal / 100g", "Cơm mềm mịn như kem sữa thơm nồng nàn"),
    "MangosteenRung": ("Trái mangosteen rừng (Măng cụt rừng)", "🟣", "70 kcal / 100g", "Vỏ dày múi trắng chua thanh hoang dã tự nhiên"),
    "MarianPlum": ("Trái marian plum (Thanh trà Thái Mayongchid)", "🟠", "52 kcal / 100g", "Quả to vàng cam ngọt lịm thơm nức mũi"),
    "TraiMelinjo": ("Trái melinjo (Hạt gắm bùi Tây Nguyên)", "🔴", "160 kcal / 100g", "Quả đỏ luộc ăn béo ngậy làm bánh phồng emping"),
    "MiracleTomato": ("Trái miracle tomato (Cà chua kỳ diệu ngọt mát)", "🍅", "25 kcal / 100g", "Hàm lượng đường tự nhiên cao ăn ngọt như táo"),
    "MonkeyOrange": ("Trái monkey orange (Cam khỉ châu Phi)", "🟡", "70 kcal / 100g", "Vỏ gỗ cứng đập ra ruột vàng thơm vị đinh hương"),
    "MountainPepperBerry": ("Trái mountain pepper berry Tasmania", "🟣", "65 kcal / 100g", "Tiêu rừng vị quả mọng cay nồng thảo mộc"),
    "TraiMuntries": ("Trái muntries (Táo bụi đất nước Úc)", "🟢", "50 kcal / 100g", "Quả nhỏ đỏ xanh thơm ngọt mùi bánh táo nướng"),
    "NashiDo": ("Trái nashi đỏ (Lê cát đỏ Nhật Bản)", "🍐", "48 kcal / 100g", "Quả tròn vỏ nâu đỏ mọng nước ngọt lịm"),
    "NashiXanh": ("Trái nashi xanh (Lê cát xanh Nijisseiki)", "🍐", "45 kcal / 100g", "Vỏ xanh mướt giòn rôm rốp ngọt mát"),
    "NativeCurrant": ("Trái native currant (Lý gai bản địa Úc)", "🫐", "48 kcal / 100g", "Chùm quả tím mọng nước giàu vitamin C"),
    "NipaPalmFruit": ("Trái nipa palm fruit (Dừa nước ngọt lành)", "🥥", "40 kcal / 100g", "Cơm dừa nước dẻo dai mát rượi sông nước miền Tây"),
    "OilFruitElaeagnus": ("Trái oil fruit (Quả nhót dầu Nga)", "🔴", "75 kcal / 100g", "Quả đỏ ánh bạc giàu axit béo omega quý"),
    "OtaheiteGooseberry": ("Trái otaheite gooseberry (Chùm ruột chua)", "🟢", "30 kcal / 100g", "Múi khía xanh giòn ngâm mắm đường ớt"),
    "TraiPacay": ("Trái pacay (Đậu kem Inga ruột bông tuyết)", "🟢", "60 kcal / 100g", "Quả đậu dài bóc ra cơm bông trắng vị kem sữa"),
    "PandanBerry": ("Trái pandan berry (Quả mọng hương dứa dại)", "🟠", "58 kcal / 100g", "Thơm nức mùi lá dứa tự nhiên ngọt thanh"),
    "PawpawMy": ("Trái pawpaw Mỹ (Na chuối Asimina triloba)", "🟡", "80 kcal / 100g", "Thịt kem vàng óng vị tổng hòa chuối xoài vani"),
    "PeanutButterFruit": ("Trái peanut butter fruit (Bơ đậu phộng)", "🔴", "90 kcal / 100g", "Màu đỏ cam thịt dẻo vị hệt bơ lạc đậu phộng"),
    "TraiPequi": ("Trái pequi vàng rực rỡ Brazil", "🟡", "130 kcal / 100g", "Hương vị nồng nàn độc đáo nấu cơm gà pequi"),
    "PersianLime": ("Trái persian lime (Chanh Ba Tư vỏ nhẵn)", "🍋", "30 kcal / 100g", "Nhiều nước không hạt chuyên pha chế cocktail"),
    "PigeonPlum": ("Trái pigeon plum (Mận bồ câu ven biển)", "🟣", "55 kcal / 100g", "Quả tím đỏ mọng nước ngọt chát nhẹ"),
    "PindoPalmFruit": ("Trái pindo palm fruit (Quả thốt nốt thạch)", "🟠", "65 kcal / 100g", "Quả vàng cam vị dứa chuối làm thạch jelly"),
    "PituriFruit": ("Trái pituri fruit cây bụi sa mạc", "🟢", "45 kcal / 100g", "Thảo dược bản địa thổ dân Úc"),
    "TraiPlumcot": ("Trái plumcot (Mận lai mơ Prunus)", "🔴", "50 kcal / 100g", "Lai giữa mận và mơ thịt đỏ giòn ngọt đậm"),
    "PomegranateTrang": ("Trái pomegranate trắng (Lựu trắng Bạch ngọc)", "🍎", "78 kcal / 100g", "Hạt lựu trắng trong veo ngọt thanh không chua"),
    "PulasanDo": ("Trái pulasan đỏ (Chôm chôm rừng đỏ rực)", "🔴", "76 kcal / 100g", "Gai ngắn cơm dày tróc hạt ngọt sắc"),
    "QuandongSaMac": ("Trái quandong sa mạc (Đào rừng Úc)", "🔴", "75 kcal / 100g", "Vỏ đỏ ruby thịt thơm dẻo giàu chất chống oxy hóa"),
    "RimuBerry": ("Trái rimu berry rừng New Zealand", "🔴", "50 kcal / 100g", "Quả mọng nhỏ màu đỏ trên cành thông cổ thụ"),
    "RoseAppleDo": ("Trái rose apple đỏ (Roi đỏ / Mận đỏ miền Nam)", "🍎", "30 kcal / 100g", "Quả hình chuông đỏ tươi giòn tan nhiều nước"),
    "RoseAppleTrang": ("Trái rose apple trắng (Roi trắng mọng nước)", "⚪", "28 kcal / 100g", "Trắng ngà giòn ngọt giải khát tức thì"),
    "SafouChauPhi": ("Trái safou (Mận bơ châu Phi)", "🟣", "230 kcal / 100g", "Nướng ăn béo ngậy như bơ gọi là bơ của người nghèo"),
    "SandpaperFig": ("Trái sandpaper fig (Sung lá nhám Úc)", "🟣", "50 kcal / 100g", "Quả đen mọng ngọt mọc hoang dã ven suối"),
    "SantolDo": ("Trái santol đỏ (Sấu đỏ Thái Lan)", "🔴", "55 kcal / 100g", "Cơm mềm như bông xốp vị chua ngọt đậm"),
    "SantolVang": ("Trái santol vàng (Sấu vàng ngọt)", "🟡", "58 kcal / 100g", "Vỏ vàng mịn múi mọng ngọt ngào"),
    "SeaBuckthornCam": ("Trái sea buckthorn (Hắc mai biển vàng cam)", "🟠", "82 kcal / 100g", "Siêu quả vitamin C tái tạo và làm sáng da"),
    "SeaGrape": ("Trái sea grape (Nho biển Coccoloba)", "🟣", "60 kcal / 100g", "Từng chùm quả ven biển chín tím ăn sống hoặc làm mứt"),
    "SloeBerry": ("Trái sloe berry (Mận gai ngâm rượu Sloe Gin)", "🟣", "52 kcal / 100g", "Tím đen phủ phấn trắng ủ rượu Gin truyền thống Anh"),
    "SnowberryTrang": ("Trái snowberry (Quả mọng tuyết trắng muốt)", "⚪", "35 kcal / 100g", "Trắng như tuyết mọc mùa đông vùng ôn đới"),
    "TraiSoncoya": ("Trái soncoya (Na gai tím Trung Mỹ)", "🟤", "82 kcal / 100g", "Gai nhọn ruột cam thơm ngọt đậm đà"),
    "SorbApple": ("Trái sorb apple (Táo dại châu Âu cổ)", "🍎", "65 kcal / 100g", "Chín thơm vào mùa thu chuyên làm rượu vang táo"),
    "SpanishLime": ("Trái spanish lime (Mamoncillo chanh Tây Ban Nha)", "🟢", "58 kcal / 100g", "Vỏ xanh ruột cam mọng nước chua ngọt"),
    "StrawberryGuava": ("Trái strawberry guava (Ổi dâu tây đỏ)", "🔴", "55 kcal / 100g", "Quả tròn đỏ mọng vị ổi thơm ngát mùi dâu tây"),
    "SugarPalmFruit": ("Trái sugar palm fruit (Thốt nốt dẻo ngọt)", "⚪", "87 kcal / 100g", "Múi thạch dẻo ngọt ngào giải nhiệt ngày hè"),
    "SyzygiumBerry": ("Trái syzygium berry (Quả mận sim Úc)", "🟣", "46 kcal / 100g", "Màu tím hồng vị chua thanh giàu chất chống lão hóa"),
    "VelvetAppleMabolo": ("Trái velvet apple (Hồng nhung lông tơ đỏ)", "🔴", "75 kcal / 100g", "Vỏ đỏ lông tơ thịt quả dẻo thơm ngào ngạt")
}

def inject_batch3():
    print("=" * 70)
    print("   BẮT ĐẦU ĐỒNG BỘ 100 LOẠI QUẢ QUÝ HIẾM TOÀN CẦU (201 - 300)   ")
    print("=" * 70)

    db = dict(FRUIT_LIBRARY_600)
    added = 0
    for k, (vn_name, icon, cal, ben) in RARE_100_BATCH3.items():
        db[k] = {
            "vn_name": vn_name,
            "icon": icon,
            "calories": cal,
            "vitamins": "Vitamin C, E, Axit béo tự nhiên và các vi khoáng chất chống oxy hóa cao",
            "benefits": ben,
            "tips": "Bảo quản nơi khô mát hoặc ngăn mát tủ lạnh, thưởng thức khi quả chín đạt hương vị thơm ngon nhất.",
            "avg_price_per_kg": 110000
        }
        added += 1

    out_file = os.path.join(PROJECT_ROOT, "src", "fruit_library_600.py")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("# fruit_library_600.py - Thư viện Tri thức Trái cây Toàn cầu Chuẩn hóa\n")
        f.write("FRUIT_LIBRARY_600 = " + json.dumps(db, ensure_ascii=False, indent=4) + "\n")

    print(f"[OK] Đã nạp thành công {added} loại quả mới vào Thư viện!")
    print(f"[*] Tổng số loại trái cây hiện tại trong Thư viện: {len(db)} loại!")

if __name__ == "__main__":
    inject_batch3()

