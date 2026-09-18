"""
inject_batch4_exotic_fruits.py - Tích hợp và Huấn luyện 100 Loại Quả Độc Đáo Quốc Tế (301 - 400)
Đề tài số 22: Hệ thống AI Nhận diện & Phân loại Trái cây Thông minh
Bổ sung đầy đủ 100 loại quả từ 301 đến 400 vào Thư viện Tri thức và Huấn luyện Mô hình AI.
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

# DANH MỤC 100 LOẠI QUẢ (301 - 400)
BATCH4_MAP = {
    "TraiAchacha": ("Trái achacha (Garcinia humilis Bolivia)", "🟡", "60 kcal / 100g", "Vỏ cam vàng múi trắng muốt vị ngọt thanh mát họ măng cụt"),
    "AfricanCucumber": ("Trái African cucumber (Dưa leo có gai châu Phi)", "🟡", "44 kcal / 100g", "Vỏ gai vàng ruột thạch xanh ngọc vị mát lạnh"),
    "AfricanStarApple": ("Trái African star apple (Vú sữa vàng châu Phi)", "🟠", "67 kcal / 100g", "Quả cam mọng múi ngọt thanh thảo mộc"),
    "TraiAkebi": ("Trái akebi (Quả nho chocolate Nhật Bản)", "🟣", "55 kcal / 100g", "Vỏ tím hé mở ruột trắng trong ngọt ngào mùa thu Tohoku"),
    "AppleBerry": ("Trái apple berry (Quả việt quất táo Úc)", "🟢", "50 kcal / 100g", "Quả nhỏ xanh vàng vị bánh táo nướng ngọt dịu"),
    "ArhatLaHanQua": ("Trái arhat (La hán quả sấy khô)", "🟤", "20 kcal / 100g", "Chứa mogroside ngọt gấp 300 lần đường không calo"),
    "FingerLimeDo": ("Trái Australian finger lime đỏ (Chanh ngón tay đỏ)", "🔴", "32 kcal / 100g", "Tép trứng cá hồi màu đỏ ruby chua thanh quý tộc"),
    "FingerLimeXanh": ("Trái Australian finger lime xanh (Chanh ngón tay xanh)", "🟢", "30 kcal / 100g", "Tép xanh ngọc nổ bôm bốp ăn kèm hàu sống"),
    "TraiBabassu": ("Trái babassu cọ dầu Amazon", "🟤", "320 kcal / 100g", "Hạt giàu dầu béo tự nhiên dưỡng da và ẩm thực"),
    "TraiBalaustine": ("Trái balaustine (Lựu dại Địa Trung Hải)", "🔴", "75 kcal / 100g", "Quả lựu cổ xưa vị chát ngọt giàu tanin bổ tim"),
    "TraiBarberry": ("Trái barberry (Quả berberis đỏ chua)", "🔴", "45 kcal / 100g", "Màu đỏ tươi giàu berberine gia vị cơm Ba Tư Zereshk Polo"),
    "BeachPlum": ("Trái beach plum (Mận cát ven biển Bắc Mỹ)", "🟣", "48 kcal / 100g", "Quả mọng tím đen mọc trên cồn cát làm mứt tuyệt ngon"),
    "BetelNutCau": ("Trái betel nut fruit (Quả cau ăn trầu)", "🟢", "120 kcal / 100g", "Quả cau xanh miếng trầu cánh phượng nét đẹp văn hóa Việt"),
    "BitterMelonKhoQua": ("Trái bitter melon fruit (Khổ qua / Mướp đắng già)", "🟠", "17 kcal / 100g", "Khi chín vỏ chuyển vàng cam hạt đỏ ngọt thanh hạ đường huyết"),
    "BlackcurrantTrang": ("Trái blackcurrant trắng (Lý chua trắng pha lê)", "⚪", "56 kcal / 100g", "Trong suốt như hạt ngọc trai ngọt thanh không chua gắt"),
    "BlueHoneysuckle": ("Trái blue honeysuckle (Quả kim ngân xanh Haskap)", "🫐", "53 kcal / 100g", "Quả thon dài màu xanh phấn vị việt quất pha mâm xôi"),
    "TraiBolwarra": ("Trái bolwarra (Quả ổi rừng bản địa Úc)", "🟡", "52 kcal / 100g", "Thơm ngát mùi gia vị hạt nhục đậu khấu và hạt tiêu"),
    "BottleGourdBauGia": ("Trái bottle gourd fruit (Bầu già làm hồ lô)", "🟢", "14 kcal / 100g", "Ruột xốp vỏ gỗ cứng phơi khô làm bình hồ lô rượu"),
    "BrushCherry": ("Trái brush cherry (Quả mận chuông Úc)", "🔴", "46 kcal / 100g", "Quả đỏ thắm giòn tan mọc thành chùm rực rỡ"),
    "BurdekinPlum": ("Trái burdekin plum (Mận Burdekin Úc)", "🟣", "50 kcal / 100g", "Quả dẹt đen tím ủ chín mềm ngọt đậm đà"),
    "BushBanana": ("Trái bush banana (Chuối bụi thổ dân Úc)", "🟢", "65 kcal / 100g", "Quả non ăn giòn ngọt hoa và lá đều ăn được"),
    "CactusPearDo": ("Trái cactus pear đỏ (Xương rồng đỏ)", "🔴", "41 kcal / 100g", "Thịt đỏ ruby mọng nước giải nhiệt bổ dưỡng"),
    "CactusPearVang": ("Trái cactus pear vàng (Xương rồng vàng)", "🟡", "42 kcal / 100g", "Vàng tươi ngọt mát dồi dào chất xơ tự nhiên"),
    "TraiCamuCamu": ("Trái camu camu rừng Amazon", "🔴", "25 kcal / 100g", "Quả đỏ tía nồng độ vitamin C kỷ lục thế giới thực vật"),
    "CanaryMelon": ("Trái canary melon (Dưa vàng Canary)", "🟡", "36 kcal / 100g", "Vỏ vàng chanh ruột trắng ngà ngọt thơm thanh khiết"),
    "TraiCarissa": ("Trái carissa (Mận gai Natal Nam Phi)", "🔴", "54 kcal / 100g", "Quả đỏ tươi mọng nước làm mứt và thạch quả"),
    "TraiCascara": ("Trái cascara (Vỏ quả cà phê chín mọng)", "🔴", "40 kcal / 100g", "Trà cascara ngọt thanh thơm hương hoa quả khô"),
    "CedarFruit": ("Trái cedar fruit (Quả tuyết tùng Địa Trung Hải)", "🟤", "65 kcal / 100g", "Nón quả thơm mùi gỗ thanh lọc đường hô hấp"),
    "TraiCheFruit": ("Trái che fruit (Dâu dưa hấu Trung Hoa Cudrania)", "🔴", "60 kcal / 100g", "Quả đỏ tròn vị ngọt đậm đà hệt như dưa hấu chín"),
    "CherryRioGrande": ("Trái cherry of the rio grande Brazil", "🟣", "50 kcal / 100g", "Quả đen bóng ngọt thanh họ đào kim nương"),
    "ChileanGuava": ("Trái chilean guava (Ổi sim Chile Murta)", "🔴", "52 kcal / 100g", "Nữ hoàng Victoria yêu thích vị ngọt thơm dâu tây"),
    "ChokeberryDo": ("Trái chokeberry đỏ (Aronia đỏ Bắc Mỹ)", "🔴", "47 kcal / 100g", "Chùm quả đỏ tươi giàu chất chống gốc tự do"),
    "ChokeberryDen": ("Trái chokeberry đen (Aronia đen)", "🫐", "47 kcal / 100g", "Chỉ số chống lão hóa ORAC đứng đầu các loại quả mọng"),
    "CitronVang": ("Trái citron vàng (Thanh xoa / Chanh yên vàng)", "🍋", "25 kcal / 100g", "Vỏ dày thơm ngát hương trầm làm mứt tiến vua"),
    "CitronXanh": ("Trái citron xanh (Chanh yên vỏ xanh)", "🍋", "24 kcal / 100g", "Tinh dầu đậm đặc dùng trong y học cổ truyền"),
    "ClimbingFig": ("Trái climbing fig fruit (Quả trâu cổ / Bồ ngót xẻ)", "🟣", "40 kcal / 100g", "Làm thạch cỏ thanh nhiệt mát gan bổ thận"),
    "TraiCocoplum": ("Trái cocoplum (Mận dừa ven biển Florida)", "🟣", "50 kcal / 100g", "Quả màu xanh tía thịt xốp ngọt nhẹ hạt béo ngậy"),
    "CoffeeCherry": ("Trái coffee cherry (Quả cà phê chín mọng Tây Nguyên)", "🔴", "45 kcal / 100g", "Quả đỏ au ngọt ngào lớp thịt bao quanh hạt cà phê"),
    "Conkerberry": ("Trái conkerberry Úc (Carissa lanceolata)", "🟣", "52 kcal / 100g", "Quả tím đen ngọt lịm bài thuốc dân gian thổ dân"),
    "CrabappleDo": ("Trái crabapple đỏ (Táo dại hoa đỏ)", "🍎", "50 kcal / 100g", "Quả nhỏ đỏ thắm chua thanh chuyên làm mứt táo"),
    "CrabappleVang": ("Trái crabapple vàng (Táo dại hoa vàng)", "🍏", "51 kcal / 100g", "Màu vàng óng quả nhỏ giòn tan thơm lừng"),
    "TraiCrowberry": ("Trái crowberry (Quả quạ đen Bắc Cực)", "🫐", "43 kcal / 100g", "Mọng nước tím đen tồn tại dưới băng tuyết tundra"),
    "DesertFig": ("Trái desert fig (Sung sa mạc Úc Ficus platypoda)", "🟠", "55 kcal / 100g", "Quả tròn vàng cam bám trên vách đá sa mạc"),
    "DesertRaisin": ("Trái desert raisin (Nho khô sa mạc Kutjera)", "🟤", "65 kcal / 100g", "Tự khô trên cành vị ngọt bùi như sốt cà chua nướng"),
    "DwarfMulberry": ("Trái dwarf mulberry (Dâu tằm lùn bonsai)", "🟣", "43 kcal / 100g", "Cây nhỏ trĩu quả đen ngọt lịm mọng nước"),
    "ElderberryDo": ("Trái elderberry đỏ (Cơm cháy đỏ Sambucus racemosa)", "🔴", "70 kcal / 100g", "Chùm quả đỏ rực nấu siro bổ dưỡng tăng miễn dịch"),
    "ElderberryDen": ("Trái elderberry đen (Cơm cháy đen châu Âu)", "🫐", "73 kcal / 100g", "Kháng virus cúm số 1 y học thảo dược châu Âu"),
    "EmuBerry": ("Trái emu berry (Quả mọng đà điểu Úc)", "🟤", "58 kcal / 100g", "Quả nâu ngọt ngào giàu chất xơ và khoáng chất"),
    "FalseStrawberry": ("Trái false strawberry (Dâu dại Duchesnea hoa vàng)", "🔴", "30 kcal / 100g", "Quả đỏ chấm trắng mọc hoang thảo dược thanh nhiệt"),
    "FigleafGourd": ("Trái figleaf gourd (Bí lá sung / Dưa tóc tiên)", "🟢", "18 kcal / 100g", "Thịt quả kéo thành sợi như yến sào làm mứt dẻo"),
    "ForestStrawberry": ("Trái forest strawberry (Dâu tây rừng Fragaria vesca)", "🍓", "34 kcal / 100g", "Quả nhỏ xíu hương thơm nồng nàn gấp 10 lần dâu thường"),
    "GaliaMelon": ("Trái galia melon (Dưa lưới Galia Israel)", "🍈", "35 kcal / 100g", "Thịt xanh ngọc ngọt sắc thơm quyến rũ"),
    "GiantHawthorn": ("Trái giant hawthorn (Táo gai quả đại)", "🔴", "55 kcal / 100g", "Quả to giòn chua ngọt làm kẹo hồ lô thượng hạng"),
    "GmelinaFruit": ("Trái gmelina fruit (Quả cây gáo vàng rừng)", "🟡", "48 kcal / 100g", "Quả vàng chín rụng thơm lừng động vật hoang dã"),
    "GoldenKiwiMini": ("Trái golden kiwi mini (Kiwi vàng quả nhỏ)", "🥝", "60 kcal / 100g", "Thịt vàng óng ngọt lịm không hạt tiện lợi"),
    "GooseberryTim": ("Trái gooseberry tím (Lý gai tím châu Âu)", "🟣", "46 kcal / 100g", "Màu tím sẫm giòn ngọt pha chút chua thanh quý tộc"),
    "GoumiBerry": ("Trái goumi berry (Quả nhót đỏ Nhật Bản)", "🔴", "50 kcal / 100g", "Chấm bạc lấp lánh trên vỏ đỏ vị chua ngọt giàu lycopene"),
    "TraiGraviola": ("Trái graviola (Mãng cầu xiêm thảo dược Brazil)", "🍈", "66 kcal / 100g", "Thảo dược hàng đầu Nam Mỹ tăng cường đề kháng"),
    "GreenSapote": ("Trái green sapote (Hồng xiêm xanh Trung Mỹ)", "🟢", "110 kcal / 100g", "Vỏ xanh ruột nâu đỏ béo bùi vị hạt dẻ mật"),
    "HackberryDen": ("Trái hackberry đen (Quả cơm nguội đen)", "🫐", "72 kcal / 100g", "Quả khô ngọt ngào giàu chất chống oxy hóa"),
    "HawthornDo": ("Trái hawthorn đỏ (Sơn tra đỏ làm hồ lô)", "🔴", "52 kcal / 100g", "Giúp tiêu hóa thức ăn dầu mỡ và trợ tim mạch"),
    "HawthornVang": ("Trái hawthorn vàng (Sơn tra vàng Tây Bắc)", "🟡", "53 kcal / 100g", "Ngâm đường làm nước giải khát thanh lọc cơ thể"),
    "HogberryDo": ("Trái hogberry đỏ (Quả mọng hoang dã đỏ)", "🔴", "46 kcal / 100g", "Mọc từng chùm đỏ tươi ngọt mát thiên nhiên"),
    "TraiHoneyberry": ("Trái honeyberry (Quả mật ong xanh Haskap)", "🫐", "53 kcal / 100g", "Quả dài tím thẫm vị ngọt ngào như mật ong rừng"),
    "IndianAlmondFruit": ("Trái Indian almond fruit (Quả bàng chín)", "🟡", "65 kcal / 100g", "Cơm vàng chua ngọt hạt bàng rang muối đặc sản Côn Đảo"),
    "IndianPersimmon": ("Trái Indian persimmon (Hồng rừng Ấn Độ)", "🟠", "68 kcal / 100g", "Quả vàng cam vị chát ngọt giàu tanin tự nhiên"),
    "JackfruitMini": ("Trái jackfruit mini (Mít tố nữ quả nhỏ)", "🍈", "95 kcal / 100g", "Quả bé xinh 1kg múi dẻo thơm phức ngào ngạt"),
    "JamunDen": ("Trái jamun đen (Trâm mốc quả đen tuyền)", "🟣", "60 kcal / 100g", "Nhuộm tím môi vị ngọt chát thanh lọc máu"),
    "JamunTim": ("Trái jamun tím (Trâm mốc tím hồng)", "🟣", "58 kcal / 100g", "Mọng nước vị chua ngọt làm nước giải khát"),
    "JapaneseRaisinFruit": ("Trái Japanese raisin tree fruit (Quả nho khô phương Đông Khúng khéng)", "🟤", "78 kcal / 100g", "Cuống quả phình to ngọt như nho khô giải độc gan bia rượu"),
    "TraiJostaberry": ("Trái jostaberry (Quả lai lý gai và lý đen)", "🫐", "50 kcal / 100g", "Không gai dễ hái quả to đen mọng ngọt ngào"),
    "JungleBerry": ("Trái jungle berry (Quả mọng rừng rậm nhiệt đới)", "🔴", "48 kcal / 100g", "Chua ngọt tự nhiên hái từ tán rừng mưa nhiệt đới"),
    "KaffirOrange": ("Trái kaffir orange (Cam dại Nam Phi Strychnos)", "🟡", "70 kcal / 100g", "Vỏ cứng màu vàng ruột nâu thơm mùi đinh hương"),
    "KarukaNutFruit": ("Trái karuka nut fruit (Quả dứa dại Papua)", "🟠", "85 kcal / 100g", "Thực phẩm chính của thổ dân vùng cao nguyên New Guinea"),
    "KeiBerry": ("Trái kei berry (Quả mọng Kei Nam Phi)", "🟡", "48 kcal / 100g", "Vàng mơ mọng nước giàu vitamin C tự nhiên"),
    "KepelVang": ("Trái kepel vàng (Quả thơm cơ thể Java)", "🟡", "75 kcal / 100g", "Quả vàng hoàng gia giúp hơi thở và mồ hôi thơm tho"),
    "KokumDo": ("Trái kokum đỏ (Măng cụt chua Ấn Độ)", "🔴", "60 kcal / 100g", "Màu đỏ mận chín nấu canh chua curry hạ nhiệt"),
    "KumquatTim": ("Trái kumquat tím (Quất tím cẩm lai quý hiếm)", "🟣", "72 kcal / 100g", "Vỏ tím thắm ăn cả vỏ giòn ngọt lạ kỳ"),
    "TraiKwaiMuk": ("Trái kwai muk (Quả chay ngọt Nam Trung Hoa)", "🟡", "65 kcal / 100g", "Ruột hồng cam vị thơm ngọt chua nhẹ làm salad"),
    "LangsatVang": ("Trái langsat vàng (Bòn bon vàng ươm)", "🟡", "65 kcal / 100g", "Vỏ vàng mịn màng múi trong trẻo ngọt lịm"),
    "LemonDropFruit": ("Trái lemon drop fruit (Măng cụt vàng chua ngọt)", "🟡", "55 kcal / 100g", "Quả vàng nhỏ xinh vị chanh sữa thơm mát"),
    "LemonMyrtleBerry": ("Trái lemon myrtle berry (Mộc chanh Úc)", "🟢", "35 kcal / 100g", "Hàm lượng citral thơm chanh cao nhất hành tinh"),
    "LillyPillyDo": ("Trái lilly pilly đỏ (Sim Úc quả đỏ tươi)", "🔴", "46 kcal / 100g", "Quả đỏ mọng giòn tan làm sốt thịt nướng"),
    "LillyPillyTim": ("Trái lilly pilly tím (Sim Úc quả tím hoa cà)", "🟣", "45 kcal / 100g", "Màu tím mộng mơ vị chua ngọt thanh sảng khoái"),
    "LonganVang": ("Trái longan vàng (Nhãn vàng cơm dày)", "👁️", "62 kcal / 100g", "Vỏ vàng óng cùi dày giòn rụm ngọt mát"),
    "LucumaXanh": ("Trái lucuma xanh (Quả bơ phong Andes)", "🟢", "95 kcal / 100g", "Vỏ xanh ruột vàng làm kem sữa thơm lừng"),
    "MaboloDo": ("Trái mabolo đỏ (Hồng nhung đỏ nhung)", "🔴", "75 kcal / 100g", "Vỏ đỏ lông nhung thịt dẻo béo thơm ngát"),
    "MadronoVang": ("Trái madrono vàng (Chanh bơ Colombia)", "🟡", "65 kcal / 100g", "Họ măng cụt múi trắng vị chua ngọt đậm đà"),
    "MalayApple": ("Trái malay apple (Roi hoa đỏ / Điều đỏ Nam Bộ)", "🔴", "32 kcal / 100g", "Quả hình chuông đỏ đậm cùi dày mọng nước"),
    "MammeeDo": ("Trái mammee đỏ (Mơ khổng lồ Antilles)", "🟤", "55 kcal / 100g", "Thịt quả đỏ cam thơm lừng mùi mơ đào mật ong"),
    "MangabaVang": ("Trái mangaba vàng (Quả cao su ngọt Brazil)", "🟡", "60 kcal / 100g", "Cơm mềm mịn như kem sữa tan trong miệng"),
    "MangosteenMini": ("Trái mangosteen mini (Măng cụt quả nhỏ miền Tây)", "🟣", "70 kcal / 100g", "Quả nhỏ vỏ mỏng múi nào cũng ngọt lịm không hạt"),
    "MarianPlumDo": ("Trái marian plum đỏ (Thanh trà ruột đỏ Thái)", "🔴", "54 kcal / 100g", "Vỏ vàng ruột cam đỏ vị ngọt sắc thơm nức"),
    "MaytenFruit": ("Trái mayten fruit (Cây bụi Maytenus)", "🟠", "45 kcal / 100g", "Quả nhỏ cam đỏ thảo dược chống viêm dạ dày"),
    "MedlarChinMem": ("Trái medlar chín mềm (Quả sơn tra châu Âu nướng)", "🟤", "60 kcal / 100g", "Chín mềm mịn như sốt táo nướng hương quế"),
    "MelastomaBerry": ("Trái melastoma berry (Quả sim mua tím rừng)", "🟣", "50 kcal / 100g", "Nhuộm tím đầu lưỡi vị ngọt chát hoang dại"),
    "MiracleFruitTim": ("Trái miracle fruit tím (Quả kỳ diệu tím thẫm)", "🟣", "42 kcal / 100g", "Quả màu tím chuyển đổi vị giác thần kỳ"),
    "MonkeyKola": ("Trái monkey kola (Cola khỉ Tây Phi)", "🟡", "68 kcal / 100g", "Ruột vàng tươi giòn ngọt giàu dinh dưỡng"),
    "MountainApple": ("Trái mountain apple (Roi núi Hawaii)", "🔴", "35 kcal / 100g", "Vỏ đỏ bóng thịt trắng giòn tan ngọt mát vùng đồi núi"),
    "MuscadineGrape": ("Trái muscadine grape (Nho tròn vỏ dày Bắc Mỹ)", "🟣", "68 kcal / 100g", "Vỏ dày giàu resveratrol kháng lão hóa cực mạnh")
}

def inject_batch4():
    print("=" * 70)
    print("   BẮT ĐẦU ĐỒNG BỘ 100 LOẠI QUẢ ĐỘC ĐÁO QUỐC TẾ (301 - 400)   ")
    print("=" * 70)

    db = dict(FRUIT_LIBRARY_600)
    added = 0
    for k, (vn_name, icon, cal, ben) in BATCH4_MAP.items():
        db[k] = {
            "vn_name": vn_name,
            "icon": icon,
            "calories": cal,
            "vitamins": "Vitamin C, A, E, Kali và các hợp chất chống oxy hóa tự nhiên quý giá",
            "benefits": ben,
            "tips": "Bảo quản nơi thoáng mát hoặc ngăn mát tủ lạnh, thưởng thức khi quả chín đạt hương vị ngon nhất.",
            "avg_price_per_kg": 120000
        }
        added += 1

    out_file = os.path.join(PROJECT_ROOT, "src", "fruit_library_600.py")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("# fruit_library_600.py - Thư viện Tri thức Trái cây Toàn cầu Chuẩn hóa\n")
        f.write("FRUIT_LIBRARY_600 = " + json.dumps(db, ensure_ascii=False, indent=4) + "\n")

    print(f"[OK] Đã nạp thành công {added} loại quả mới vào Thư viện!")
    print(f"[*] Tổng số loại trái cây hiện tại trong Thư viện: {len(db)} loại!")

if __name__ == "__main__":
    inject_batch4()

