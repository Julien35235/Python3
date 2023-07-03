import datetime
import pytz
import time

# Définir les fuseaux horaires de chaque ville
pays = {"New York": "America/New_York",
        "Londres": "Europe/London",
        "Paris": "Europe/Paris",
        "Tokyo": "Asia/Tokyo"}

while True:
    for ville, fuseau_horaire in pays.items():
        tz = pytz.timezone(fuseau_horaire)
        heure_locale = datetime.datetime.now(tz)
        print(ville, ":", heure_locale.strftime("%H:%M:%S"))
    time.sleep(1)
