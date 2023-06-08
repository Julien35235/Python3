def openfilleJeuxMethod():
    def afficher_menu():
        print("Bienvenue dans Paris Driver Simulator !")
        print("1. Afficher les lignes de métro")
        print("2. Afficher les lignes de RER")
        print("3. Afficher les lignes de tram")
        print("4. Afficher toutes les stations de métro, RER et tram")
        print("5. Afficher les gares de France et les lignes des TGV")
        print("6. Quitter")

    def afficher_lignes_metro():
        print("Lignes de métro:")
        lignes_metro = {
            "M1": ["La Défense", "Château de Vincennes"],
            "M2": ["Porte Dauphine", "Nation"],
            "M3": ["Pont de Levallois", "Gallieni"],
            # Ajoutez les autres lignes de métro avec leurs stations
        }
        for ligne, stations in lignes_metro.items():
            print(f"{ligne}: {stations[0]} - {stations[1]}")

    def afficher_lignes_rer():
        print("Lignes de RER:")
        lignes_rer = {
            "RER A": ["Saint-Germain-en-Laye", "Boissy-Saint-Léger"],
            "RER B": ["Robinson", "Aéroport Charles de Gaulle"],
            "RER C": ["Pontoise", "Massy-Palaiseau"],
            # Ajoutez les autres lignes de RER avec leurs stations
        }
        for ligne, stations in lignes_rer.items():
            print(f"{ligne}: {stations[0]} - {stations[1]}")

    def afficher_lignes_tram():
        print("Lignes de tram:")
        lignes_tram = {
            "T1": ["Asnières-Gennevilliers", "Noisy-le-Sec"],
            "T2": ["Pont de Bezons", "Porte de Versailles"],
            "T3": ["Pont du Garigliano", "Porte d'Ivry"],
            # Ajoutez les autres lignes de tram avec leurs stations
        }
        for ligne, stations in lignes_tram.items():
            print(f"{ligne}: {stations[0]} - {stations[1]}")

    def afficher_stations_metro_rer_tram():
        print("Stations de métro, RER et tram:")
        stations_metro = {
            "M1": ["La Défense", "Château de Vincennes"],
            "M2": ["Porte Dauphine", "Nation"],
            "M3": ["Pont de Levallois", "Gallieni"],
            # Ajoutez les autres lignes de métro avec leurs stations
        }
        stations_rer = {
            "RER A": ["Saint-Germain-en-Laye", "Boissy-Saint-Léger"],
            "RER B": ["Robinson", "Aéroport Charles de Gaulle"],
            "RER C": ["Pontoise", "Massy-Palaiseau"],
            # Ajoutez les autres lignes de RER avec leurs stations
        }
        stations_tram = {
            "T1": ["Asnières-Gennevilliers", "Noisy-le-Sec"],
            "T2": ["Pont de Bezons", "Porte de Versailles"],
            "T3": ["Pont du Garigliano", "Porte d'Ivry"],
            # Ajoutez les autres lignes de tram avec leurs stations
        }
        for ligne, stations in stations_metro.items():
            print(f"{ligne}: {', '.join(stations)}")
        for ligne, stations in stations_rer.items():
            print(f"{ligne}: {', '.join(stations)}")
        for ligne, stations in stations_tram.items():
            print(f"{ligne}: {', '.join(stations)}")

    def afficher_gares_tgv():
        print("Gares de France et lignes des TGV:")
        gares_tgv = {
            "Paris": ["Gare de Lyon", "Gare du Nord"],
            "Lyon": ["Gare de Lyon Part-Dieu", "Gare de Lyon Perrache"],
            # Ajoutez les autres gares de France avec leurs lignes de TGV
        }
        for ville, gares in gares_tgv.items():
            print(f"{ville}: {', '.join(gares)}")

    while True:
        afficher_menu()

        choix = input("Choisissez une option : ")
        if choix == "1":
            afficher_lignes_metro()
        elif choix == "2":
            afficher_lignes_rer()
        elif choix == "3":
            afficher_lignes_tram()
        elif choix == "4":
            afficher_stations_metro_rer_tram()
        elif choix == "5":
            afficher_gares_tgv()
        elif choix == "6":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")
