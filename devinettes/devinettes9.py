import random

# Liste des villes
villes = ["Rennes", "Nantes", "Bordeaux", "Lege Cap Ferret", "Lunel", "Noumea", "Papeete", "Bora Bora",
          "Delhi", "Mumbai", "Chennai", "Colombo", "Kandy", "Galle", "Dallas", "Montreal", "Quebec"]

# Dictionnaire des météos
meteos = {
    "Rennes": "nuageux",
    "Nantes": "pluvieux",
    "Bordeaux": "ensoleillé",
    "Lege Cap Ferret": "venteux",
    "Lunel": "neigeux",
    "Noumea": "ensoleillé",
    "Papeete": "pluvieux",
    "Bora Bora": "ensoleillé",
    "Delhi": "ensoleillé",
    "Mumbai": "pluvieux",
    "Chennai": "nuageux",
    "Colombo": "pluvieux",
    "Kandy": "nuageux",
    "Galle": "ensoleillé",
    "Dallas": "ensoleillé",
    "Montreal": "neigeux",
    "Quebec": "pluvieux"
}

print("Devinez la météo d'une ville!")

devinette = True

while devinette:
    ville = random.choice(villes)
    meteo_attendue = meteos[ville]

    devinez = input("Quelle est la météo attendue pour {} ? ".format(ville))

    if devinez.lower() == meteo_attendue.lower():
        print("Félicitations! Vous avez deviné correctement!")
        devinette = False
    else:
        print("Ce n'est pas la bonne réponse. Réessayez!")

print("Fin du jeu.")
