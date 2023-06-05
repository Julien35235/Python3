import random
import pytz
from datetime import datetime
import pycountry

# Liste des pays représentatifs du monde entier
world_countries = [
    'France', 'United States', 'Japan', 'Egypt',
    # Ajoutez d'autres pays représentatifs ici
]

# Fonction pour obtenir l'heure actuelle dans un fuseau horaire donné
def get_current_time(timezone):
    tz = pytz.timezone(timezone)
    current_time = datetime.now(tz)
    return current_time.strftime('%H:%M')

# Fonction pour afficher les heures des pays
def afficher_heures():
    print("--- Heures du monde entier ---")
    for country_name in world_countries:
        country_code = pycountry.countries.get(name=country_name).alpha_2
        timezone = pytz.country_timezones.get(country_code)[0]
        current_time = get_current_time(timezone)
        print(f"L'heure actuelle dans {country_name} est {current_time}.")
    print()

# Fonction pour afficher les températures des pays
def afficher_températures():
    print("--- Températures du monde entier ---")
    for country_name in world_countries:
        temperature = random.randint(-20, 40)  # Génère une température aléatoire entre -20°C et 40°C
        print(f"La température dans {country_name} est de {temperature} degrés Celsius.")
    print()

# Fonction principale pour afficher le menu
def afficher_menu():
    while True:
        print("=== MENU ===")
        print("1. Afficher les heures du monde entier")
        print("2. Afficher les températures du monde entier")
        print("0. Quitter")
        choix = input("Entrez votre choix : ")
        print()

        if choix == "1":
            afficher_heures()
        elif choix == "2":
            afficher_températures()
        elif choix == "0":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
        print()

# Appel de la fonction principale
afficher_menu()
