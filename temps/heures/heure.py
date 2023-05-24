import pytz
from datetime import datetime

# obtenir la date et l'heure actuelles
heure_actuelle = datetime.now()

# parcourir tous les fuseaux horaires de la base de données pytz
for nom_fuseau in pytz.all_timezones:
    tz = pytz.timezone(nom_fuseau)
    heure_locale = heure_actuelle.astimezone(tz)
    print(f"L'heure actuelle dans le fuseau horaire {nom_fuseau} est {heure_locale.strftime('%H:%M')}")
