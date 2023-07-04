import calendar

annee = 80

while annee <= 30000:
    print(f"Calendrier de l'année {annee}:")
    print(calendar.calendar(annee))

    print("\n")

    annee += 10
