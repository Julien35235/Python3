def openfilleMeteoMethod():
    import random

    cities = [
    "Dinard", "Rennes", "Châteaubourg", "Saint-Jacques-de-la-Lande", "Ploërmel",
    "Quimper", "Douarnenez", "Crozon", "Brest", "Lannion", "Guingamp", "Saint-Brieuc", "Saint-Malo",
    "Cancale", "Saint-Méloir-des-Ondes", "Combourg", "Mordelles", "Le Rheu", "Paris", "Châteauroux",
    "Le Plessis-Belleville", "Roissy-en-France", "Saint-Denis", "Nanterre", "La Défense", "Suresnes",
    "Boulogne-Billancourt", "Bezons", "Pontoise", "Vincennes", "Lognes", "Torcy", "Lagny-sur-Marne",
    "Thorigny-sur-Marne", "Marne-la-Vallée", "Noisy-le-Grand", "Versailles", "Massy", "Antony",
    "Saint-Arnoult-en-Yvelines", "Rambouillet", "Maintenon", "Saint-Piat", "Yermenonville", "Armenonville", "Gallardon", "Gas",
    "Saint-Prest","Jouy", "Soulaires", "Gasville-Oisème", "Coltainville", "Champhol", "Nogent-le-Roi", "Chaudon",
    "Le Gué-de-Longroi", "Ablis", "Auneau-Bleury-Saint-Symphorien", "Aunay-sous-Auneau", "Villiers-le-Morhier",
    "Épernon", "Houx", "Chartres", "Le Mans", "Bordeaux", "Caen", "Rouen", "Amiens", "Compiègne", "Reims",
    "Cabourg", "Bar-le-Duc", "Nancy", "Metz", "Chambley-Bussières", "Hagéville", "Lachaussée",
    "Saint-Julien-lès-Gorze", "Mars-la-Tour", "Jarny", "Doncourt-lès-Conflans", "Tronville", "Troyes",
    "Lyon", "Grenoble", "Strasbourg", "Besançon", "Saint-Hilaire-du-Touvet", "Le Touvet", "La Terrasse",
    "Chambéry", "La Tour-du-Pin", "Romans-sur-Isère", "Valence", "Avignon", "Lunel", "Nîmes", "Montpellier",
    "Toulon", "Pierrefeu-du-Var", "Marseille", "Carcassonne", "Toulouse", "Montauban", "Angoulême",
    "Nantes", "Niort", "Poitiers", "Bourges", "Blois", "Créteil", "Limoges", "Brive-la-Gaillarde",
    "Cahors", "Clermont-Ferrand", "Lège-Cap-Ferret", "Arès", "Andernos-les-Bains", "Biganos", "Arcachon",
    "Cap Ferret", "Laval", "Fougères", "Romagné", "Saint-Aubin-du-Cormier", "Liffré", "Thorigné-Fouillard",
    "Vitré", "Flers", "Alençon", "Dreux", "Fontainebleau", "Melun", "Château-Tierry", "Meaux", "Calais", "Lille",
    "Betton", "Melesse", "La Mézière", "Saint Sulpice-la-Forêt", "Chevaigné", "La Bouëxière", "La Chapelle-des-Fougeretz",
    "Vignoc", "Pacé", "Chantepie", "Noyal-sur-Vilaine", "Acigné", "Cesson-Sévigné", "Servon-sur-Vilaine", "Brécé",
    "Domloup", "Vern-sur-Seiche", "Chartres-de-Bretagne", "Bruz", "Pont-Péan", "Guichen",
    "Milan", "Venise", "Rome", "Palerme", "Catane", "Héraklion", "La Canée", "Réthymnon", "Kissamos",
    "Sougia", "Paleóchora", "Fira", "Oia", "Kamari Καμάρι", "Athènes", "Ankara", "Istanbul", "Konya", "Antalya",
    "Nicosie", "Larnaca Λάρνακα","Le Caire", "Jérusalem", "Tel-Aviv", "Amman", "Madaba", "Ma'in", "Al-Karak", "Dana",
    "Ma'an", "Petra", "Wadi Rum Village", "Aqaba","Swemeh", "Al-'Ula", "Al-Madinah", "Riyad", "Manama","Doha",
    "Dubaï", "Mascate", "Colombo", "Bangalore","Abidjan", "Accra","Libreville", "Conakry", "Dakar", "Casablanca",
    "Madrid", "Barcelone", "Bilbao", "Palma", "Lisbonne", "Vigo", "Porto","Séville", "Cadix", "Gibraltar",
    "Málaga","Tunis", "Tripoli","Funchal", "Las Palmas de Gran Canaria", "Monterrey",
    "León", "Managua", "San José", "Bogota", "Quito","Lima", "Trujillo", "Rio de Janeiro", "São Paulo", "Montevideo", "Punta Arenas",
    "Îles Falkland (Malvinas)","Santiago", "Paramaribo", "Dar es Salam", "Arusha", "Zanzibar", "Luanda", "Freetown", "Niamey", "Djouba",
    "Khartoum", "Singapour", "Jakarta", "Surabaya", "Yogyakarta", "Banyuwangi", "Denpasar", "Ruteng",
    "Labuan Bajoen", "Sydney", "Melbourne", "Adélaïde", "Perth", "Darwin", "Nouméa", "Poum", "Koumac",
    "Koné", "Moméa", "Dumbéa", "La Coulée", "Prony", "Goro", "Konoé-Chaoué", "Nandaï", "Port Moresby",
    "Port-Vila", "Papeete", "Bora-Bora", "Honolulu", "Anchorage", "Qamani'tuaq", "Reykjavik",
    "Longyearbyen", "Oslo", "Stockholm", "Helsinki", "Rovaniemi", "La Havane", "Nassau", "San Juan",
    "Saint-Domingue", "Port-au-Prince","Ponce", "Fort-de-France", "Pointe-à-Pitre", "Miami", "Dallas",
    "New-York", "Boston", "Washington", "Atlanta", "Las Vegas", "Los Angeles", "San Francisco",
    "Sacramento", "Seattle", "Vancouver","Portland", "Winnipeg","Calgary", "Edmonton", "Ottawa", "Montréal",
    "Saint-Pierre-et-Miquelon","Saguenay", "Trois-Rivières","Québec", "Toronto", "Kansas City", "Dublin", "Londres",
    "Manchester", "Liverpool","Glasgow","Édimbourg", "Aberdeen", "Tórshavn", "Îles Féroé", "Bucarest", "Iaşi",
    "Cluj-Napoca", "Braşov","Budapest", "Vienne", "Salzbourg", "Prague", "Varsovie", "Tallinn", "Riga", "Hô Chi Minh-Ville",
    "Hanoï", "Phnom Penh", "Bangkok", "Manille", "Cebu",  "Naypyidaw", "Chittagong", "Dacca", "Katmandou",
    "Karachi", "Hyderâbâd"
    ]

    def get_weather(city):
        weather_conditions = ["Ensoleillé", "Nuageux", "Pluie", "Brume", "Orages"]
        return random.choice(weather_conditions)

    def get_humidity():
        return random.randint(0, 100)

    def get_wind_speed():
        return random.randint(0, 50)

    def get_gust_speed():
        return random.randint(0, 70)

    def display_weather(city):
        weather = get_weather(city)
        print(f"Les conditions météorologiques à {city} est: {weather}.")

    def display_humidity():
        humidity = get_humidity()
        print(f"L'humidité est de : {humidity}%.")

    def display_wind_speed():
        wind_speed = get_wind_speed()
        print(f"La vitesse du vent est de : {wind_speed} km/h.")

    def display_gust_speed():
        gust_speed = get_gust_speed()
        print(f"La vitesse des rafales est de : {gust_speed} km/h.")

    def display_city_menu():
        print("Sélectionnez une ville :")
        for i, city in enumerate(cities, start=1):
            print(f"{i}. {city}")

    def display_main_menu():
        print("=== Menu Principal ===")
        print("1. Précipitations")
        print("2. Humidité")
        print("3. Vent")
        print("4. Rafale")
        print("5. Ensoleillé")
        print("6. Nuageux")
        print("7. Pluie")
        print("8. Brume")
        print("9. Orages")
        print("0. Quitter")

    # Programme principal
    while True:
        display_main_menu()
        choice = input("Sélectionnez une option : ")

        if choice == "0":
            print("Au revoir !")
            break

        if choice == "1":
            display_city_menu()
            city_choice = int(input("Sélectionnez une ville : "))
            city = cities[city_choice - 1]
            display_weather(city)

        if choice == "2":
            display_humidity()

        if choice == "3":
            display_wind_speed()

        if choice == "4":
            display_gust_speed()

        if choice == "5":
            display_city_menu()
            city_choice = int(input("Sélectionnez une ville : "))
            city = cities[city_choice - 1]
            display_weather(city)

        if choice == "6":
            display_city_menu()
            city_choice = int(input("Sélectionnez une ville : "))
            city = cities[city_choice - 1]
            display_weather(city)

        if choice == "7":
            display_city_menu()
            city_choice = int(input("Sélectionnez une ville : "))
            city = cities[city_choice - 1]
            display_weather(city)

        if choice == "8":
            display_city_menu()
            city_choice = int(input("Sélectionnez une ville : "))
            city = cities[city_choice - 1]
            display_weather(city)

        if choice == "9":
            display_city_menu()
            city_choice = int(input("Sélectionnez une ville : "))
            city = cities[city_choice - 1]
            display_weather(city)

        input("Appuyez sur Entrée pour continuer...")