def openfilleMethod():
    import calendar

    # Fonction pour obtenir les jours fériés
    def get_holidays(year):
        # Ajoutez ici la logique pour récupérer les jours fériés pour l'année spécifiée
        # Par exemple, vous pouvez utiliser une API ou une base de données contenant les jours fériés

        # Pour l'exemple, je vais simplement retourner une liste vide
        return {}

    # Fonction pour obtenir les vacances scolaires
    def get_vacations(zone, year):
        # Ajoutez ici la logique pour récupérer les vacances scolaires pour la zone et l'année spécifiées
        # Par exemple, vous pouvez utiliser une API ou une base de données contenant les dates des vacances

        # Pour l'exemple, je vais simplement retourner une liste vide
        return []

    # Fonction pour générer le calendrier d'une année donnée
    def generate_calendar(year, zone):
        # Ajoutez ici la logique pour générer le calendrier de l'année spécifiée
        # Utilisez la bibliothèque calendar pour obtenir les jours et les mois

        holidays = get_holidays(year)
        vacations = get_vacations(zone, year)

        # Affichez le calendrier, les jours fériés et les vacances scolaires ici

    # Fonction pour afficher le menu principal
    def main_menu():
        while True:
            print("Calendriers Français")
            print("--------------------")
            print("1. Afficher les Zones")
            print("2. Quitter")

            choice = input("Veuillez sélectionner une option (1-2) : ")

            if choice == "1":
                year = int(input("Veuillez entrer une année : "))

                print("\nZones :")
                print("-------")
                print("1. Zone A : Besançon, Bordeaux, Clermont-Ferrand, Dijon, Grenoble, Limoges, Lyon, Poitiers.")
                print(
                    "2. Zone B : Aix-Marseille, Amiens, Caen, Lille, Nancy-Metz, Nantes, Nice, Orléans-Tours, Reims, Rennes, Rouen, Strasbourg.")
                print("3. Zone C : Créteil, Montpellier, Paris, Toulouse, Versailles.")

                zone_choice = input("Veuillez sélectionner une zone (1-3) : ")

                if zone_choice == "1":
                    zone = "A"
                elif zone_choice == "2":
                    zone = "B"
                elif zone_choice == "3":
                    zone = "C"
                else:
                    print("Choix invalide.")
                    continue

                generate_calendar(year, zone)

            elif choice == "2":
                print("Au revoir !")
                break

            else:
                print("Choix invalide. Veuillez sélectionner une option valide.")

    # Appel du menu principal
    main_menu()