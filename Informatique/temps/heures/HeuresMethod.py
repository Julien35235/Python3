def openfilleHeuresMethod():
    import datetime

    sunrise_sunset = {
        "New-York": ("05:25", "20:31"),
        "Boston": ("05:07", "20:25"),
        "Dinard": ("05:00", "21:47"),
        "Rennes": ("05:03", "21:49"),
        "Paris": ("05:26", "21:59"),
        "Le Mans": ("05:31", "22:08"),
        "Bordeaux": ("06:05", "22:05"),
        "Caen": ("05:20", "21:49"),
        "Rouen": ("05:23", "21:54"),
        "Amiens": ("05:16", "21:50"),
        "Compiègne": ("05:14", "21:50"),
        "Reims": ("05:11", "21:53"),
        "Cabourg": ("05:18", "21:47"),
        "Bar-le-Duc": ("05:23", "21:52"),
        "Nancy": ("05:27", "21:56"),
        "Metz": ("05:30", "21:59"),
        "Troyes": ("05:15", "21:50"),
        "Lyon": ("05:38", "21:55"),
        "Grenoble": ("05:45", "21:57"),
        "Valence": ("05:43", "21:57"),
        "Avignon": ("05:51", "21:57"),
        "Lunel": ("05:52", "21:39"),
        "Nîmes": ("05:54", "21:43"),
        "Montpellier": ("05:55", "21:42"),
        "Carcassonne": ("06:01", "21:40"),
        "Toulouse": ("06:10", "21:49"),
        "Montauban": ("06:08", "21:47"),
        "Angoulême": ("05:39", "22:06"),
        "Nantes": ("05:29", "22:07"),
        "Niort": ("05:36", "22:07"),
        "Poitiers": ("05:37", "22:04"),
        "Bourges": ("05:28", "21:59"),
        "Blois": ("05:32", "21:59"),
        "Créteil": ("05:28", "21:59"),
        "Limoges": ("05:48", "22:10"),
        "Brive-la-Gaillarde": ("05:47", "22:10"),
        "Cahors": ("06:00", "22:09"),
        "Clermont-Ferrand": ("05:56", "22:10"),
        "Lège-Cap-Ferret": ("06:18", "22:07"),
        "Arès": ("06:18", "22:07"),
        "Andernos-les-Bains": ("06:18", "22:07"),
        "Biganos": ("06:18", "22:07"),
        "Arcachon": ("06:18", "22:07"),
        "Cap Ferret": ("06:18", "22:07"),
        "Rennes": ("05:03", "21:49"),
        "Laval": ("05:06", "21:48"),
        "Fougères": ("05:03", "21:49"),
        "Romagné": ("05:05", "21:49"),
        "Milan": ("05:39", "21:03"),
        "Venise": ("05:28", "20:56"),
        "Turin": ("05:37", "21:12"),
        "Rome": ("05:37", "20:49"),
        "Palerme": ("05:34", "20:51"),
        "Catane": ("05:22", "20:51"),
        "Héraklion": ("05:48", "21:08"),
        "La Canée": ("05:43", "21:08"),
        "Le Caire": ("04:52", "18:55"),
        "Jérusalem": ("05:29", "19:40"),
        "Amman": ("04:55", "19:30"),
        "Al-'Ula": ("05:29", "19:51"),
        "Al-Madinah": ("05:18", "19:39"),
        "Riyad": ("05:25", "19:45"),
        "Manama": ("04:52", "18:48"),
        "Doha": ("04:46", "18:27"),
        "Dubaï": ("05:36", "19:52"),
        "Mascate": ("05:08", "18:57"),
        "Colombo": ("05:43", "18:46"),
        "Bangalore": ("05:59", "18:44"),
        "Abidjan": ("05:52", "18:42"),
        "Accra": ("05:52", "18:48"),
        "Libreville": ("06:07", "18:27"),
        "Conakry": ("05:36", "18:35"),
        "Dakar": ("06:50", "19:54"),
        "Casablanca": ("06:31", "21:06"),
        "Madrid": ("06:45", "21:46"),
        "Barcelone": ("06:20", "21:29"),
        "Bilbao": ("06:35", "21:44"),
        "Palma": ("06:21", "21:35"),
        "Lisbonne": ("06:19", "21:05"),
        "Vigo": ("06:13", "21:11"),
        "Porto": ("06:11", "21:18"),
        "Séville": ("06:26", "21:38"),
        "Cadix": ("06:27", "21:39"),
        "Gibraltar": ("06:14", "21:29"),
        "Málaga": ("06:34", "21:54"),
        "Tunis": ("05:25", "20:10"),
        "Tripoli": ("05:26", "19:50"),
        "Funchal": ("06:16", "21:00"),
        "Las Palmas de Gran Canaria": ("06:33", "20:55"),
        "Monterrey": ("06:29", "20:16"),
        "León": ("06:18", "20:20"),
        "Managua": ("05:23", "18:24"),
        "San José": ("05:18", "18:28"),
        "Bogota": ("05:36", "18:13"),
        "Quito": ("06:12", "18:09"),
        "Lima": ("06:22", "17:46"),
        "Trujillo": ("06:14", "17:37"),
        "Rio de Janeiro": ("06:08", "17:03"),
        "São Paulo": ("06:46", "17:14"),
        "Montevideo": ("07:00", "17:32"),
        "Punta Arenas": ("08:29", "17:16"),
        "Îles Falkland (Malvinas)": ("08:02", "17:30"),
        "Santiago": ("07:47", "17:46"),
        "Paramaribo": ("05:40", "18:31"),
        "Dar es Salam": ("06:29", "18:02"),
        "Arusha": ("06:37", "18:12"),
        "Zanzibar": ("06:13", "18:02"),
        "Luanda": ("05:42", "17:51"),
        "Freetown": ("06:33", "18:51"),
        "Niamey": ("05:59", "19:56"),
        "Djouba": ("06:19", "18:49"),
        "Khartoum": ("05:37", "18:48"),
        "Singapour": ("06:52", "18:57"),
        "Jakarta": ("05:50", "17:57"),
        "Surabaya": ("05:31", "17:51"),
        "Yogyakarta": ("05:29", "17:47"),
        "Banyuwangi": ("05:12", "17:37"),
        "Denpasar": ("05:57", "18:03"),
        "Ruteng": ("05:45", "17:58"),
        "Labuan Bajoen": ("05:54", "18:05"),
        "Sydney": ("06:51", "16:53"),
        "Melbourne": ("07:01", "17:01"),
        "Adélaïde": ("07:16", "17:07"),
        "Perth": ("06:44", "17:20"),
        "Darwin": ("06:24", "18:21"),
        "Nouméa": ("06:29", "17:47"),
        "Port Moresby": ("06:15", "18:01"),
        "Port-Vila": ("06:19", "17:18"),
        "Papeete": ("06:41", "17:56"),
        "Bora-Bora": ("06:36", "17:50"),
        "Honolulu": ("05:52", "19:06"),
        "Anchorage": ("04:20", "23:44"),
        "Reykjavik": ("03:22", "23:21"),
        "Longyearbyen": ("02:20", "00:09"),
        "Oslo": ("04:03", "22:45"),
        "Stockholm": ("03:39", "22:06"),
        "Helsinki": ("02:50", "23:01"),
        "Rovaniemi": ("01:59", "23:19"),
        "La Havane": ("05:45", "19:24"),
        "Nassau": ("05:29", "19:50"),
        "Miami": ("05:45", "20:11"),
        "Dallas": ("06:20", "20:34"),
        "Washington": ("05:43", "20:33"),
        "Atlanta": ("06:30", "20:51"),
        "Las Vegas": ("05:23", "19:53"),
        "Los Angeles": ("05:42", "19:57"),
        "San Francisco": ("05:47", "20:34"),
        "Sacramento": ("05:45", "20:26"),
        "Seattle": ("05:11", "21:09"),
        "Vancouver": ("05:07", "21:26"),
        "Portland": ("05:21", "21:12"),
        "Winnipeg": ("04:43", "21:21"),
        "Calgary": ("04:32", "21:37"),
        "Edmonton": ("04:30", "21:51"),
        "Ottawa": ("05:14", "20:55"),
        "Montréal": ("05:07", "20:55"),
        "Québec": ("04:54", "21:01"),
        "Toronto": ("05:29", "20:57"),
        "Kansas City": ("05:51", "20:50"),
        "Dublin": ("04:55", "21:57"),
        "Londres": ("04:45", "21:20"),
        "Manchester": ("04:42", "21:30"),
        "Liverpool": ("04:44", "21:34"),
        "Glasgow": ("04:42", "21:41"),
        "Édimbourg": ("04:34", "21:46"),
        "Aberdeen": ("04:15", "21:58"),
        "Tórshavn": ("03:33", "23:23"),
        "Bucarest": ("05:42", "20:17"),
        "Iaşi": ("05:34", "20:34"),
        "Cluj-Napoca": ("05:47", "20:49"),
        "Braşov": ("05:41", "20:36"),
        "Budapest": ("05:03", "20:27"),
        "Vienne": ("04:46", "20:48"),
        "Salzbourg": ("04:40", "20:51"),
        "Prague": ("04:58", "21:14"),
        "Varsovie": ("04:28", "21:03"),
        "Tallinn": ("04:07", "22:05"),
        "Riga": ("04:05", "22:03"),
        "Hô Chi Minh-Ville": ("05:25", "18:06"),
        "Hanoï": ("05:24", "18:37"),
        "Phnom Penh": ("05:25", "18:38"),
        "Manille": ("05:24", "18:36"),
        "Naypyidaw": ("05:16", "18:36"),
        "Chittagong": ("04:52", "18:40"),
        "Dacca": ("04:51", "18:45"),
        "Katmandou": ("05:06", "18:43"),
        "Karachi": ("04:55", "19:25"),
        "Hyderâbâd": ("05:18", "18:47")
    }

    def get_sunrise_sunset(city):
        if city in sunrise_sunset:
            return sunrise_sunset[city]
        else:
            return None

    def print_sunrise_sunset(city, sunrise, sunset):
        print(f"Lever du soleil à {city}: {sunrise}")
        print(f"Coucher du soleil à {city}: {sunset}")

    def main():
        print("Bienvenue ! Veuillez choisir une ville :")
        print("1. New York")
        print("2. Boston")
        print("3. Dinard")
        print("4. Rennes")
        print("5. Paris")
        print("6. Le Mans")
        print("7. Bordeaux")
        print("8. Caen")
        print("9. Rouen")
        print("10. Amiens")
        print("11. Compiègne")
        print("12. Reims")
        print("13. Cabourg")
        print("14. Bar-le-Duc")
        print("15. Nancy")
        print("16. Metz")
        print("17. Troyes")
        print("18. Lyon")
        print("19. Grenoble")
        print("20. Valence")
        print("21. Avignon")
        print("22. Lunel")
        print("23. Nîmes")
        print("24. Montpellier")
        print("25. Carcassonne")
        print("26. Toulouse")
        print("27. Montauban")
        print("28. Angoulême")
        print("29. Nantes")
        print("30. Niort")
        print("31. Poitiers")
        print("32. Bourges")
        print("33. Blois")
        print("34. Créteil")
        print("35. Limoges")
        print("36. Brive-la-Gaillarde")
        print("37. Cahors")
        print("38. Clermont-Ferrand")
        print("39. Lège-Cap-Ferret")
        print("40. Arès")
        print("41. Andernos-les-Bains")
        print("42. Biganos")
        print("43. Arcachon")
        print("44. Cap Ferret")
        print("45. Rennes")
        print("46. Laval")
        print("47. Fougères")
        print("48. Romagné")
        print("49. Milan")
        print("50. Venise")
        print("51. Turin")
        print("52. Rome")
        print("53. Palerme")
        print("54. Catane")
        print("55. Héraklion")
        print("56. La Canée")
        print("57. Le Caire")
        print("58. Jérusalem")
        print("59. Amman")
        print("60. Al-'Ula")
        print("61. Al-Madinah")
        print("62. Riyad")
        print("63. Manama")
        print("64. Doha")
        print("65. Dubaï")
        print("66. Mascate")
        print("67. Colombo")
        print("68. Bangalore")
        print("69. Abidjan")
        print("70. Accra")
        print("71. Libreville")
        print("72. Conakry")
        print("73. Dakar")
        print("74. Casablanca")
        print("75. Madrid")
        print("76. Barcelone")
        print("77. Bilbao")
        print("78. Palma")
        print("79. Lisbonne")
        print("80. Vigo")
        print("81. Porto")
        print("82. Séville")
        print("83. Cadix")
        print("84. Gibraltar")
        print("85. Málaga")
        print("86. Tunis")
        print("87. Tripoli")
        print("88. Funchal")
        print("89. Las Palmas de Gran Canaria")
        print("90. Monterrey")
        print("91. León")
        print("92. Managua")
        print("93. San José")
        print("94. Bogota")
        print("95. Quito")
        print("96. Lima")
        print("97. Trujillo")
        print("98. Rio de Janeiro")
        print("99. São Paulo")
        print("100. Montevideo")
        print("101. Punta Arenas")
        print("102. Îles Falkland (Malvinas)")
        print("103. Santiago")
        print("104. Paramaribo")
        print("105. Dar es Salam")
        print("106. Arusha")
        print("107. Zanzibar")
        print("108. Luanda")
        print("109. Freetown")
        print("110. Niamey")
        print("111. Djouba")
        print("112. Khartoum")
        print("113. Singapour")
        print("114. Jakarta")
        print("115. Surabaya")
        print("116. Yogyakarta")
        print("117. Banyuwangi")
        print("118. Denpasar")
        print("119. Ruteng")
        print("120. Labuan Bajoen")
        print("121. Sydney")
        print("122. Melbourne")
        print("123. Adélaïde")
        print("124. Perth")
        print("125. Darwin")
        print("126. Nouméa")
        print("127. Port Moresby")
        print("128. Port-Vila")
        print("129. Papeete")
        print("130. Bora-Bora")
        print("131. Honolulu")
        print("132. Anchorage")
        print("133. Reykjavik")
        print("134. Longyearbyen")
        print("135. Oslo")
        print("136. Stockholm")
        print("137. Helsinki")
        print("138. Rovaniemi")
        print("139. La Havane")
        print("140. Nassau")
        print("141. Miami")
        print("142. Dallas")
        print("143. Washington")
        print("144. Atlanta")
        print("145. Las Vegas")
        print("146. Los Angeles")
        print("147. San Francisco")
        print("148. Sacramento")
        print("149. Seattle")
        print("150. Vancouver")
        print("151. Portland")
        print("152. Winnipeg")
        print("153. Calgary")
        print("154. Edmonton")
        print("155. Ottawa")
        print("156. Montréal")
        print("157. Québec")
        print("158. Toronto")
        print("159. Kansas City")
        print("160. Dublin")
        print("161. Londres")
        print("162. Manchester")
        print("163. Liverpool")
        print("164. Glasgow")
        print("165. Édimbourg")
        print("166. Aberdeen")
        print("167. Tórshavn")
        print("168. Bucarest")
        print("169. Iaşi")
        print("170. Cluj-Napoca")
        print("171. Braşov")
        print("172. Budapest")
        print("173. Vienne")
        print("174. Salzbourg")
        print("175. Prague")
        print("176. Varsovie")
        print("177. Tallinn")
        print("178. Riga")
        print("179. Hô Chi Minh-Ville")
        print("180. Hanoï")
        print("181. Phnom Penh")
        print("182. Manille")
        print("183. Naypyidaw")
        print("184. Chittagong")
        print("185. Dacca")
        print("186. Katmandou")
        print("187. Karachi")
        print("188. Hyderâbâd")

        city_choice = input("Veuillez entrer le numéro de la ville : ")
        city_choice = int(city_choice)

        if city_choice < 1 or city_choice > 188:
            print("Ville non valide. Veuillez sélectionner un numéro de ville valide.")
            return
        city_sunrise, city_sunset = get_sunrise_sunset(city_name)

        if city_sunrise is None or city_sunset is None:
            print("Impossible d'obtenir les informations sur le lever et le coucher du soleil pour cette ville.")
        else:
            print_sunrise_sunset(city_name, city_sunrise, city_sunset)

    # Exécution du programme principal
    main()

