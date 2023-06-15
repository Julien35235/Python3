def openfilleMethod():
    import datetime

    # Liste des jours fériés
    jours_feries = {
        datetime.date(datetime.date.today().year, 1, 1): "Jour de l'an",
        datetime.date(datetime.date.today().year, 5, 1): "Fête du Travail",
        datetime.date(datetime.date.today().year, 7, 14): "Fête nationale",
        datetime.date(datetime.date.today().year, 12, 25): "Noël"
    }

    # Liste des fêtes nationales
    fetes_nationales = {
        datetime.date(datetime.date.today().year, 2, 14): "Saint-Valentin",
        datetime.date(datetime.date.today().year, 3, 17): "Saint-Patrick",
        datetime.date(datetime.date.today().year, 7, 4): "Fête de l'Indépendance",
        datetime.date(datetime.date.today().year, 10, 31): "Halloween"
    }

    # Fonction pour afficher le calendrier avec les jours fériés et les fêtes nationales
    def afficher_calendrier(year):
        print("                 ", year)
        print(" Janvier ")
        print("Lun Mar Mer Jeu Ven Sam Dim")
        first_day = datetime.date(year, 1, 1)
        last_day = datetime.date(year, 2, 1) - datetime.timedelta(days=1)
        start_day = first_day.weekday()
        print(" " * (3 * start_day), end="")
        for day in range(1, last_day.day + 1):
            date = datetime.date(year, 1, day)
            if date.weekday() == 0 and day != 1:
                print()
            if date in jours_feries:
                print("[" + str(day).rjust(2) + "]", end=" ")
            elif date in fetes_nationales:
                print("(" + str(day).rjust(2) + ")", end=" ")
            else:
                print(str(day).rjust(2), end=" ")
        print("\n")

        for month in range(2, 13):
            month_name = datetime.date(year, month, 1).strftime("%B")
            print(" " * 10, month_name)
            print("Lun Mar Mer Jeu Ven Sam Dim")
            first_day = datetime.date(year, month, 1)
            last_day = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
            start_day = first_day.weekday()
            print(" " * (3 * start_day), end="")
            for day in range(1, last_day.day + 1):
                date = datetime.date(year, month, day)
                if date.weekday() == 0 and day != 1:
                    print()
                if date in jours_feries:
                    print("[" + str(day).rjust(2) + "]", end=" ")
                elif date in fetes_nationales:
                    print("(" + str(day).rjust(2) + ")", end=" ")
                else:
                    print(str(day).rjust(2), end=" ")
            print("\n")

    # Affichage du calendrier pour chaque année
    for year in range(1300, 3001):
        afficher_calendrier(year)
        print("-" * 50)
