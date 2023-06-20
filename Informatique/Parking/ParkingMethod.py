def openfilleParkingMethod():
    def afficher_menu():
        print("=== Menu principal ===")
        print("1. Afficher les places de parking disponibles")
        print("2. Réserver une place de parking")
        print("3. Quitter")

    def afficher_places_de_parking(villes):
        print("Voici les places de parking disponibles :")
        for i, ville in enumerate(villes, 1):
            print(f"{i}. {ville}")

    def reserver_place_de_parking(villes):
        afficher_places_de_parking(villes)
        choix = input("Sélectionnez le numéro de la ville pour réserver une place de parking : ")
        try:
            choix = int(choix)
            if choix < 1 or choix > len(villes):
                raise ValueError
            ville_selectionnee = villes[choix - 1]
            email = input("Entrez votre adresse e-mail : ")
            password = input("Entrez votre mot de passe : ")
            immatriculation = input("Entrez le numéro de plaque d'immatriculation : ")
            heure_arrivee = input("Entrez l'heure d'arrivée : ")
            print(f"Vous avez réservé une place de parking à {ville_selectionnee}.")
            print("Détails de la réservation :")
            print(f"Adresse e-mail : {email}")
            print(f"Numéro de plaque d'immatriculation : {immatriculation}")
            print(f"Heure d'arrivée : {heure_arrivee}")
        except ValueError:
            print("Erreur : veuillez entrer un numéro valide.")
        except Exception as e:
            print(f"Erreur : {str(e)}")

    # Liste des villes de parking
    villes = [
        "Dinard", "Rennes", "Châteaubourg", "Saint-Jacques-de-la-Lande", "Ploërmel",
        "Quimper", "Douarnenez", "Crozon", "Brest", "Lannion", "Guingamp", "Saint-Brieuc", "Saint-Malo",
        "Cancale", "Saint-Méloir-des-Ondes", "Combourg", "Mordelles", "Le Rheu", "Paris", "Châteauroux",
        "Le Plessis-Belleville", "Roissy-en-France", "Saint-Denis", "Nanterre", "La Défense", "Suresnes",
        "Boulogne-Billancourt", "Bezons", "Pontoise", "Vincennes", "Lognes", "Torcy", "Lagny-sur-Marne",
        "Thorigny-sur-Marne", "Marne-la-Vallée", "Noisy-le-Grand", "Versailles", "Massy", "Antony",
        "Saint-Arnoult-en-Yvelines", "Rambouillet", "Maintenon", "Saint-Piat", "Yermenonville", "Armenonville",
        "Gallardon", "Gas","Saint-Prest", "Jouy", "Soulaires", "Gasville-Oisème", "Coltainville", "Champhol", "Nogent-le-Roi", "Chaudon",
        "Le Gué-de-Longroi", "Ablis", "Auneau-Bleury-Saint-Symphorien", "Aunay-sous-Auneau", "Villiers-le-Morhier",
        "Épernon", "Houx", "Chartres", "Le Mans", "Bordeaux", "Caen", "Rouen", "Amiens", "Compiègne", "Reims",
        "Cabourg", "Bar-le-Duc", "Nancy", "Metz", "Chambley-Bussières", "Hagéville", "Lachaussée",
        "Saint-Julien-lès-Gorze", "Mars-la-Tour", "Jarny", "Doncourt-lès-Conflans", "Tronville", "Troyes", "Lyon",
        "Grenoble", "Strasbourg", "Besançon", "Saint-Hilaire-du-Touvet", "Le Touvet", "La Terrasse", "Chambéry",
        "La Tour-du-Pin", "Romans-sur-Isère", "Valence", "Avignon", "Lunel", "Nîmes", "Montpellier", "Toulon",
        "Pierrefeu-du-Var", "Marseille", "Carcassonne", "Toulouse", "Montauban", "Angoulême", "Nantes", "Niort",
        "Poitiers", "Bourges", "Blois", "Créteil", "Limoges", "Brive-la-Gaillarde", "Cahors", "Clermont-Ferrand",
        "Lège-Cap-Ferret", "Arès", "Andernos-les-Bains", "Biganos", "Arcachon", "Cap Ferret", "Laval", "Fougères",
        "Romagné", "Saint-Aubin-du-Cormier", "Liffré", "Thorigné-Fouillard", "Vitré", "Flers", "Alençon", "Dreux",
        "Fontainebleau", "Melun", "Château-Tierry", "Meaux", "Calais", "Lille", "Betton", "Melesse", "La Mézière",
        "Saint Sulpice-la-Forêt", "Chevaigné", "La Bouëxière", "La Chapelle-des-Fougeretz", "Vignoc", "Pacé",
        "Chantepie", "Noyal-sur-Vilaine", "Acigné", "Cesson-Sévigné", "Servon-sur-Vilaine", "Brécé", "Domloup",
        "Vern-sur-Seiche", "Chartres-de-Bretagne", "Bruz", "Pont-Péan", "Guichen", "Milan", "Venise", "Rome", "Palerme",
        "Catane", "Héraklion", "La Canée", "Réthymnon", "Kissamos", "Sougia", "Paleóchora", "Fira", "Oia",
        "Kamari Καμάρι", "Athènes", "Ankara", "Istanbul", "Konya", "Antalya", "Nicosie", "Larnaca Λάρνακα", "Le Caire",
        "Louxor الأقصر", "Edfou إدفو", "Kôm Ombo aكوم امبو", "Qena قنا", "Assouan أسوان", "Abou Simbel أبو سمبل السياحية",
        "Hurghada الغردقة", "Port Ghalib بورت غالب", "Marsa Alam مرسى علم", "Port Safaga سفاجا", "Alexandrie الإسكندرية",
        "Jérusalem", "Tel-Aviv", "Amman", "Madaba", "Ma'in", "Al-Karak", "Dana", "Ma'an", "Petra", "Wadi Rum Village",
        "Aqaba", "Swemeh", "Al-'Ula", "Al-Madinah", "Riyad", "Manama", "Doha", "Dubaï", "Mascate", "Colombo",
        "Bangalore", "Abidjan", "Accra", "Libreville", "Conakry", "Dakar", "Bamako", "Kano", "Casablanca", "Madrid", "Barcelone",
        "Bilbao", "Palma", "Lisbonne", "Vigo", "Porto", "Séville", "Cadix", "Gibraltar", "Málaga", "Tunis", "Tripoli",
        "Funchal", "Las Palmas de Gran Canaria", "Monterrey", "León", "Managua", "San José", "Bogota", "Quito", "Lima",
        "Trujillo", "Rio de Janeiro", "São Paulo", "Montevideo", "Punta Arenas", "Îles Falkland (Malvinas)", "Santiago",
        "Paramaribo", "Dar es Salam", "Arusha", "Zanzibar", "Luanda", "Freetown", "Niamey", "Djouba", "Khartoum",
        "Singapour", "Jakarta", "Surabaya", "Yogyakarta", "Banyuwangi", "Denpasar", "Ruteng", "Labuan Bajoen", "Sydney",
        "Melbourne", "Adélaïde", "Perth", "Darwin", "Nouméa", "Poum", "Koumac", "Koné", "Moméa", "Dumbéa", "La Coulée",
        "Prony", "Goro", "Konoé-Chaoué", "Nandaï", "Port Moresby", "Port-Vila", "Papeete", "Bora-Bora", "Honolulu",
        "Anchorage", "Barrow", "Fairbanks", "Pays de Galles", "York", "Seoul", "Incheon", "Pyongyang", "Tokyo", "Osaka",
        "Qamani'tuaq", "Reykjavik", "Longyearbyen", "Barentsburg", "Pyramiden", "Grumantbyen","Ny-Ålesund",
        "Antarctique","Oslo", "Stockholm", "Helsinki", "Rovaniemi",
        "Turku", "Tampere", "Oulu", "Alta", "Selfoss", "Akureyri", "Reyðarfjörður", "Kirkjubæjarklaustur",
        "Flókalundur", "Vík í Mýrdal", "Seyðisfjörður",
        "La Havane", "Nassau", "San Juan", "Saint-Domingue", "Port-au-Prince", "Ponce", "Fort-de-France",
        "Pointe-à-Pitre", "Miami", "Dallas", "New-York", "Boston", "Washington", "Atlanta", "Las Vegas", "Los Angeles",
        "San Francisco", "Sacramento", "Seattle", "Vancouver", "Portland", "Winnipeg", "Calgary", "Edmonton", "Ottawa",
        "Montréal", "Saint-Pierre-et-Miquelon", "Saguenay", "Trois-Rivières", "Québec", "Toronto", "Kansas City",
        "Dublin", "Londres", "Manchester", "Liverpool", "Glasgow", "Édimbourg", "Aberdeen", "Tórshavn", "Îles Féroé",
        "Bucarest", "Iaşi", "Cluj-Napoca", "Braşov", "Budapest", "Vienne", "Salzbourg", "Prague", "Varsovie", "Tallinn",
        "Riga", "Hô Chi Minh-Ville", "Hanoï", "Phnom Penh", "Bangkok", "Manille", "Cebu", "Naypyidaw", "Chittagong",
        "Dacca", "Katmandou"]

    def afficher_menu():
        print("=== Menu principal ===")
        print("1. Afficher les places de parking disponibles")
        print("2. Réserver une place de parking")
        print("3. Quitter")

    def afficher_places_de_parking(villes):
        print("Voici les places de parking disponibles :")
        for i, ville in enumerate(villes, 1):
            print(f"{i}. {ville}")

    def reserver_place_de_parking(villes):
        afficher_places_de_parking(villes)
        choix = input("Sélectionnez le numéro de la ville pour réserver une place de parking : ")
        try:
            choix = int(choix)
            if choix < 1 or choix > len(villes):
                raise ValueError
            ville_selectionnee = villes[choix - 1]
            email = input("Entrez votre adresse e-mail : ")
            password = input("Entrez votre mot de passe : ")
            immatriculation = input("Entrez le numéro de plaque d'immatriculation : ")
            heure_arrivee = input("Entrez l'heure d'arrivée : ")
            print(f"Vous avez réservé une place de parking à {ville_selectionnee}.")
            print("Détails de la réservation :")
            print(f"Adresse e-mail : {email}")
            print(f"Numéro de plaque d'immatriculation : {immatriculation}")
            print(f"Heure d'arrivée : {heure_arrivee}")
        except ValueError:
            print("Erreur : veuillez entrer un numéro valide.")
        except Exception as e:
            print(f"Erreur : {str(e)}")

    afficher_menu()
    choix_menu = input("Sélectionnez une option : ")

    while choix_menu != "3":
        if choix_menu == "1":
            afficher_places_de_parking(villes)
        elif choix_menu == "2":
            reserver_place_de_parking(villes)
        else:
            print("Option invalide.")

        afficher_menu()
        choix_menu = input("Sélectionnez une option : ")

    print("Merci d'avoir utilisé notre service de réservation de places de parking.")
