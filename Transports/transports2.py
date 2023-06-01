import matplotlib.pyplot as plt
import json

# Charger les données du réseau
with open('stations_metro.json') as f:
    stations_metro = json.load(f)

with open('stations_rer.json') as f:
    stations_rer = json.load(f)

with open('stations_tram.json') as f:
    stations_tram = json.load(f)

with open('gares_france.json') as f:
    gares_france = json.load(f)

with open('traces_lignes.json') as f:
    traces_lignes = json.load(f)

# Fonction pour afficher le menu principal
def afficher_menu():
    print("Menu principal:")
    print("1. Métro")
    print("2. RER")
    print("3. Tramway")
    print("4. TGV")
    print("5. Gares de France")
    print("6. Quitter")

# Fonction pour afficher toutes les stations de métro jusqu'aux terminus
def afficher_stations_metro():
    print("Stations de métro jusqu'aux terminus:")
    for ligne, stations in stations_metro.items():
        print(f"Ligne {ligne}:")
        for station in stations:
            print(station)
        print()

# Fonction pour afficher toutes les stations RER jusqu'aux terminus
def afficher_stations_rer():
    print("Stations RER jusqu'aux terminus:")
    for ligne, stations in stations_rer.items():
        print(f"Ligne {ligne}:")
        for station in stations:
            print(station)
        print()

# Fonction pour afficher toutes les stations de tramway jusqu'aux terminus
def afficher_stations_tram():
    print("Stations de tramway jusqu'aux terminus:")
    for ligne, stations in stations_tram.items():
        print(f"Ligne {ligne}:")
        for station in stations:
            print(station)
        print()

# Fonction pour afficher toutes les gares de France
def afficher_gares_france():
    print("Gares de France:")
    for gare in gares_france:
        print(gare)
    print()

# Fonction pour afficher les tracés des lignes
def afficher_traces_lignes():
    print("Tracés des lignes:")
    for ligne, trace in traces_lignes.items():
        plt.plot(trace['x'], trace['y'], label=f"Ligne {ligne}")
    plt.legend()
    plt.axis('equal')
    plt.show()

# Boucle principale
while True:
    afficher_menu()
    choix = input("Choisissez une option (1-6): ")

    if choix == '1':
        afficher_stations_metro()
    elif choix == '2':
        afficher_stations_rer()
    elif choix == '3':
        afficher_stations_tram()
    elif choix == '4':
        print("Les informations sur les lignes TGV sont actuellement indisponibles.")
    elif choix == '5':
        afficher_gares_france()
    elif choix == '6':
        print("Au revoir !")
        break
    else:
        print("Option invalide. Veuillez choisir une option valide.")

    if choix == '1' or choix == '2' or choix == '3' or choix == '4':
        afficher_traces_lignes()
