#Un programme qui affiche tous les pays du monde avec leurs continents
# Importer la bibliothèque requests pour effectuer une demande HTTP
import requests

# Initialisation de l'URL de l'API
url = "https://restcountries.com/v3.1/all"

# Effectuer une demande HTTP pour récupérer les données de tous les pays
response = requests.get(url)

# Vérifier si la demande HTTP a réussi
if response.status_code == 200:
    # Convertir la réponse JSON en un dictionnaire Python
    data = response.json()

    # Initialiser les variables pour la boucle
    index = 0
    nb_pays = len(data)

    # Boucle pour afficher tous les pays
    while index < nb_pays:
        pays_actuel = data[index]['name']['common']
        print(pays_actuel)
        index += 1
else:
    # Afficher un message d'erreur si la demande HTTP a échoué
    print("Erreur lors de la récupération des données.")

