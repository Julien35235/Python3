def afficher_menu_principal():
    print("Menu principal")
    print("1. Départs")
    print("2. Arrivées")
    print("3. Annonces en gare")
    print("4. Quitter")


# Exemple de données de départs et arrivées en gare pour différentes villes et services
departs = {
    "TGV": [
        {"ville": "Bordeaux", "heure": "08h00", "destination": "Marseille", "voie": "Voie 1"},
        {"ville": "Lyon", "heure": "09h30", "destination": "Paris", "voie": "Voie 2"}
    ],
    "Eurostar": [
        {"ville": "Lille", "heure": "10h15", "destination": "Londres", "voie": "Voie 3"},
        {"ville": "Londres", "heure": "11h45", "destination": "Paris", "voie": "Voie 4"}
    ],
    "Eurotunnel": [
        {"ville": "Calais", "heure": "12h30", "destination": "Folkestone", "voie": "Voie A"},
        {"ville": "Folkestone", "heure": "13h15", "destination": "Calais", "voie": "Voie B"}
    ],
    "TER": [
        {"ville": "Rennes", "heure": "12h00", "destination": "Saint-Malo", "voie": "Voie 5"},
        {"ville": "Nantes", "heure": "13h30", "destination": "Angers", "voie": "Voie 6"}
    ],
    "Intercités": [
        {"ville": "Niort", "heure": "10h00", "destination": "Bordeaux", "voie": "Voie 7"},
        {"ville": "Lyon", "heure": "11h30", "destination": "Marseille", "voie": "Voie 8"}
    ],
    "Transilien": [
        {"ville": "Paris", "heure": "07h45", "destination": "Versailles", "voie": "Voie 9"},
        {"ville": "Saint-Denis", "heure": "08h30", "destination": "Chantilly", "voie": "Voie 10"}
    ],
    "RER": [
        {"ville": "Paris", "heure": "08h15", "destination": "Marne-la-Vallée", "voie": "Voie A"},
        {"ville": "Cergy", "heure": "09h00", "destination": "Gare du Nord", "voie": "Voie B"}
    ],
    "Ouigo": [
        {"ville": "Paris", "heure": "22h00", "destination": "Lyon", "voie": "Voie 11"},
        {"ville": "Lyon", "heure": "23h15", "destination": "Paris", "voie": "Voie 12"}
    ],
    "InOui": [
        {"ville": "Paris", "heure": "00h00", "destination": "Marseille", "voie": "Voie 13"},
        {"ville": "Marseille", "heure": "01h15", "destination": "Paris", "voie": "Voie 14"}
    ],
    "Auto-Train": [
        {"ville": "Paris", "heure": "02h00", "destination": "Nice", "voie": "Voie 15"},
        {"ville": "Nice", "heure": "03h15", "destination": "Paris", "voie": "Voie 16"}
    ],
    "Night Jet": [
        {"ville": "Paris", "heure": "04h00", "destination": "Munich", "voie": "Voie 17"},
        {"ville": "Munich", "heure": "05h15", "destination": "Paris", "voie": "Voie 18"}
    ]
}

arrivees = {
    "TGV": [
        {"ville": "Marseille", "heure": "07h45", "provenance": "Paris", "voie": "Voie 1"},
        {"ville": "Paris", "heure": "08h30", "provenance": "Lyon", "voie": "Voie 2"}
    ],
    "Eurostar": [
        {"ville": "Londres", "heure": "10h00", "provenance": "Lille", "voie": "Voie 3"},
        {"ville": "Paris", "heure": "11h30", "provenance": "Londres", "voie": "Voie 4"}
    ],
    "Eurotunnel": [
        {"ville": "Folkestone", "heure": "12h15", "provenance": "Calais", "voie": "Voie B"},
        {"ville": "Calais", "heure": "13h00", "provenance": "Folkestone", "voie": "Voie A"}
    ],
    "TER": [
        {"ville": "Saint-Malo", "heure": "12h30", "provenance": "Rennes", "voie": "Voie 3"},
        {"ville": "Angers", "heure": "13h15", "provenance": "Nantes", "voie": "Voie 5"}
    ],
    "Intercités": [
        {"ville": "Bordeaux", "heure": "10h30", "provenance": "Paris", "voie": "Voie 7"},
        {"ville": "Marseille", "heure": "11h45", "provenance": "Lyon", "voie": "Voie 9"}
    ],
    "Transilien": [
        {"ville": "Versailles", "heure": "07h30", "provenance": "Paris", "voie": "Voie 1"},
        {"ville": "Chantilly", "heure": "08h15", "provenance": "Saint-Denis", "voie": "Voie 3"}
    ],
    "RER": [
        {"ville": "Marne-la-Vallée", "heure": "08h00", "provenance": "Paris", "voie": "Voie A"},
        {"ville": "Gare du Nord", "heure": "08h45", "provenance": "Cergy", "voie": "Voie B"}
    ],
    "Ouigo": [
        {"ville": "Lyon", "heure": "20h00", "provenance": "Paris", "voie": "Voie 11"},
        {"ville": "Paris", "heure": "21h15", "provenance": "Lyon", "voie": "Voie 12"}
    ],
    "InOui": [
        {"ville": "Marseille", "heure": "23h30", "provenance": "Paris", "voie": "Voie 14"},
        {"ville": "Paris", "heure": "00h45", "provenance": "Marseille", "voie": "Voie 15"}
    ],
    "Auto-Train": [
        {"ville": "Nice", "heure": "01h00", "provenance": "Paris", "voie": "Voie 16"},
        {"ville": "Paris", "heure": "02h15", "provenance": "Nice", "voie": "Voie 18"}
    ],
    "Night Jet": [
        {"ville": "Munich", "heure": "03h00", "provenance": "Paris", "voie": "Voie 19"},
        {"ville": "Paris", "heure": "04h15", "provenance": "Munich", "voie": "Voie 20"}
    ]
}

while True:
    afficher_menu_principal()
    choix = input("Choisissez une option : ")

    if choix == "1":
        print("Départs")
        for service, trains in departs.items():
            print(f"- {service}:")
            for train in trains:
                print(f"  - {train['ville']} - {train['heure']} - {train['destination']} - {train['voie']}")

    elif choix == "2":
        print("Arrivées")
        for service, trains in arrivees.items():
            print(f"- {service}:")
            for train in trains:
                print(f"  - {train['ville']} - {train['heure']} - {train['provenance']} - {train['voie']}")

    elif choix == "3":
        print("Annonces en gare")
        # Ajoutez ici le code pour les annonces en gare

    elif choix == "4":
        print("Au revoir !")
        break

    else:
        print("Option invalide. Veuillez choisir une option valide.")