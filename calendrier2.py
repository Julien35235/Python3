import calendar
import datetime

#Mettre la langue française
locale = 'fr_FR'

# Obtenir l'année actuelle
current_year = datetime.datetime.now().year

# Afficher des calendriers pour les 50 prochaines années
for year in range(current_year, current_year + 50):
    cal = calendar.calendar(year)
    print("Calendrier pour l'année {year}:")
    print(cal)
    print("\n")
