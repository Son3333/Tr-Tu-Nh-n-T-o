"""
inject_batch2_exotic_fruits.py - Tích hợp và Huấn luyện 100 Loại Quả Độc Đáo Quốc Tế (101 - 200)
Đề tài số 22: Hệ thống AI Nhận diện & Phân loại Trái cây Thông minh
Bổ sung đầy đủ 100 loại quả nhiệt đới, dại, hiếm có trên thế giới theo danh sách 101-200.
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

# DANH MỤC 100 LOẠI QUẢ HIẾM QUỐC TẾ (101 - 200)
EXOTIC_100_BATCH2 = {
    "TraiAbiu": ("Trái abiu (Vú sữa hoàng kim Nam Mỹ)", "🟡", "70 kcal / 100g", "Vỏ vàng óng ả, thịt trong suốt mềm ngọt như thạch caramen"),
    "TraiAcerola": ("Trái acerola (Sơ ri Barbados)", "🔴", "32 kcal / 100g", "Vua vitamin C tự nhiên cao gấp 30 lần cam chanh"),
    "TraiAckee": ("Trái ackee quốc quả Jamaica", "🟡", "150 kcal / 100g", "Thịt quả màu vàng kem xào cá muối trứ danh vùng Caribbean"),
    "TraiAraza": ("Trái araza rừng Amazon", "🟡", "30 kcal / 100g", "Họ ổi thơm ngát làm nước ép và sinh tố chua dịu tuyệt hảo"),
    "TraiAtemoya": ("Trái atemoya (Na dứa lai Đài Loan)", "🍈", "94 kcal / 100g", "Lai giữa na dai và cherimoya, dai dẻo thơm hương dứa"),
    "TraiBabaco": ("Trái babaco đu đủ núi không hạt", "🟡", "25 kcal / 100g", "Quả 5 cạnh mọng nước sủi tăm vị dâu tây dứa đu đủ"),
    "TraiBacuri": ("Trái bacuri rừng Amazon", "🟡", "85 kcal / 100g", "Hương thơm quyến rũ bậc nhất Brazil thịt trắng ngần"),
    "TraiBarbadine": ("Trái barbadine (Chanh dây khổng lồ)", "🟢", "55 kcal / 100g", "Quả chanh dây to bằng quả dưa hấu cơm dày nấu canh"),
    "TraiBilimbi": ("Trái bilimbi (Khế tàu chua)", "🟢", "22 kcal / 100g", "Mọc từng chùm quanh thân cây chuyên nấu canh chua Nam Bộ"),
    "TraiBlackSapote": ("Trái black sapote (Hồng socola)", "🟢", "65 kcal / 100g", "Ruột đen sánh dẻo vị hệt bánh pudding socola ngọt ngào"),
    "TraiCanistel": ("Trái canistel (Quả trứng gà / Lêkima)", "🟡", "138 kcal / 100g", "Thịt vàng ươm bùi béo ngọt đậm như lòng đỏ trứng"),
    "CarambolaDo": ("Trái carambola đỏ (Khế đỏ rừng)", "🔴", "32 kcal / 100g", "Màu đỏ tía lạ mắt múi sao 5 cánh chua ngọt thanh"),
    "TraiCherimoya": ("Trái cherimoya na kem dãy Andes", "🍈", "75 kcal / 100g", "Được Mark Twain ca ngợi là loại quả ngon nhất trần gian"),
    "TraiCupuacu": ("Trái cupuacu cacao trắng Amazon", "🟤", "90 kcal / 100g", "Họ cacao thịt trắng béo ngậy thơm mùi dứa và socola"),
    "CurrantDo": ("Trái currant đỏ (Lý chua đỏ châu Âu)", "🔴", "56 kcal / 100g", "Từng chùm hạt ngọc đỏ mọng nước trang trí bánh Pháp"),
    "CurrantDen": ("Trái currant đen (Cassis châu Âu)", "🫐", "63 kcal / 100g", "Màu tím đen sản xuất rượu mùi Crème de Cassis nổi tiếng"),
    "TraiDamson": ("Trái damson mận đen Anh Quốc", "🟣", "46 kcal / 100g", "Vỏ đen ánh xanh chuyên làm mứt mận và rượu Gin Damson"),
    "DesertLime": ("Trái desert lime (Chanh sa mạc Úc)", "🍋", "30 kcal / 100g", "Chịu hạn sa mạc quả nhỏ chua thanh thơm mát"),
    "TraiFeijoa": ("Trái feijoa (Ổi dứa New Zealand)", "🟢", "55 kcal / 100g", "Mùi thơm nức mũi tổng hòa của ổi dứa và bạc hà"),
    "TraiGacilla": ("Trái gacilla quả mọng nhiệt đới", "🔴", "45 kcal / 100g", "Quả mọng hoang dã giàu chất chống oxy hóa"),
    "TraiGenip": ("Trái genip (Mamoncillo Tây Ban Nha)", "🟢", "58 kcal / 100g", "Vỏ xanh ruột cam dẻo quánh ngậm chua ngọt giải khát"),
    "TraiGrumichama": ("Trái grumichama (Cherry Brazil)", "🟣", "50 kcal / 100g", "Quả đen tím mọng nước vị tương tự quả anh đào ngọt"),
    "TraiHackberry": ("Trái hackberry (Quả cơm nguội rừng)", "🟤", "70 kcal / 100g", "Quả khô ngọt ngào giàu canxi thức ăn thổ dân"),
    "TraiHuckleberry": ("Trái huckleberry núi Bắc Mỹ", "🫐", "55 kcal / 100g", "Quả mọng tím đen biểu tượng vùng núi Rocky"),
    "TraiImbe": ("Trái imbe (Măng cụt châu Phi)", "🟠", "60 kcal / 100g", "Vỏ cam sáng vị chua ngọt thanh nhiệt mùa khô"),
    "TraiJaboticaba": ("Trái jaboticaba (Nho thân gỗ Brazil)", "🟣", "50 kcal / 100g", "Mọc chi chít trên thân gỗ cổ thụ ngọt lịm như rượu vang"),
    "TraiJambul": ("Trái jambul (Trâm mốc Ấn Độ / Java plum)", "🟣", "60 kcal / 100g", "Màu tím đen hỗ trợ hạ đường huyết cực tốt"),
    "TraiJuneberry": ("Trái juneberry (Saskatoon berry)", "🫐", "58 kcal / 100g", "Quả mọng ngọt ngào thu hoạch vào tháng 6 ở Canada"),
    "KeiApple": ("Trái kei apple châu Phi gai nhọn", "🟡", "48 kcal / 100g", "Vàng mơ mọng nước vị chua thanh làm mứt thượng hạng"),
    "TraiKepel": ("Trái kepel hoàng gia Java Indonesia", "🟤", "75 kcal / 100g", "Thảo dược quý giúp cơ thể tỏa hương hoa tự nhiên"),
    "TraiLangsat": ("Trái langsat bòn bon vỏ mỏng", "🟡", "65 kcal / 100g", "Múi trong suốt không nhựa dính vị ngọt thanh mát"),
    "TraiLucuma": ("Trái lucuma vàng dãy Andes Peru", "🟡", "99 kcal / 100g", "Thịt vàng dẻo vị kem caramel phong mạch nha"),
    "TraiLongkong": ("Trái longkong Thái Lan cao cấp", "🟡", "68 kcal / 100g", "Chùm quả dày đặc không mủ ngọt lịm mọng nước"),
    "MammeeApple": ("Trái mammee apple (Mơ Santo Domingo)", "🟤", "51 kcal / 100g", "Quả to da nâu thịt vàng cam giòn ngọt mùi quả mơ"),
    "MameySapote": ("Trái mamey sapote hồng xiêm khổng lồ", "🟤", "124 kcal / 100g", "Ruột đỏ cam béo ngậy vị khoai lang mật hạnh nhân"),
    "TraiMarang": ("Trái marang tarap đảo Borneo", "🟤", "85 kcal / 100g", "Gai mềm múi trắng muốt thơm lừng mềm như tuyết"),
    "TraiMedlar": ("Trái medlar châu Âu thời Trung cổ", "🟤", "60 kcal / 100g", "Ăn khi chín nẫu mềm mịn như sốt táo nướng quế"),
    "MiracleFruit": ("Trái miracle fruit (Quả kỳ diệu)", "🔴", "40 kcal / 100g", "Chứa miraculin biến đồ chua cay thành ngọt lịm tức thì"),
    "MonsteraDeliciosa": ("Trái monstera deliciosa (Trái trầu bà xẻ)", "🟢", "75 kcal / 100g", "Vỏ vảy lục giác thịt chín vị tổng hợp chuối dứa xoài"),
    "MountainSoursop": ("Trái mountain soursop (Mãng cầu núi)", "🍈", "60 kcal / 100g", "Mọc vùng núi cao vị chua thanh dịu mát"),
    "TraiNance": ("Trái nance vàng Trung Mỹ", "🟡", "73 kcal / 100g", "Quả tròn vàng ươm mùi pho mát ngọt lên men"),
    "TraiNoni": ("Trái noni (Quả nhàu trị đau khớp)", "🟢", "40 kcal / 100g", "Thảo dược quý ngâm đường hoặc phơi khô trị đau lưng"),
    "OilPalmFruit": ("Trái oil palm fruit (Cọ dầu châu Phi)", "🟠", "540 kcal / 100g", "Chùm quả đỏ cam chiết xuất dầu cọ giàu vitamin E"),
    "TraiPejibaye": ("Trái pejibaye (Cọ đào đào lộn hột)", "🟠", "190 kcal / 100g", "Luộc ăn béo bùi như hạt dẻ giàu tinh bột tự nhiên"),
    "TraiPitanga": ("Trái pitanga (Khế đỏ Surinam cherry)", "🔴", "33 kcal / 100g", "Hình khía múi đỏ rực vị thơm chua ngọt kì lạ"),
    "TraiPitomba": ("Trái pitomba rừng rậm Amazon", "🟡", "45 kcal / 100g", "Màu vàng óng ả thơm ngát mùi chanh dây và mơ"),
    "PlantainDo": ("Trái plantain đỏ (Chuối ngự đỏ luộc)", "🍌", "122 kcal / 100g", "Vỏ đỏ thẫm chuyên nấu nướng chiên xào Nam Mỹ"),
    "TraiPulasan": ("Trái pulasan râu ngắn Malaysia", "🔴", "76 kcal / 100g", "Họ chôm chôm quả to cùi dày hạt giòn ăn được"),
    "TraiQuandong": ("Trái quandong (Đào sa mạc Úc)", "🔴", "75 kcal / 100g", "Quả đỏ tươi giàu chất sắt thảo dược thổ dân"),
    "TraiRambai": ("Trái rambai dâu da đất rừng", "🟡", "52 kcal / 100g", "Từng chùm quả dài múi mọng chua ngọt thanh tao"),
    "RedMombin": ("Trái red mombin (Cóc đỏ Jocote)", "🔴", "60 kcal / 100g", "Màu đỏ mận chín chấm muối ăn vặt Trung Mỹ"),
    "SalakRan": ("Trái salak (Quả mây da rắn Indonesia)", "🟤", "82 kcal / 100g", "Vỏ vảy rắn thịt giòn rụm thơm mùi dứa sầu riêng"),
    "TraiSantol": ("Trái santol (Sấu đỏ Thái Lan)", "🟡", "55 kcal / 100g", "Cơm mềm như bông xốp chua ngọt đậm đà"),
    "SapodillaDen": ("Trái sapodilla đen (Black sapote)", "🟢", "65 kcal / 100g", "Vỏ xanh ruột đen sô-cô-la ngọt lành"),
    "Serviceberry": ("Trái serviceberry (Juneberry Bắc Mỹ)", "🫐", "60 kcal / 100g", "Quả mọng tím sẫm làm bánh pie thơm lừng"),
    "SoursopNui": ("Trái soursop núi (Mãng cầu xiêm rừng)", "🍈", "62 kcal / 100g", "Vỏ gai mềm chua thanh chống oxy hóa tế bào"),
    "SugarAppleTim": ("Trái sugar apple tím (Na tím hoàng gia)", "🟣", "95 kcal / 100g", "Vỏ tím thắm mắt nở đều cùi dai thơm ngọt"),
    "SurinamCherry": ("Trái surinam cherry khía múi đỏ", "🔴", "33 kcal / 100g", "Chua ngọt thơm tinh dầu bổ sung vitamin C"),
    "TraiTamarillo": ("Trái tamarillo (Cà chua thân gỗ)", "🔴", "35 kcal / 100g", "Vỏ đỏ cam chua thanh độc đáo giàu vitamin A E"),
    "TraiTayberry": ("Trái tayberry Scotland quả dài", "🔴", "52 kcal / 100g", "Lai giữa mâm xôi đỏ và dâu đen thơm nồng đượm"),
    "WhiteSapote": ("Trái white sapote (Hồng xiêm trắng Mexico)", "🟢", "80 kcal / 100g", "Thịt kem mềm như kem bơ vani thư giãn an thần"),
    "TraiYuzu": ("Trái yuzu quý tộc Nhật Bản", "🍋", "40 kcal / 100g", "Hương thơm số 1 thế giới cam quýt Nhật Bản"),
    "TraiYoungberry": ("Trái youngberry lai tạo Nam Phi", "🫐", "50 kcal / 100g", "Màu tím đen ngọt lịm quả mọng mùa hè"),
    "ZapoteTrang": ("Trái zapote trắng ruột kem", "🟢", "78 kcal / 100g", "Vị kem sữa dẻo ngọt thanh tao"),
    "ZapoteVang": ("Trái zapote vàng (Canistel)", "🟡", "135 kcal / 100g", "Cơm vàng bùi béo như khoai lang mật"),
    "ZapoteDen": ("Trái zapote đen socola bánh kem", "🟢", "65 kcal / 100g", "Ruột sánh dẻo vị socola tự nhiên"),
    "ZinfandelGrape": ("Trái zinfandel grape (Nho rượu vang đỏ)", "🍇", "72 kcal / 100g", "Nho đen đỏ đậm đà chuyên ủ rượu vang California"),
    "CamKaffir": ("Trái cam kaffir (Chanh chúc sần sùi)", "🍋", "30 kcal / 100g", "Vỏ sần sùi thơm nồng tinh dầu lá chúc"),
    "ChanhYenCitron": ("Trái chanh yên (Citron cổ đại)", "🍋", "25 kcal / 100g", "Cùi trắng dày ngọt thơm làm mứt citron cổ truyền"),
    "PhatThuFingered": ("Trái fingered citron (Phật thủ vàng)", "🍋", "25 kcal / 100g", "Múi xòe ngón tay Phật thơm ngát bàn thờ tổ tiên"),
    "HogPlum": ("Trái hog plum (Cóc rừng Mombin)", "🟡", "48 kcal / 100g", "Quả vàng chua thanh dầm muối ớt rừng"),
    "IceCreamBean": ("Trái ice cream bean (Đậu kem Inga)", "🟢", "60 kcal / 100g", "Quả đậu dài bóc ra cơm bông trắng vị hệt kem vani"),
    "TraiIlama": ("Trái ilama na kem Trung Mỹ", "🍈", "85 kcal / 100g", "Thịt hồng hoặc trắng ngọt ngào thơm ngát"),
    "IndianGooseberry": ("Trái Indian gooseberry (Amla Ấn Độ)", "🟢", "44 kcal / 100g", "Vua vitamin C trẻ hóa tóc và thị lực"),
    "JujubeHoang": ("Trái jujube hoang (Táo gai dại)", "🍎", "65 kcal / 100g", "Quả nhỏ vị chua ngọt bổ khí huyết"),
    "KaffirPlum": ("Trái kaffir plum (Mận Harpephyllum)", "🔴", "50 kcal / 100g", "Vỏ đỏ bóng vị chua thanh làm thạch Nam Phi"),
    "KumquatDo": ("Trái kumquat đỏ (Quất đỏ quý hiếm)", "🔴", "72 kcal / 100g", "Vỏ đỏ cam ăn cả vỏ ngọt thơm lạ kỳ"),
    "KumquatXanh": ("Trái kumquat xanh (Tắc xanh vắt nước)", "🟢", "35 kcal / 100g", "Pha trà tắc giải khát mùa hè"),
    "LemonAspen": ("Trái lemon aspen rừng mưa nước Úc", "🟡", "38 kcal / 100g", "Vị chanh bưởi the mát gia vị bushfood Úc"),
    "LimeCaviar": ("Trái lime caviar (Trứng cá hồi chanh)", "🍋", "32 kcal / 100g", "Tép tròn lấp lánh nổ giòn trong miệng"),
    "LucumaPeru": ("Trái lucuma Peru vàng ươm", "🟡", "99 kcal / 100g", "Vàng nghệ thơm ngọt dẻo làm kem số 1 Peru"),
    "MaboloHongNhung": ("Trái mabolo (Hồng nhung lông tơ)", "🔴", "75 kcal / 100g", "Vỏ lông nhung đỏ thắm thịt dẻo béo thơm ngon"),
    "MaquiBerry": ("Trái maqui berry Chile tím thẫm", "🫐", "68 kcal / 100g", "Siêu quả chống oxy hóa số 1 vùng Patagonia"),
    "TraiMarula": ("Trái marula Nam Phi thơm lừng", "🟡", "65 kcal / 100g", "Ủ rượu sữa Amarula nổi tiếng lục địa đen"),
    "TraiMaypop": ("Trái maypop (Chanh leo dại tím)", "🟣", "50 kcal / 100g", "Hoa chùm rực rỡ quả ngọt thanh mát"),
    "MidgenBerry": ("Trái midgen berry nước Úc", "⚪", "55 kcal / 100g", "Quả đốm tím trắng vị gừng ngọt độc đáo"),
    "MiracleBerryDo": ("Trái miracle berry đỏ tươi", "🔴", "40 kcal / 100g", "Làm mất cảm giác chua tăng vị ngọt diệu kỳ"),
    "MoringaPod": ("Trái moringa pod (Quả chùm ngây)", "🟢", "37 kcal / 100g", "Quả dài nấu canh cà ri siêu dinh dưỡng"),
    "MuntingiaTrungCa": ("Trái muntingia (Trứng cá đỏ ngọt)", "🔴", "45 kcal / 100g", "Quả mọng nhỏ đỏ ngọt lịm kỷ niệm tuổi thơ"),
    "TraiNaranjilla": ("Trái naranjilla (Lulo cam xanh Andes)", "🟠", "25 kcal / 100g", "Nước ép cam xanh giải khát hàng đầu Colombia"),
    "NeemFruit": ("Trái neem fruit (Quả xoan Ấn Độ)", "🟢", "50 kcal / 100g", "Thảo dược kháng khuẩn thanh lọc cơ thể"),
    "OsageOrange": ("Trái osage orange (Quả cam dại có rãnh)", "🟢", "45 kcal / 100g", "Vỏ rãnh não độc đáo đuổi côn trùng tự nhiên"),
    "PandanusFruit": ("Trái pandanus fruit (Dứa dại ven biển)", "🟠", "60 kcal / 100g", "Múi cam lửa nướng thơm ngọt giải nhiệt"),
    "PepinoMelon": ("Trái pepino melon (Dưa dưa hấu mini)", "🟡", "30 kcal / 100g", "Sọc tím vỏ vàng thơm mát vị dưa lê Nam Mỹ"),
    "PersimmonHoang": ("Trái persimmon hoang dại núi rừng", "🟠", "68 kcal / 100g", "Quả nhỏ đỏ cam vị ngọt đậm khi sương xuống"),
    "PhysalisTamBop": ("Trái physalis (Tầm bóp / Thù lù lồng đèn)", "🟡", "53 kcal / 100g", "Nằm trong lồng đèn giấy vàng óng bồi bổ gan"),
    "TraiPineberry": ("Trái pineberry (Dâu tây trắng vị dứa)", "🍓", "32 kcal / 100g", "Màu trắng hạt đỏ thơm nồng nàn hương dứa"),
    "PitahayaTim": ("Trái pitahaya tím (Thanh long ruột đỏ tím)", "🐉", "62 kcal / 100g", "Ruột đỏ tím thẫm ngọt mát chống lão hóa"),
    "PricklyPear": ("Trái prickly pear (Xương rồng Nopal)", "🟣", "41 kcal / 100g", "Quả tím đỏ mát lành hạ đường huyết"),
    "PurpleMangosteenWild": ("Trái purple mangosteen wild (Măng cụt tím rừng)", "🟣", "72 kcal / 100g", "Quả hoang dã vị chua ngọt thanh tao quý phái")
}

def inject_batch2():
    print("=" * 70)
    print("   BẮT ĐẦU ĐỒNG BỘ 100 LOẠI QUẢ ĐỘC ĐÁO QUỐC TẾ (101 - 200)   ")
    print("=" * 70)

    db = dict(FRUIT_LIBRARY_600)
    added = 0
    for k, (vn_name, icon, cal, ben) in EXOTIC_100_BATCH2.items():
        db[k] = {
            "vn_name": vn_name,
            "icon": icon,
            "calories": cal,
            "vitamins": "Vitamin C, E, Axit amin và các hợp chất chống oxy hóa ORAC cao",
            "benefits": ben,
            "tips": "Bảo quản nơi mát mẻ hoặc ngăn mát tủ lạnh, thưởng thức khi quả chín đạt hương thơm tối đa.",
            "avg_price_per_kg": 95000
        }
        added += 1

    out_file = os.path.join(PROJECT_ROOT, "src", "fruit_library_600.py")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("# fruit_library_600.py - Thư viện Tri thức Trái cây Toàn cầu Chuẩn hóa\n")
        f.write("FRUIT_LIBRARY_600 = " + json.dumps(db, ensure_ascii=False, indent=4) + "\n")

    print(f"[OK] Đã nạp thành công {added} loại quả mới vào Thư viện!")
    print(f"[*] Tổng số loại trái cây hiện tại trong Thư viện: {len(db)} loại!")

if __name__ == "__main__":
    inject_batch2()

