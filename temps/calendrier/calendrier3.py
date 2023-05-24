import calendar
import datetime

# Obtenir l'année actuelle
current_year = datetime.datetime.now().year

# Boucle sur toutes les années passées jusqu'à l'année actuelle
for year in range(1, current_year):
    print(f"Calendrier de l'année {year}:")
    print(calendar.calendar(year))
