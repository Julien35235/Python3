# Importation de la bibliothèque random pour choisir aléatoirement un pays et son continent
import random

# Définition des listes de pays et de continents
pays = ['France', 'Allemagne', 'Espagne', 'Italie', 'Royaume-Uni', 'États-Unis', 'Canada', 'Mexique', 'Brésil', 'Chine',
        'Inde', 'Japon', 'Australie']
continents = ['Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Amérique du Nord', 'Amérique du Nord',
              'Amérique du Nord', 'Amérique du Sud', 'Asie', 'Asie', 'Asie', 'Océanie']

# Boucle infinie pour afficher les pays et leur continent
while True:
    # Sélection aléatoire d'un pays et de son continent correspondant
    index = random.randint(0, len(pays) - 1)
    pays_choisi = pays[index]
    continent_choisi = continents[index]

    # Affichage du pays et de son continent
    print(pays_choisi + ' se trouve en ' + continent_choisi)
