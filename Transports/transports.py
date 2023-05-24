import requests
import json
from datetime import datetime


# Fonction pour récupérer les horaires des transports à Paris
def get_paris_transport_schedules():
    api_url = "https://api-ratp.pierre-grimaud.fr/v4/schedules"
    params = {
        "type": "metros",
        "code": "all",
        "station": "all"
    }
    response = requests.get(api_url, params=params)
    data = response.json()
    return data["result"]["schedules"]


# Fonction pour récupérer les horaires des transports à Rennes
def get_paris_transport_schedules():
    api_url = "https://api-ratp.pierre-grimaud.fr/v4/schedules"
    params = {
        "type": "metros",
        "code": "all",
        "station": "all"
    }
    response = requests.get(api_url, params=params)
    data = response.json()
    print(data)  # Affiche la réponse complète de l'API

    response = requests.get(api_url, params=params)
    data = response.json()
    return data["records"]


# Générer le contenu HTML avec les horaires des transports
def generate_html_content(paris_schedules, rennes_schedules):
    html_content = "<html><body>"

    # Horaires des transports à Paris
    html_content += "<h2>Horaires des transports à Paris</h2>"
    html_content += "<ul>"
    for schedule in paris_schedules:
        html_content += f"<li>Ligne {schedule['line']} - Destination {schedule['destination']} - Prochain départ à {schedule['message']}</li>"
    html_content += "</ul>"

    # Horaires des transports à Rennes
    html_content += "<h2>Horaires des transports à Rennes</h2>"
    html_content += "<ul>"
    for record in rennes_schedules:
        schedule = record["fields"]
        timestamp = int(schedule["date"].split(".")[0])
        date = datetime.fromtimestamp(timestamp)
        html_content += f"<li>Ligne {schedule['ligne']} - Destination {schedule['destination']} - Prochain départ à {date.strftime('%H:%M')}</li>"
    html_content += "</ul>"

    html_content += "</body></html>"
    return html_content


# Obtenir les horaires des transports à Paris
paris_schedules = get_paris_transport_schedules()

# Obtenir les horaires des transports à Rennes
rennes_schedules = get_rennes_transport_schedules()

# Générer le contenu HTML
html_content = generate_html_content(paris_schedules, rennes_schedules)

# Écrire le contenu HTML dans un fichier
with open("horaires_transports.html", "w") as file:
    file.write(html_content)

print("Le fichier horaires_transports.html a été généré avec succès.")
