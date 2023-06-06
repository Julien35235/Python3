def openfilleMethod():
    import datetime

    # Définition des fêtes nationales
    HOLIDAYS = {
        (1, 1): "Jour de l'an",
        (1, 5): "Fête du travail",
        (8, 5): "Victoire 1945",
        (14, 7): "Fête nationale",
        (15, 8): "Assomption",
        (1, 11): "Toussaint",
        (11, 11): "Armistice 1918",
        (25, 12): "Noël"
    }

    # Définition des vacances scolaires par zone
    VACATIONS = {
        "A": [
            (datetime.date(2023, 2, 11), datetime.date(2023, 2, 26)),
            (datetime.date(2023, 4, 8), datetime.date(2023, 4, 23)),
            (datetime.date(2023, 7, 8), datetime.date(2023, 9, 4))
        ],
        "B": [
            (datetime.date(2023, 2, 25), datetime.date(2023, 3, 12)),
            (datetime.date(2023, 4, 22), datetime.date(2023, 5, 7)),
            (datetime.date(2023, 7, 1), datetime.date(2023, 9, 4))
        ],
        "C": [
            (datetime.date(2023, 2, 18), datetime.date(2023, 3, 5)),
            (datetime.date(2023, 4, 15), datetime.date(2023, 4, 30)),
            (datetime.date(2023, 6, 24), datetime.date(2023, 9, 4))
        ]
    }

    # Fonction pour vérifier si une date est un jour férié ou une vacance
    def is_holiday(date):
        # Vérifier les fêtes nationales
        if (date.month, date.day) in HOLIDAYS:
            return True
        # Vérifier les vacances scolaires
        for vacations in VACATIONS.values():
            for vacation in vacations:
                if date >= vacation[0] and date <= vacation[1]:
                    return True
        # Si la date n'est ni une fête ni une vacance, retourner False
        return False

    # Début de la boucle while
    year = 1560
    html = "<html>\n<head>\n<title>Calendrier</title>\n</head>\n<body>\n"
    while year <= 2090:
        html += f"<h2>Calendrier pour l'année {year}</h2>\n<table>\n"
        # Boucle sur les mois
        for month in range(1, 13):
            # Récupérer le premier jour du mois
            first_day = datetime.date(year, month, 1)
            # Calculer le nombre de jours dans le mois
            if month == 12:
                num_days = 31
            elif month == 2:
                if year % 4 == 0:

                    num_days = 29 if year % 100 == 0 and year % 400 != 0 else 28
                elif month in [4, 6, 9, 11]:
                    num_days = 30
                else:
                    num_days = 31
                    # Créer la première ligne du mois dans le tableau
                html += "<tr><th>" + first_day.strftime("%B") + "</th>"
                # Ajouter des cellules vides pour aligner le jour de la semaine
                for i in range(first_day.weekday()):
                    html += "<td></td>"
                # Boucle sur les jours du mois
                for day in range(1, num_days + 1):
                    # Vérifier si la date est une fête ou une vacance
                    if is_holiday(datetime.date(year, month, day)):
                        html += f"<td><b>{day}</b></td>"
                    else:
                        html += f"<td>{day}</td>"
                    # Ajouter une nouvelle ligne après chaque samedi
                    if datetime.date(year, month, day).weekday() == 5:
                        html += "</tr>\n<tr>"
                # Ajouter des cellules vides pour terminer le tableau
                for i in range(6 - datetime.date(year, month, num_days).weekday()):
                    html += "<td></td>"
                html += "</tr>\n"
            html += "</table>\n"
            year += 1

        html += "</body>\n</html>"

        # Enregistrer le résultat dans un fichier HTML
        with open("calendrier.html", "w") as f:
            f.write(html)
