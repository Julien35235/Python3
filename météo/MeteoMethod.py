def openfilleMeteoMethod():
    import random

    cities = [
        "New-York", "Boston", "Dinard", "Rennes", "Paris", "Le Mans", "Bordeaux", "Caen", "Rouen", "Amiens",
        "Compiègne", "Reims", "Cabourg", "Bar-le-Duc", "Nancy", "Metz", "Troyes", "Lyon", "Grenoble", "Valence",
        "Avignon", "Lunel", "Nîmes", "Montpellier", "Carcassonne", "Toulouse", "Montauban", "Angoulême", "Nantes",
        "Niort", "Poitiers", "Bourges", "Blois", "Créteil", "Limoges", "Brive-la-Gaillarde", "Cahors",
        "Clermont-Ferrand","Lège-Cap-Ferret", "Arès", "Andernos-les-Bains", "Biganos", "Arcachon", "Cap Ferret", "Laval", "Fougères",
        "Romagné", "Milan", "Venise", "Turin", "Rome", "Palerme", "Catane", "Héraklion", "La Canée", "Le Caire", "Jérusalem",
        "Amman", "Al-'Ula", "Al-Madinah", "Riyad", "Manama", "Doha", "Dubaï", "Mascate", "Colombo", "Bangalore",
        "Abidjan", "Accra", "Libreville", "Conakry", "Dakar", "Casablanca", "Madrid", "Barcelone", "Bilbao", "Palma",
        "Lisbonne", "Vigo", "Porto", "Séville", "Cadix", "Gibraltar", "Málaga", "Tunis", "Tripoli", "Funchal",
        "Las Palmas de Gran Canaria", "Monterrey", "León", "Managua", "San José", "Bogota", "Quito", "Lima",
        "Trujillo", "Rio de Janeiro", "São Paulo", "Montevideo", "Punta Arenas", "Îles Falkland (Malvinas)", "Santiago",
        "Paramaribo", "Dar es Salam", "Arusha", "Zanzibar", "Luanda", "Freetown", "Niamey", "Djouba", "Khartoum",
        "Singapour", "Jakarta", "Surabaya", "Yogyakarta", "Banyuwangi", "Denpasar", "Ruteng", "Labuan Bajoen", "Sydney",
        "Melbourne", "Adélaïde", "Perth", "Darwin", "Nouméa", "Port Moresby", "Port-Vila", "Papeete", "Bora-Bora",
        "Honolulu", "Anchorage", "Reykjavik", "Longyearbyen", "Oslo", "Stockholm", "Helsinki", "Rovaniemi", "La Havane",
        "Nassau", "Miami", "Dallas", "Washington", "Atlanta", "Las Vegas", "Los Angeles", "San Francisco", "Sacramento",
        "Seattle", "Vancouver", "Portland", "Winnipeg", "Calgary", "Edmonton", "Ottawa", "Montréal", "Québec",
        "Toronto", "Kansas City", "Dublin", "Londres", "Manchester", "Liverpool", "Glasgow", "Édimbourg", "Aberdeen",
        "Tórshavn", "Îles Féroé", "Bucarest", "Iaşi", "Cluj-Napoca", "Braşov", "Budapest", "Vienne", "Salzbourg",
        "Prague", "Varsovie", "Tallinn", "Riga", "Hô Chi Minh-Ville", "Hanoï", "Phnom Penh", "Bangkok", "Manille",
        "Naypyidaw", "Chittagong", "Dacca", "Katmandou", "Karachi", "Hyderâbâd"
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