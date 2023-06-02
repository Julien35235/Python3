import requests


def afficher_gares():
    url = "https://api.sncf.com/v1/coverage/sncf/stop_areas"

    params = {
        "count": 100,  # Nombre maximum de gares à afficher
        "disable_geojson": "true"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        for gare in data["stop_areas"]:
            nom = gare["label"]
            horaires = obtenir_horaires(gare["id"])

            print(f"Gare : {nom}")
            print("Horaires :")
            for horaire in horaires:
                print(horaire)
            print("")
    else:
        print("Une erreur s'est produite lors de la récupération des gares.")


def obtenir_horaires(gare_id):
    url = f"https://api.sncf.com/v1/coverage/sncf/stop_areas/{gare_id}/departures"

    params = {
        "count": 3  # Nombre d'horaires à afficher par gare
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        horaires = []
        for train in data["departures"]:
            horaires.append(train["stop_date_time"]["departure_date_time"])
        return horaires
    else:
        return []


def menu_principal():
    while True:
        print("=== Menu Principal ===")
        print("1. Afficher les gares de France et leurs horaires")
        print("2. Quitter")
        choix = input("Choisissez une option : ")

        if choix == "1":
            afficher_gares()
        elif choix == "2":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez choisir à nouveau.")


menu_principal()
