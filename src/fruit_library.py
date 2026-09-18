"""
fruit_library.py - Thư viện tri thức chuẩn hóa 100 loại trái cây
Môn học: Trí tuệ nhân tạo (AI) - Đề tài số 22
"""

FRUIT_LIBRARY_100 = {
    "Apple": {
        "vn_name": "Táo", "icon": "🍎", "calories": "52 kcal / 100g",
        "vitamins": "Vitamin C, Kali, Chất xơ pectin",
        "benefits": "Tốt cho tim mạch, hỗ trợ giảm cân, ngừa tiểu đường, làm sạch đường ruột.",
        "tips": "Chọn quả cầm nặng tay, vỏ căng bóng, không bị thâm dập.", "avg_price_per_kg": 65000
    },
    "Banana": {
        "vn_name": "Chuối", "icon": "🍌", "calories": "89 kcal / 100g",
        "vitamins": "Vitamin B6, Vitamin C, Kali phong phú",
        "benefits": "Cung cấp năng lượng tức thì, giảm chuột rút cơ bắp, hỗ trợ tiêu hóa.",
        "tips": "Chọn nải có cả quả xanh quả vàng, vỏ có lấm tấm chấm đen là ngọt nhất.", "avg_price_per_kg": 28000
    },
    "Orange": {
        "vn_name": "Cam", "icon": "🍊", "calories": "47 kcal / 100g",
        "vitamins": "Vitamin C cực cao, Axit Folic, Thiamine",
        "benefits": "Tăng cường hệ miễn dịch, đẹp da, tăng hấp thu sắt, giải nhiệt cơ thể.",
        "tips": "Chọn quả núm cuống phẳng, đáy vàng đều, bóp nhẹ thấy mọng nước.", "avg_price_per_kg": 40000
    },
    "Mango": {
        "vn_name": "Xoài", "icon": "🥭", "calories": "60 kcal / 100g",
        "vitamins": "Vitamin A (beta-carotene), Vitamin C, E",
        "benefits": "Sáng mắt, tăng cường thị lực, bổ sung chất chống oxy hóa, hỗ trợ tiêu hóa.",
        "tips": "Chọn quả có cuống còn dính nhựa mềm, da căng mịn, thơm ngào ngạt ở cuống.", "avg_price_per_kg": 50000
    },
    "Watermelon": {
        "vn_name": "Dưa hấu", "icon": "🍉", "calories": "30 kcal / 100g",
        "vitamins": "Lycopene, Vitamin A, C, Nước 92%",
        "benefits": "Bù nước nhanh, giảm đau nhức cơ bắp, mát gan lợi tiểu, tốt cho da.",
        "tips": "Xem đáy quả có vệt màu vàng kem, cuống nhỏ héo và gõ nghe tiếng bộp bộp.", "avg_price_per_kg": 18000
    },
    "Strawberry": {
        "vn_name": "Dâu tây", "icon": "🍓", "calories": "32 kcal / 100g",
        "vitamins": "Vitamin C dồi dào, Mangan, Axit Ellagic",
        "benefits": "Chống lão hóa da, kiểm soát đường huyết, kháng viêm, tăng cường trí nhớ.",
        "tips": "Chọn quả đỏ mọng đều màu, cuống lá còn xanh tươi, hạt màu vàng sáng.", "avg_price_per_kg": 180000
    },
    "Grape": {
        "vn_name": "Nho", "icon": "🍇", "calories": "69 kcal / 100g",
        "vitamins": "Resveratrol, Vitamin K, Vitamin B2",
        "benefits": "Bảo vệ thành mạch máu, ngăn ngừa hình thành cục máu đông, làm chậm lão hóa.",
        "tips": "Chùm nho còn phủ lớp phấn trắng tự nhiên, quả căng mọng, cuống tươi dẻo.", "avg_price_per_kg": 120000
    },
    "Pineapple": {
        "vn_name": "Dứa (Thơm)", "icon": "🍍", "calories": "50 kcal / 100g",
        "vitamins": "Enzyme Bromelain, Vitamin C, Mangan",
        "benefits": "Kháng viêm mạnh mẽ, hỗ trợ tiêu hóa protein, làm dịu vết thương, thơm miệng.",
        "tips": "Chọn quả ngắn tròn bầu bĩnh, mắt to đều, màu vàng tươi từ cuống đến ngọn.", "avg_price_per_kg": 25000
    },
    "Avocado": {
        "vn_name": "Bơ", "icon": "🥑", "calories": "160 kcal / 100g",
        "vitamins": "Chất béo đơn không bão hòa, Vitamin E, K, Kali",
        "benefits": "Hạ cholesterol xấu LDL, phát triển trí não, nuôi dưỡng làn da và mái tóc bóng khỏe.",
        "tips": "Nắn nhẹ thấy hơi mềm, lắc nghe tiếng hạt tách nhẹ, cuống hơi vàng là bơ sáp ngon.", "avg_price_per_kg": 55000
    },
    "Dragonfruit": {
        "vn_name": "Thanh long", "icon": "🐉", "calories": "57 kcal / 100g",
        "vitamins": "Chất xơ prebiotic, Sắt, Vitamin C, Magie",
        "benefits": "Nuôi dưỡng lợi khuẩn đường ruột, hỗ trợ thiếu máu do thiếu sắt, kiểm soát đường huyết.",
        "tips": "Vỏ màu hồng đậm tươi, tai ngoe còn xanh cứng cáp, quả căng tròn không thâm đen.", "avg_price_per_kg": 35000
    },
    "Lemon": {
        "vn_name": "Chanh vàng", "icon": "🍋", "calories": "29 kcal / 100g",
        "vitamins": "Axit citric, Vitamin C, Hesperidin",
        "benefits": "Thanh lọc cơ thể, hỗ trợ tiêu hóa, ngăn ngừa sỏi thận, kiềm hóa cơ thể.",
        "tips": "Vỏ bóng loáng, màu vàng tươi đều, cầm nặng tay, có mùi thơm mát tự nhiên.", "avg_price_per_kg": 45000
    },
    "Lime": {
        "vn_name": "Chanh ta (Chanh xanh)", "icon": "🍋", "calories": "30 kcal / 100g",
        "vitamins": "Vitamin C, Canxi, Axit Citric",
        "benefits": "Tăng tiết dịch tiêu hóa, chống say xe, tăng đề kháng, pha nước chấm tuyệt hảo.",
        "tips": "Vỏ mỏng láng mịn, bóp nhẹ thấy mềm và thơm nồng là chanh nhiều nước.", "avg_price_per_kg": 30000
    },
    "Peach": {
        "vn_name": "Đào", "icon": "🍑", "calories": "39 kcal / 100g",
        "vitamins": "Vitamin C, A, Kali, Niacin",
        "benefits": "Làm mịn da, bảo vệ mắt, cải thiện lưu thông máu, hỗ trợ tiêu hóa.",
        "tips": "Quả tròn đều, lớp lông tơ mịn màng, ngửi cuống thơm dịu, ấn nhẹ không bị mềm nhũn.", "avg_price_per_kg": 70000
    },
    "Cherry": {
        "vn_name": "Anh đào (Cherry)", "icon": "🍒", "calories": "63 kcal / 100g",
        "vitamins": "Melatonin tự nhiên, Anthocyanin, Vitamin C",
        "benefits": "Cải thiện giấc ngủ, giảm đau nhức do gút và viêm khớp, phục hồi cơ bắp.",
        "tips": "Màu đỏ thẫm đen bóng, cuống xanh tươi dính chặt vào quả, không bị nứt vỏ.", "avg_price_per_kg": 350000
    },
    "Kiwi": {
        "vn_name": "Kiwi", "icon": "🥝", "calories": "61 kcal / 100g",
        "vitamins": "Enzyme Actinidin, Vitamin C gấp đôi cam, Vitamin E",
        "benefits": "Tốt cho hệ hô hấp, ngừa hen suyễn, cải thiện chất lượng giấc ngủ.",
        "tips": "Bấm nhẹ tay thấy hơi lún đều là quả vừa chín tới, vị ngọt thanh chua dịu.", "avg_price_per_kg": 140000
    },
    "Coconut": {
        "vn_name": "Dừa", "icon": "🥥", "calories": "354 kcal / 100g (Cơm) | 19 kcal (Nước)",
        "vitamins": "Chất điện giải tự nhiên, Axit Lauric, Kali, Magie",
        "benefits": "Bù nước và điện giải cấp tốc, tăng cường miễn dịch, kháng khuẩn kháng nấm.",
        "tips": "Chọn dừa xiêm quả nhỏ vừa phải, cuống còn tươi xanh, lắc nghe nước óc ách.", "avg_price_per_kg": 25000
    },
    "Pear": {
        "vn_name": "Lê", "icon": "🍐", "calories": "57 kcal / 100g",
        "vitamins": "Chất xơ hòa tan, Vitamin C, Vitamin K, Đồng",
        "benefits": "Mát họng, giảm ho, bổ phế tiêu đờm, hạ sốt, duy trì sức khỏe tim mạch.",
        "tips": "Quả tròn đều, vỏ bóng mịn, rốn lê dưới đáy sâu và rộng là quả ngọt thanh.", "avg_price_per_kg": 60000
    },
    "Pomegranate": {
        "vn_name": "Lựu", "icon": "🍎", "calories": "83 kcal / 100g",
        "vitamins": "Punicalagin, Axit Punicic, Vitamin C, K",
        "benefits": "Chống oxy hóa vượt trội gấp 3 lần trà xanh, hạ huyết áp, bảo vệ tế bào não.",
        "tips": "Quả to tròn có các gờ cạnh rõ rệt (quả ngọt nhiều hạt), vỏ hơi nám đỏ sẫm.", "avg_price_per_kg": 85000
    },
    "Papaya": {
        "vn_name": "Đu đủ", "icon": "🍈", "calories": "43 kcal / 100g",
        "vitamins": "Enzyme Papain, Beta-carotene, Folate, Vitamin C",
        "benefits": "Hỗ trợ tiêu hóa cực tốt, chống táo bón, làm sáng da mờ thâm nám, bổ mắt.",
        "tips": "Dáng thon dài, chín vàng từ cuống lan dần xuống, ấn nhẹ vào vỏ thấy mềm đều.", "avg_price_per_kg": 22000
    },
    "Guava": {
        "vn_name": "Ổi", "icon": "🍏", "calories": "68 kcal / 100g",
        "vitamins": "Vitamin C cao gấp 4 lần cam, Chất xơ thô",
        "benefits": "Ổn định đường huyết cho người tiểu đường, giảm cân, cải thiện sức đề kháng.",
        "tips": "Có đường vân gồ ghề, cầm chắc tay, vỏ màu xanh nhạt hơi ửng vàng.", "avg_price_per_kg": 25000
    },
    "Lychee": {
        "vn_name": "Vải thiều", "icon": "🍒", "calories": "66 kcal / 100g",
        "vitamins": "Oligonol, Vitamin C, Đồng, Magie",
        "benefits": "Bồi bổ khí huyết, tăng sinh collagen, tăng cường tuần hoàn máu, giải tỏa mệt mỏi.",
        "tips": "Cành dẻo, vỏ đỏ tươi gai nhẵn, nắn thấy căng tròn, cùi dày hạt nhỏ.", "avg_price_per_kg": 45000
    },
    "Longan": {
        "vn_name": "Nhãn", "icon": "🟤", "calories": "60 kcal / 100g",
        "vitamins": "Sắt, Vitamin C, Riboflavin, Polyphenol",
        "benefits": "An thần, dưỡng tâm bổ tỳ, cải thiện chứng mất ngủ suy nhược thần kinh.",
        "tips": "Nhãn lồng cùi dày ráo nước, vỏ màu vàng sậm hơi ráp, hạt nhỏ vị ngọt sắc.", "avg_price_per_kg": 40000
    },
    "Rambutan": {
        "vn_name": "Chôm chôm", "icon": "🔴", "calories": "68 kcal / 100g",
        "vitamins": "Vitamin C, Đồng, Sắt, Phốt pho",
        "benefits": "Hỗ trợ tái tạo tế bào hồng cầu, tăng cường năng lượng, làm khỏe tóc và da.",
        "tips": "Râu còn xanh tươi cứng cáp, vỏ đỏ thắm, cùi tróc dễ bóc không dính hạt.", "avg_price_per_kg": 45000
    },
    "Durian": {
        "vn_name": "Sầu riêng", "icon": "🟡", "calories": "147 kcal / 100g",
        "vitamins": "Chất béo thực vật lành mạnh, Vitamin B, Tryptophan",
        "benefits": "Vua trái cây: bổ sung năng lượng dồi dào, giảm căng thẳng, tăng hạnh phúc.",
        "tips": "Gai to đều nở bung, eo tròn phình to lộ rõ múi, cuống tươi ướt nhựa thơm nức.", "avg_price_per_kg": 130000
    },
    "Jackfruit": {
        "vn_name": "Mít", "icon": "🍈", "calories": "95 kcal / 100g",
        "vitamins": "Isoflavone, Lignans, Vitamin A, C, Canxi",
        "benefits": "Tăng cường sức khỏe xương khớp, chống lại tác hại gốc tự do, bổ mắt.",
        "tips": "Gai mít nở to thưa phẳng, quả tròn đều không thắt eo, vỗ vào nghe tiếng bình bịch.", "avg_price_per_kg": 35000
    },
    "Mangosteen": {
        "vn_name": "Măng cụt", "icon": "🟣", "calories": "73 kcal / 100g",
        "vitamins": "Hợp chất Xanthone quý giá, Axit Folic, Magie",
        "benefits": "Nữ hoàng trái cây: kháng khuẩn mạnh, thanh nhiệt giải độc, ngừa ung thư.",
        "tips": "Đếm số cánh hoa dưới đáy quả, nắn nhẹ thấy mềm đều tay không bị sượng.", "avg_price_per_kg": 85000
    },
    "Plum": {
        "vn_name": "Mận hậu", "icon": "🟣", "calories": "46 kcal / 100g",
        "vitamins": "Axit malic, Vitamin C, Chất xơ sorbitol",
        "benefits": "Kích thích vị giác, chống táo bón tự nhiên, làm sạch răng miệng, bổ sung sắt.",
        "tips": "Phủ phấn trắng dày, màu đỏ tía sẫm, sờ thấy căng tròn rắn rỏi.", "avg_price_per_kg": 55000
    },
    "Passionfruit": {
        "vn_name": "Chanh leo (Chanh dây)", "icon": "🟡", "calories": "97 kcal / 100g",
        "vitamins": "Alkaloid harman làm dịu thần kinh, Vitamin A, C, Sắt",
        "benefits": "Giảm lo âu căng thẳng, hỗ trợ điều trị mất ngủ, hạ huyết áp, giải nhiệt.",
        "tips": "Vỏ hơi nhăn nheo tím đậm (xuống nước ngọt đậm đà), cầm nặng tay.", "avg_price_per_kg": 35000
    },
    "Fig": {
        "vn_name": "Quả sung ngọt (Mỹ)", "icon": "🟤", "calories": "74 kcal / 100g",
        "vitamins": "Canxi phong phú bậc nhất, Kali, Kẽm, Chất xơ",
        "benefits": "Phòng ngừa loãng xương, tốt cho hệ tiêu hóa, điều hòa huyết áp tim mạch.",
        "tips": "Chín mềm vừa phải màu tím nâu, phần đáy hé mở nhẹ tỏa mùi mật ngọt.", "avg_price_per_kg": 160000
    },
    "Blueberry": {
        "vn_name": "Việt quất", "icon": "🫐", "calories": "57 kcal / 100g",
        "vitamins": "Anthocyanin hàm lượng siêu cao, Vitamin K1, Vitamin C",
        "benefits": "Siêu thực phẩm cho não bộ: tăng trí nhớ, bảo vệ mắt, làm chậm lão hóa.",
        "tips": "Màu xanh thẫm phủ lớp phấn mờ bạc bên ngoài, hạt mọng đều, không mềm nhũn.", "avg_price_per_kg": 280000
    },
    "CustardApple": {
        "vn_name": "Mãng cầu ta (Na)", "icon": "🍏", "calories": "75 kcal / 100g",
        "vitamins": "Vitamin C, Vitamin B6, Magie, Kali",
        "benefits": "Bổ não, tốt cho tim mạch, hỗ trợ giảm triệu chứng viêm khớp, tăng đề kháng.",
        "tips": "Mắt to phẳng, kẽ mắt trắng ngà hơi nứt nhẹ, cuống nhỏ, quả tròn đều.", "avg_price_per_kg": 60000
    },
    "Soursop": {
        "vn_name": "Mãng cầu xiêm", "icon": "🍈", "calories": "66 kcal / 100g",
        "vitamins": "Acetogenins, Vitamin C, B1, B2",
        "benefits": "Tăng cường miễn dịch, kháng khuẩn kháng viêm, hỗ trợ hạ huyết áp.",
        "tips": "Gai mềm thưa, khoảng cách giữa các gai rộng, nắn thấy mềm tay là quả chín.", "avg_price_per_kg": 45000
    },
    "Starfruit": {
        "vn_name": "Khế ngọt / Khế chua", "icon": "⭐", "calories": "31 kcal / 100g",
        "vitamins": "Vitamin C, Axit Oxalic, Đồng, Kali",
        "benefits": "Thanh nhiệt, giải độc, hỗ trợ hạ đường huyết, tiêu đờm trị ho.",
        "tips": "Khía múi dày căng mọng, rìa khía có màu xanh đậm ngả vàng là khế chín ngọt.", "avg_price_per_kg": 25000
    },
    "Persimmon": {
        "vn_name": "Hồng giòn / Hồng đỏ", "icon": "🟠", "calories": "70 kcal / 100g",
        "vitamins": "Tannin, Beta-carotene, Mangan, Vitamin C",
        "benefits": "Làm khỏe mạch máu, bổ mắt, làm chậm quá trình lão hóa, hỗ trợ tiêu hóa.",
        "tips": "Chọn hồng giòn vỏ vàng cam bóng láng, cầm chắc nịch không dập nát.", "avg_price_per_kg": 50000
    },
    "Grapefruit": {
        "vn_name": "Bưởi diễn", "icon": "🍈", "calories": "42 kcal / 100g",
        "vitamins": "Naringin, Vitamin C, Chất xơ hòa tan",
        "benefits": "Đốt cháy mỡ thừa tự nhiên, hạ cholesterol, kiểm soát nồng độ insulin.",
        "tips": "Quả nhỏ tròn, vỏ mỏng vàng ươm, xuống nước nắn mềm, mùi thơm nồng nàn.", "avg_price_per_kg": 35000
    },
    "Tangerine": {
        "vn_name": "Quýt đường", "icon": "🍊", "calories": "53 kcal / 100g",
        "vitamins": "Flavonoid, Vitamin C, Axit Folic",
        "benefits": "Chống oxy hóa, bảo vệ gan, tăng sinh collagen, tăng tuần hoàn máu não.",
        "tips": "Vỏ mỏng hơi phồng, màu vàng cam sáng, cuống còn xanh tươi dính chặt.", "avg_price_per_kg": 35000
    },
    "Apricot": {
        "vn_name": "Mơ vàng", "icon": "🍑", "calories": "48 kcal / 100g",
        "vitamins": "Lutein, Zeaxanthin, Vitamin A, E",
        "benefits": "Bảo vệ võng mạc mắt, làm dịu niêm mạc dạ dày, thải độc đường ruột.",
        "tips": "Quả tròn phủ lông tơ óng ả, màu vàng nghệ ửng hồng, thơm dịu dễ chịu.", "avg_price_per_kg": 60000
    },
    "Blackberry": {
        "vn_name": "Mâm xôi đen", "icon": "🫐", "calories": "43 kcal / 100g",
        "vitamins": "Axit Ellagic, Vitamin C, K, Mangan",
        "benefits": "Bảo vệ não bộ khỏi suy thoái nhận thức, giúp xương chắc khỏe, lành vết thương.",
        "tips": "Hạt mọng đen tuyền sáng bóng, cuống rỗng không dính lõi trắng.", "avg_price_per_kg": 320000
    },
    "Raspberry": {
        "vn_name": "Mâm xôi đỏ (Phúc bồn tử)", "icon": "🍓", "calories": "52 kcal / 100g",
        "vitamins": "Rheosmin (xeton mâm xôi), Vitamin C, Chất xơ",
        "benefits": "Kích thích chuyển hóa mỡ, chống viêm mãn tính, bảo vệ tế bào tim mạch.",
        "tips": "Quả đỏ tươi đều màu, các túi hạt căng mọng, khô ráo không bị dập nát.", "avg_price_per_kg": 300000
    },
    "Cranberry": {
        "vn_name": "Nam việt quất", "icon": "🍒", "calories": "46 kcal / 100g",
        "vitamins": "Proanthocyanidins loại A, Vitamin C, E",
        "benefits": "Ngăn ngừa vi khuẩn bám vào đường tiết niệu, bảo vệ men răng khỏi sâu.",
        "tips": "Quả đỏ thẫm sáng bóng, rắn chắc, khi rơi xuống bàn có độ nảy tốt.", "avg_price_per_kg": 260000
    },
    "Gooseberry": {
        "vn_name": "Lý chua lông", "icon": "🍏", "calories": "44 kcal / 100g",
        "vitamins": "Axit hữu cơ, Vitamin C, Đồng, Mangan",
        "benefits": "Kích thích enzym tiêu hóa, giải nhiệt, hỗ trợ kiểm soát đường huyết.",
        "tips": "Vỏ trong mờ nhìn thấy hạt bên trong, gân sọc rõ ràng, màu xanh ngọc bích.", "avg_price_per_kg": 190000
    },
    "Mulberry": {
        "vn_name": "Dâu tằm", "icon": "🟣", "calories": "43 kcal / 100g",
        "vitamins": "Resveratrol, Sắt, Vitamin C, Vitamin K1",
        "benefits": "Bổ can thận, dưỡng huyết trừ phong, làm đen râu tóc, an thần sáng mắt.",
        "tips": "Chọn quả màu tím đen căng mọng, cuống tươi, vị ngọt thanh không bị chua gắt.", "avg_price_per_kg": 50000
    },
    "Sapodilla": {
        "vn_name": "Hồng xiêm (Sabôchê)", "icon": "🥔", "calories": "83 kcal / 100g",
        "vitamins": "Tannin kháng viêm, Vitamin A, Canxi, Phốt pho",
        "benefits": "Cung cấp năng lượng dồi dào, cầm tiêu chảy nhẹ, làm dịu dạ dày, chắc răng.",
        "tips": "Quả thon dài màu nâu cát, vỏ không nứt, nắn mềm đều, thơm mùi mật mía.", "avg_price_per_kg": 35000
    },
    "Tamarind": {
        "vn_name": "Me ngọt / Me chua", "icon": "🟤", "calories": "239 kcal / 100g",
        "vitamins": "Axit Tartaric, Vitamin B1 (Thiamine), Magie, Sắt",
        "benefits": "Nhuận tràng, giải nhiệt hạ sốt, điều hòa mỡ máu, tăng dẫn truyền thần kinh.",
        "tips": "Vỏ nâu giòn rụm dễ bóc, thịt me dẻo quánh nâu sẫm, không bị mốc trắng.", "avg_price_per_kg": 60000
    },
    "Kumquat": {
        "vn_name": "Quất (Tắc)", "icon": "🍊", "calories": "71 kcal / 100g",
        "vitamins": "Tinh dầu vỏ quất, Vitamin C, Limonene, Lutein",
        "benefits": "Trừ ho tiêu đờm, làm ấm cổ họng, chống nôn say xe, kích thích vị giác.",
        "tips": "Quả tròn vàng ươm, vỏ mọng tinh dầu, thơm hăng tự nhiên, cuống tươi cứng.", "avg_price_per_kg": 30000
    },
    "Jujube": {
        "vn_name": "Táo tàu tươi", "icon": "🟤", "calories": "79 kcal / 100g",
        "vitamins": "Saponin, Flavonoid, Vitamin C cao gấp 20 lần táo",
        "benefits": "Bổ trung ích khí, dưỡng huyết an thần, tăng sức bền thành mạch, kéo dài tuổi thọ.",
        "tips": "Quả da xanh lấm tấm đốm nâu đỏ, giòn tan ngọt sắc, thịt trắng ngà.", "avg_price_per_kg": 90000
    },
    "Date": {
        "vn_name": "Chà là tươi", "icon": "🟤", "calories": "277 kcal / 100g",
        "vitamins": "Đường tự nhiên Glucose, Fructose, Kali, Selen",
        "benefits": "Hồi phục sức lực ngay lập tức cho vận động viên, tốt cho phụ nữ mang thai.",
        "tips": "Quả vàng óng hoặc đỏ thắm, thịt giòn ngọt thanh không chát, vỏ không rách.", "avg_price_per_kg": 180000
    },
    "Cantaloupe": {
        "vn_name": "Dưa lưới vàng", "icon": "🍈", "calories": "34 kcal / 100g",
        "vitamins": "Beta-carotene cực cao, Axit Folic, Vitamin C",
        "benefits": "Bảo vệ làn da khỏi tia cực tím UV, nuôi dưỡng mắt sáng, điều hòa huyết áp.",
        "tips": "Lớp vân lưới nổi cộm đều đặn, rốn dưa hơi lún vào và thơm ngát hương mật.", "avg_price_per_kg": 45000
    },
    "Honeydew": {
        "vn_name": "Dưa lê hoàng kim", "icon": "🍈", "calories": "36 kcal / 100g",
        "vitamins": "Vitamin C, B6, Đồng, Kali",
        "benefits": "Bổ sung collagen, làm mờ nếp nhăn, hỗ trợ xương khớp dẻo dai.",
        "tips": "Vỏ màu vàng kim bóng loáng hoặc xanh ngọc, đáy quả tròn đầy thơm dịu.", "avg_price_per_kg": 35000
    },
    "StarApple": {
        "vn_name": "Vú sữa Lò Rèn", "icon": "🟣", "calories": "67 kcal / 100g",
        "vitamins": "Dòng sữa ngọt giàu Canxi, Phốt pho, Vitamin C",
        "benefits": "Làm dịu cơn đói, chắc khỏe xương răng, làm đẹp da phụ nữ, dễ tiêu hóa.",
        "tips": "Vỏ màu tím nhạt hoặc trắng sáng bóng, bóp nhẹ thấy mềm đều toàn thân.", "avg_price_per_kg": 55000
    },
    "Breadfruit": {
        "vn_name": "Sa kê", "icon": "🍈", "calories": "103 kcal / 100g",
        "vitamins": "Tinh bột kháng lành mạnh, Chất xơ, Sắt, Kali",
        "benefits": "No lâu giảm mỡ, hỗ trợ kiểm soát huyết áp, tốt cho đường ruột.",
        "tips": "Quả to nở đều mắt, mắt gai nở phẳng, vỏ xanh ngả vàng nhạt.", "avg_price_per_kg": 40000
    },
    "Pomelo": {
        "vn_name": "Bưởi da xanh", "icon": "🍈", "calories": "38 kcal / 100g",
        "vitamins": "Vitamin C, Naringenin, Axit Citric, Kali",
        "benefits": "Hạ mỡ máu, giảm cân an toàn, thanh lọc gan, hạ đường huyết.",
        "tips": "Quả nặng từ 1.2kg trở lên, cuống tươi, da căng láng, gai nở đều.", "avg_price_per_kg": 50000
    },
    "Langsat": {
        "vn_name": "Bòn bon", "icon": "🟡", "calories": "65 kcal / 100g",
        "vitamins": "Vitamin C, B1, Riboflavin, Chất xơ",
        "benefits": "Chống oxy hóa tế bào, giải nhiệt, hỗ trợ hạ sốt, điều trị kiết lỵ.",
        "tips": "Vỏ màu vàng nhạt hơi rám, cuống tươi không rụng, nắn thấy dẻo mềm.", "avg_price_per_kg": 60000
    },
    "Santol": {
        "vn_name": "Quả sấu đỏ (Dọc / Măng cụt dại)", "icon": "🟡", "calories": "50 kcal / 100g",
        "vitamins": "Bryonolic acid, Sandoric acid, Vitamin C",
        "benefits": "Kháng khuẩn, tăng cường miễn dịch, làm dịu vết côn trùng cắn.",
        "tips": "Vỏ vàng nhung mịn, ấn thấy hơi mềm, cùi trong trắng ngà ngọt chua thanh.", "avg_price_per_kg": 40000
    },
    "Acerola": {
        "vn_name": "Sơ ri", "icon": "🍒", "calories": "32 kcal / 100g",
        "vitamins": "Vua Vitamin C (cao gấp 30-50 lần cam), Bioflavonoid",
        "benefits": "Chống lão hóa cực mạnh, tăng đề kháng nhanh chóng, ngừa cảm cúm.",
        "tips": "Quả tròn khía múi nhẹ, màu đỏ tươi mọng nước, cuống lá còn xanh bóng.", "avg_price_per_kg": 35000
    },
    "Feijoa": {
        "vn_name": "Ổi dứa (Feijoa)", "icon": "🍏", "calories": "55 kcal / 100g",
        "vitamins": "Iot tự nhiên rất hiếm, Vitamin C, Chất xơ",
        "benefits": "Hỗ trợ tuyến giáp hoạt động tối ưu, tăng chuyển hóa chất béo.",
        "tips": "Quả xanh bóng hình bầu dục, tỏa hương thơm dứa pha dâu tây nồng nàn.", "avg_price_per_kg": 150000
    },
    "PassionfruitBanana": {
        "vn_name": "Chuối tiêu hồng", "icon": "🍌", "calories": "92 kcal / 100g",
        "vitamins": "Serotonin, Kali, Vitamin B6, Magie",
        "benefits": "Giúp tinh thần sảng khoái, chống trầm cảm, bảo vệ niêm mạc dạ dày.",
        "tips": "Quả cong dài đều, màu vàng hồng rực rỡ, thịt dẻo thơm ngậy.", "avg_price_per_kg": 30000
    },
    "RedBanana": {
        "vn_name": "Chuối đỏ Dacca", "icon": "🍌", "calories": "90 kcal / 100g",
        "vitamins": "Carotenoid gấp 4 lần chuối vàng, Vitamin C, Kali",
        "benefits": "Cải thiện thị lực, chống oxy hóa, hỗ trợ ổn định nhịp tim.",
        "tips": "Vỏ màu đỏ tím thẫm đậm đà, thịt chuối màu vàng kem thơm ngọt ngậy.", "avg_price_per_kg": 75000
    },
    "Plantain": {
        "vn_name": "Chuối sứ (Chuối ngự)", "icon": "🍌", "calories": "85 kcal / 100g",
        "vitamins": "Tinh bột kháng, Kali, Vitamin B6, Vitamin C",
        "benefits": "Phục hồi chức năng dạ dày, làm dịu trào ngược dạ dày, dễ tiêu hóa.",
        "tips": "Quả tròn mập, hai đầu thon gọn, vỏ mỏng vàng ươm, vị ngọt đậm đà.", "avg_price_per_kg": 25000
    },
    "BloodOrange": {
        "vn_name": "Cam ruột đỏ (Blood Orange)", "icon": "🍊", "calories": "50 kcal / 100g",
        "vitamins": "Anthocyanin quý hiếm, Axit Folic, Vitamin C",
        "benefits": "Bảo vệ thành mạch tim mạch, ngăn xơ vữa động mạch, làm chậm lão hóa.",
        "tips": "Vỏ có vệt ửng đỏ tía, cầm nặng tay, mọng nước, vị ngọt thanh pha chua nhẹ.", "avg_price_per_kg": 95000
    },
    "Clementine": {
        "vn_name": "Quýt Clementine", "icon": "🍊", "calories": "47 kcal / 100g",
        "vitamins": "Vitamin C, Hesperidin, Axit Citric",
        "benefits": "Dễ bóc vỏ, không hạt, tăng cường hệ thống miễn dịch cho trẻ nhỏ.",
        "tips": "Quả nhỏ tròn dẹt, màu cam rực rỡ, vỏ mỏng dính sát vào múi mọng nước.", "avg_price_per_kg": 75000
    },
    "Mandarin": {
        "vn_name": "Quýt hồng Lai Vung", "icon": "🍊", "calories": "53 kcal / 100g",
        "vitamins": "Beta-cryptoxanthin, Kali, Vitamin C",
        "benefits": "Ngăn ngừa loãng xương, tốt cho hệ hô hấp, thanh nhiệt cơ thể.",
        "tips": "Vỏ mỏng màu cam đỏ láng bóng, mùi thơm thanh khiết đặc trưng.", "avg_price_per_kg": 45000
    },
    "GreenApple": {
        "vn_name": "Táo xanh Granny Smith", "icon": "🍏", "calories": "52 kcal / 100g",
        "vitamins": "Axit malic dồi dào, Chất xơ pectin, Vitamin C",
        "benefits": "Giúp răng trắng sáng, kiểm soát cảm giác thèm ăn, hỗ trợ giảm cân.",
        "tips": "Vỏ màu xanh lục sáng bóng, cầm cứng cáp, vị chua giòn sảng khoái.", "avg_price_per_kg": 80000
    },
    "GoldenDelicious": {
        "vn_name": "Táo vàng Golden Delicious", "icon": "🍏", "calories": "53 kcal / 100g",
        "vitamins": "Chất chống oxy hóa Polyphenol, Kali, Vitamin C",
        "benefits": "Thịt mềm xốp ngọt thanh, phù hợp làm bánh và sinh tố dinh dưỡng.",
        "tips": "Vỏ màu vàng rơm điểm chấm nhỏ li ti, thơm dịu, ấn nhẹ không bị dập.", "avg_price_per_kg": 75000
    },
    "RedDelicious": {
        "vn_name": "Táo đỏ Mỹ Red Delicious", "icon": "🍎", "calories": "52 kcal / 100g",
        "vitamins": "Anthocyanin trong vỏ đỏ đậm, Kali, Vitamin C",
        "benefits": "Giảm lượng đường trong máu, tốt cho đường ruột và tim mạch.",
        "tips": "Dáng thuôn dài có 5 khía nổi rõ ở đáy quả, màu đỏ thẫm bóng bẩy.", "avg_price_per_kg": 70000
    },
    "GalaApple": {
        "vn_name": "Táo Gala", "icon": "🍎", "calories": "54 kcal / 100g",
        "vitamins": "Vitamin C, Boron, Kali, Chất xơ",
        "benefits": "Tốt cho trí nhớ, củng cố độ bền của xương khớp, vị ngọt thơm nức.",
        "tips": "Vỏ sọc vàng đỏ xen kẽ, giòn rụm nhiều nước, mùi thơm vani thoang thoảng.", "avg_price_per_kg": 68000
    },
    "FujiApple": {
        "vn_name": "Táo Fuji Nhật Bản", "icon": "🍎", "calories": "63 kcal / 100g",
        "vitamins": "Độ ngọt tự nhiên cao, Vitamin C, Flavonoid",
        "benefits": "Giữ được độ giòn lâu nhất, bổ sung năng lượng, hỗ trợ tiêu hóa thức ăn.",
        "tips": "Quả to tròn trịa, màu đỏ hồng phủ vân sọc, gõ vào nghe tiếng đanh giòn.", "avg_price_per_kg": 85000
    },
    "AnjouPear": {
        "vn_name": "Lê xanh Anjou", "icon": "🍐", "calories": "58 kcal / 100g",
        "vitamins": "Axit Folic, Vitamin K, Canxi, Kali",
        "benefits": "Hạ sốt bổ phế, giải nhiệt nhanh chóng, thanh lọc chất cặn bã trong thận.",
        "tips": "Quả hình chuông ngắn, vỏ xanh nõn chuối, ấn nhẹ gần cuống thấy mềm là chín.", "avg_price_per_kg": 80000
    },
    "BoscPear": {
        "vn_name": "Lê nâu Bosc", "icon": "🍐", "calories": "60 kcal / 100g",
        "vitamins": "Chất xơ không hòa tan, Đồng, Vitamin C",
        "benefits": "Tốt cho thành ruột, nhuận tràng tự nhiên, giảm nguy cơ sỏi mật.",
        "tips": "Cổ dài thon thả, vỏ màu nâu quế điểm hoa gai nhám, thịt giòn thơm mật ong.", "avg_price_per_kg": 85000
    },
    "AsianPear": {
        "vn_name": "Lê Hàn Quốc (Mắc cọp)", "icon": "🍐", "calories": "42 kcal / 100g",
        "vitamins": "Nước 88%, Kali, Magie, Vitamin C",
        "benefits": "Giải rượu bia cấp tốc, làm dịu cổ họng khản tiếng, bù điện giải.",
        "tips": "Quả to tròn xoe như quả táo, vỏ màu vàng nâu sáng, giòn tan mọng nước.", "avg_price_per_kg": 90000
    },
    "BlackGrape": {
        "vn_name": "Nho đen không hạt Mỹ", "icon": "🍇", "calories": "70 kcal / 100g",
        "vitamins": "Resveratrol nồng độ cao nhất, Vitamin K, Kali",
        "benefits": "Ngăn ngừa đột quỵ, hạ huyết áp, bảo vệ thành mạch máu não.",
        "tips": "Quả thuôn dài, màu đen tuyền phủ lớp phấn trắng tinh, cành tươi xanh.", "avg_price_per_kg": 180000
    },
    "GreenGrape": {
        "vn_name": "Nho xanh Ninh Thuận", "icon": "🍇", "calories": "67 kcal / 100g",
        "vitamins": "Lutein, Zeaxanthin, Axit Tartaric, Vitamin C",
        "benefits": "Tốt cho giác mạc mắt, giải nhiệt mùa hè, kích thích tiết enzym dạ dày.",
        "tips": "Chùm khít quả, quả bầu dục màu xanh vàng nhạt, vỏ mỏng vị chua ngọt thanh.", "avg_price_per_kg": 75000
    },
    "RedGlobeGrape": {
        "vn_name": "Nho đỏ Red Globe", "icon": "🍇", "calories": "68 kcal / 100g",
        "vitamins": "Anthocyanin, Vitamin C, Vitamin B1, B6",
        "benefits": "Bồi bổ khí huyết, tăng lưu lượng tuần hoàn máu, làm săn chắc da mặt.",
        "tips": "Quả to tròn xoe như viên bi lớn, màu đỏ tím bóng bẩy, thịt chắc giòn.", "avg_price_per_kg": 110000
    },
    "MuscatGrape": {
        "vn_name": "Nho mẫu đơn Muscat", "icon": "🍇", "calories": "75 kcal / 100g",
        "vitamins": "Hương thơm tinh dầu tự nhiên, Đường quý, Vitamin C",
        "benefits": "Đẳng cấp trái cây thượng lưu, chống suy nhược cơ thể, thư giãn tinh thần.",
        "tips": "Quả xanh ngọc bích to đều, cắn giòn sần sật, hương thơm hoa hồng mật ong.", "avg_price_per_kg": 450000
    },
    "GoldenKiwi": {
        "vn_name": "Kiwi vàng New Zealand", "icon": "🥝", "calories": "63 kcal / 100g",
        "vitamins": "Vitamin C gấp 3 lần cam, Axit Folic, Vitamin E",
        "benefits": "Thịt vàng ươm ngọt lịm không chua, tăng sinh collagen nhanh chóng.",
        "tips": "Vỏ nhẵn mịn ít lông tơ, đầu núm tròn trịa, ấn nhẹ thấy lún đều mềm tay.", "avg_price_per_kg": 180000
    },
    "BlackCherry": {
        "vn_name": "Cherry đen Washington", "icon": "🍒", "calories": "65 kcal / 100g",
        "vitamins": "Anthocyanin siêu đậm đặc, Melatonin, Kali",
        "benefits": "Giảm axit uric trong máu cho người bệnh gút, giúp ngủ sâu giấc.",
        "tips": "Quả to cỡ 30-32mm, màu đen đỏ thẫm, cuống xanh tươi bóng loáng.", "avg_price_per_kg": 380000
    },
    "RainierCherry": {
        "vn_name": "Cherry vàng Rainier", "icon": "🍒", "calories": "68 kcal / 100g",
        "vitamins": "Hàm lượng đường tự nhiên cao, Vitamin A, C, Canxi",
        "benefits": "Vua các loại cherry: vị ngọt đậm đà quý phái, bồi bổ tế bào tim.",
        "tips": "Màu vàng kem ửng hồng phớt đỏ, vỏ mỏng căng mọng, hạt nhỏ li ti.", "avg_price_per_kg": 480000
    },
    "WhitePeach": {
        "vn_name": "Đào trắng Nhật Bản", "icon": "🍑", "calories": "41 kcal / 100g",
        "vitamins": "Nước 89%, Vitamin C, Axit amin thiết yếu",
        "benefits": "Vị ngọt thanh tan trong miệng, làm dịu cơn khát, nhuận da chống nếp nhăn.",
        "tips": "Quả to tròn cân đối, vỏ màu trắng hồng phớt, hương thơm nồng nàn quyến rũ.", "avg_price_per_kg": 250000
    },
    "YellowPeach": {
        "vn_name": "Đào vàng Lạng Sơn", "icon": "🍑", "calories": "40 kcal / 100g",
        "vitamins": "Carotenoid tạo màu vàng, Vitamin C, Chất xơ",
        "benefits": "Thịt giòn đanh, dùng ngâm trà đào bổ dưỡng thanh mát cơ thể.",
        "tips": "Quả có mỏ quạ nhẹ, vỏ vàng ửng đỏ, thịt dính hạt giòn rụm thơm dịu.", "avg_price_per_kg": 50000
    },
    "Nectarine": {
        "vn_name": "Đào tiên lông nhẵn (Nectarine)", "icon": "🍑", "calories": "44 kcal / 100g",
        "vitamins": "Vitamin A, C, Kali, Lutein",
        "benefits": "Không có lông tơ gây ngứa, vỏ ăn liền giòn ngọt, tốt cho thị lực.",
        "tips": "Vỏ bóng loáng đỏ vàng xen kẽ, nắn chắc tay, vị ngọt đậm pha chua dịu.", "avg_price_per_kg": 110000
    },
    "BlackPlum": {
        "vn_name": "Mận đen Mỹ", "icon": "🟣", "calories": "48 kcal / 100g",
        "vitamins": "Sorbitol, Isatin điều hòa đường ruột, Sắt, Vitamin C",
        "benefits": "Hỗ trợ tiêu hóa cực mạnh, phòng ngừa táo bón, tăng lượng máu.",
        "tips": "Quả to gấp 3 mận thường, màu tím đen thẫm, thịt vàng hổ phách ngọt lịm.", "avg_price_per_kg": 130000
    },
    "RedPlum": {
        "vn_name": "Mận đỏ Tam Hoa", "icon": "🔴", "calories": "45 kcal / 100g",
        "vitamins": "Axit malic, Anthocyanin, Vitamin C",
        "benefits": "Kích thích enzym dịch vị, giải nhiệt mùa hè, làm sạch khoang miệng.",
        "tips": "Quả to tròn phủ lớp phấn trắng xóa, màu đỏ tươi rực rỡ, giòn ngọt róc hạt.", "avg_price_per_kg": 45000
    },
    "Greengage": {
        "vn_name": "Mận xanh Reine Claude", "icon": "🍏", "calories": "46 kcal / 100g",
        "vitamins": "Vitamin C, Kali, Đường tự nhiên",
        "benefits": "Vị ngọt mật đặc trưng của Pháp, bổ sung khoáng chất vi lượng.",
        "tips": "Quả tròn nhỏ màu xanh lục ngả vàng, có lớp phấn mờ, thịt mọng mật ngọt.", "avg_price_per_kg": 160000
    },
    "HamiMelon": {
        "vn_name": "Dưa Hami Tân Cương", "icon": "🍈", "calories": "35 kcal / 100g",
        "vitamins": "Đường Fructose, Vitamin C, Axit Folic, Kali",
        "benefits": "Được mệnh danh 'Vua dưa lưới': giòn tan ngọt sắc, giải nhiệt cơ thể cực tốt.",
        "tips": "Dáng bầu dục dài, vân lưới xám trắng dày nổi cộm, cuống khô héo tự nhiên.", "avg_price_per_kg": 65000
    },
    "SugarBabyWatermelon": {
        "vn_name": "Dưa hấu tí hon Sugar Baby", "icon": "🍉", "calories": "31 kcal / 100g",
        "vitamins": "Lycopene chống oxy hóa, Vitamin A, C",
        "benefits": "Vừa vặn cho 1 người ăn, ruột đỏ au ngọt lịm từ tâm ra sát mép vỏ.",
        "tips": "Quả nhỏ cỡ bàn tay, vỏ xanh đen tuyền không sọc, gõ nghe tiếng thanh giòn.", "avg_price_per_kg": 28000
    },
    "YellowWatermelon": {
        "vn_name": "Dưa hấu ruột vàng", "icon": "🍉", "calories": "30 kcal / 100g",
        "vitamins": "Beta-carotene tạo màu vàng, Nước 92%, Vitamin C",
        "benefits": "Mát gan, thanh nhiệt, hương vị ngọt thanh nhẹ nhàng khác biệt dưa đỏ.",
        "tips": "Vỏ sọc sáng màu, cuống nhỏ xoăn tít, ruột màu vàng óng ả không xốp.", "avg_price_per_kg": 30000
    },
    "BlackWatermelon": {
        "vn_name": "Dưa hấu vỏ đen Densuke", "icon": "🍉", "calories": "32 kcal / 100g",
        "vitamins": "Độ ngọt cao cấp Brix 13+, Lycopene, Kali",
        "benefits": "Thượng phẩm dưa hấu Nhật Bản: độ giòn đanh đỉnh cao, giải độc cơ thể.",
        "tips": "Vỏ ngoài đen bóng loáng không tì vết, ruột đỏ thắm đậm đà hương thơm.", "avg_price_per_kg": 200000
    },
    "ElephantApple": {
        "vn_name": "Quả sổ (Trái chay rừng)", "icon": "🍏", "calories": "59 kcal / 100g",
        "vitamins": "Axit hữu cơ, Tannin, Vitamin C, Chất xơ",
        "benefits": "Nấu canh chua thanh nhiệt, hỗ trợ chữa đau nhức xương khớp mùa lạnh.",
        "tips": "Vỏ xanh cứng nhiều lớp cánh ôm chặt lấy nhau, quả già có mùi thơm thảo mộc.", "avg_price_per_kg": 35000
    },
    "IndianGooseberry": {
        "vn_name": "Me rừng (Quả mắc kham)", "icon": "🍏", "calories": "44 kcal / 100g",
        "vitamins": "Vitamin C cao kỷ lục (gấp 20 lần cam), Axit Gallic",
        "benefits": "Ban đầu chua chát sau ngọt hậu kéo dài: bổ phổi trị ho, làm chậm lão hóa.",
        "tips": "Quả tròn mờ có 6 khía mờ, màu xanh vàng nhạt, hạt cứng vị ngọt hậu sâu.", "avg_price_per_kg": 45000
    },
    "Macadamia": {
        "vn_name": "Quả mắc ca tươi", "icon": "🌰", "calories": "718 kcal / 100g",
        "vitamins": "Chất béo không bão hòa Palmitoleic, Vitamin B1, Magie",
        "benefits": "Nữ hoàng hạt dinh dưỡng: bảo vệ tim mạch, phát triển tế bào não thai nhi.",
        "tips": "Vỏ xanh bên ngoài căng tròn không sâu mọt, nhân bên trong trắng sữa thơm ngậy.", "avg_price_per_kg": 95000
    },
    "Chestnut": {
        "vn_name": "Hạt dẻ Trùng Khánh", "icon": "🌰", "calories": "213 kcal / 100g",
        "vitamins": "Giàu tinh bột phức hợp, Vitamin C, B1, B2, Canxi",
        "benefits": "Bổ thận ích khí, chắc khỏe gân cốt, cung cấp năng lượng ấm mùa đông.",
        "tips": "Vỏ ngoài phủ lớp lông tơ mịn màu hạt dẻ sáng, lắc không kêu lọc xọc.", "avg_price_per_kg": 75000
    },
    "CashewApple": {
        "vn_name": "Trái điều (Đào lộn hột)", "icon": "🟡", "calories": "53 kcal / 100g",
        "vitamins": "Vitamin C gấp 5 lần cam, Vitamin B2, Canxi",
        "benefits": "Tăng cường năng lượng, chống oxy hóa, nước ép quả điều giải nhiệt cực tốt.",
        "tips": "Quả màu đỏ vàng rực rỡ, thịt mọng nước, hạt điều gắn chặt phía đuôi quả.", "avg_price_per_kg": 25000
    },
    "Salak": {
        "vn_name": "Quả mây Thái (Da rắn)", "icon": "🥔", "calories": "82 kcal / 100g",
        "vitamins": "Pectin, Canxi, Kali, Beta-carotene, Sắt",
        "benefits": "Tốt cho trí nhớ, làm săn chắc cơ bắp, hỗ trợ điều hòa nhịp tim ổn định.",
        "tips": "Vỏ nâu vảy rắn bóng đẹp, gai li ti rụng bớt, bóc ra múi trắng ngà giòn ngọt.", "avg_price_per_kg": 65000
    },
    "SnakeFruit": {
        "vn_name": "Quả mây Bali Indonesia", "icon": "🥔", "calories": "80 kcal / 100g",
        "vitamins": "Tanin, Flavonoid, Vitamin C, Chất xơ",
        "benefits": "Hỗ trợ giảm cân, tạo cảm giác no lâu, chống lại các tác nhân oxy hóa.",
        "tips": "Vỏ nâu đen vảy xếp lớp, mùi thơm mít hòa quyện dứa, múi khô ráo giòn sần sật.", "avg_price_per_kg": 85000
    },
    "MiracleFruit": {
        "vn_name": "Quả thần kỳ (Miracle Fruit)", "icon": "🍒", "calories": "30 kcal / 100g",
        "vitamins": "Protein Miraculin biến vị chua thành ngọt lịm",
        "benefits": "Giúp người tiểu đường cảm nhận vị ngọt tự nhiên mà không tăng đường huyết.",
        "tips": "Quả màu đỏ mọng như quả nhót nhỏ, ăn cả vỏ nhai kỹ trước khi nếm đồ chua.", "avg_price_per_kg": 250000
    },
    "Jabuticaba": {
        "vn_name": "Nho thân gỗ Nam Mỹ", "icon": "🟣", "calories": "45 kcal / 100g",
        "vitamins": "Hợp chất Jaboticabin, Anthocyanin, Vitamin C",
        "benefits": "Mọc trực tiếp trên thân cây gỗ: kháng viêm mạnh, ngăn ngừa lão hóa sớm.",
        "tips": "Quả mọc bám dày đặc thân cây, màu tím đen bóng, thịt trong ngọt mát như nho.", "avg_price_per_kg": 220000
    },
    "Pitomba": {
        "vn_name": "Dâu rừng Amazon (Pitomba)", "icon": "🟡", "calories": "40 kcal / 100g",
        "vitamins": "Vitamin C, Axit Citric, Beta-cryptoxanthin",
        "benefits": "Tăng cường sức đề kháng cho đường ruột, làm dịu các cơn khát.",
        "tips": "Vỏ màu vàng cam nhẵn mịn, bóc nhẹ thấy lớp cùi mềm vị chua ngọt thanh.", "avg_price_per_kg": 180000
    },
    "Canistel": {
        "vn_name": "Quả trứng gà (Lêkima)", "icon": "🟡", "calories": "138 kcal / 100g",
        "vitamins": "Niacin (Vitamin B3), Beta-carotene, Sắt, Chất xơ",
        "benefits": "Bồi bổ thần kinh, chống suy nhược cơ thể, hạ mỡ máu, làm sáng mắt.",
        "tips": "Quả chín vàng ươm, vỏ mềm đều, thịt dẻo quánh bùi bùi béo ngậy như lòng đỏ trứng.", "avg_price_per_kg": 35000
    },
    "Ambarella": {
        "vn_name": "Cóc (Cóc bao tử)", "icon": "🍏", "calories": "48 kcal / 100g",
        "vitamins": "Axit hữu cơ, Vitamin C, Sắt, Canxi",
        "benefits": "Kích thích tiêu hóa, giải nhiệt, hỗ trợ giảm cân, chống thiếu máu.",
        "tips": "Cóc bao tử nhỏ đều hạt lép, vỏ xanh láng, cắn giòn sần sật chấm muối ớt.", "avg_price_per_kg": 25000
    },
    "Dracontomelon": {
        "vn_name": "Quả sấu Hà Nội", "icon": "🍏", "calories": "38 kcal / 100g",
        "vitamins": "Axit Citric, Axit Malic, Vitamin C, Canxi",
        "benefits": "Đặc sản mùa hè: giải nhiệt thanh nhiệt, ngâm nước uống tiêu thực trị nhiệt miệng.",
        "tips": "Sấu bánh tẻ vỏ hơi sần rám nhẹ, thịt dày hạt nhỏ, bấm vào thấy giòn mọng.", "avg_price_per_kg": 30000
    }
}

