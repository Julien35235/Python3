import requests
from getpass import getpass

# Informations de connexion à Domoticz
domoticz_ip = '192.168.1.100'  # Remplacez par l'adresse IP de votre serveur Domoticz
domoticz_port = '8080'  # Remplacez par le port utilisé par votre serveur Domoticz
domoticz_username = 'admin'  # Remplacez par votre nom d'utilisateur Domoticz
domoticz_password = getpass('Mot de passe Domoticz: ')


# Fonction pour allumer une lumière spécifique
def allumer_lumiere(idx):
    url = f"http://{domoticz_ip}:{domoticz_port}/json.htm?type=command&param=switchlight&idx={idx}&switchcmd=On"
    response = requests.get(url, auth=(domoticz_username, domoticz_password))

    if response.status_code == 200:
        print("Lumière allumée avec succès !")
    else:
        print("Erreur lors de l'allumage de la lumière.")

# Exemple d'utilisation : allumer une lumière avec l'indice IDX 123
allumer_lumiere(123)