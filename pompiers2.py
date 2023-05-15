import requests
from bs4 import BeautifulSoup
import csv

# URL de la page Web à extraire
url = "https://www.concours-pompier.com/devenir-pompier-professionnel-161/vehicules-pompiers-233"

# Effectuer une requête HTTP pour récupérer le contenu de la page
response = requests.get(url)
content = response.content

# Créer un objet BeautifulSoup pour analyser le contenu HTML de la page
soup = BeautifulSoup(content, 'html.parser')

# Trouver la table contenant les informations sur les véhicules des pompiers
table = soup.find('table')

# Créer une liste vide pour stocker les données des véhicules
vehicles = []

# Parcourir chaque ligne de la table, en ignorant la première ligne d'en-tête
for row in table.find_all('tr')[1:]:
    # Extraire les informations sur le véhicule de chaque colonne de la ligne
    cols = row.find_all('td')
    vehicle_type = cols[0].text.strip()
    model = cols[1].text.strip()
    engine_power = cols[2].text.strip()
    max_speed = cols[3].text.strip()

    # Ajouter les informations sur le véhicule à la liste des véhicules
    vehicles.append([vehicle_type, model, engine_power, max_speed])

# Écrire les données des véhicules dans un fichier CSV
with open('vehicles.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Type', 'Modèle', 'Puissance moteur', 'Vitesse maximale'])
    writer.writerows(vehicles)

# Utiliser la fonction m.save() pour enregistrer le fichier CSV dans le système de fichiers de la machine virtuelle
m.save('vehicles.html')
