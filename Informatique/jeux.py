import csv

# Ouverture du fichier CSV contenant les jeux vidéo
with open('liste_jeux_video.csv', newline='') as csvfile:
    # Lecture des données du fichier CSV
    jeux_video = csv.reader(csvfile, delimiter=',')
    # Parcours des lignes du fichier et affichage des jeux vidéo
    for row in jeux_video:
        print(row[0])  # Affichage du nom du jeu vidéo
