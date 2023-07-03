import random
import pycountry

# Liste des pays à parcourir
countries = sorted(list(pycountry.countries), key=lambda x: x.name)

# Boucle while pour afficher les températures de chaque pays
for country in countries:
    country_name = country.name
    temperature = random.randint(-20, 40)  # Génère une température aléatoire entre -20°C et 40°C
    print(f"La température à {country_name} est de {temperature} degrés Celsius.")
