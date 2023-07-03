# Définition des listes de pays et de continents
pays = ['France', 'Allemagne', 'Espagne', 'Italie', 'Royaume-Uni', 'États-Unis', 'Canada', 'Mexique', 'Brésil', 'Chine', 'Inde', 'Japon', 'Australie']
continents = ['Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Amérique du Nord', 'Amérique du Nord', 'Amérique du Nord', 'Amérique du Sud', 'Asie', 'Asie', 'Asie', 'Océanie']

# Initialisation de l'indice de la boucle
i = 0

# Boucle while pour afficher les pays et leur continent
while i < len(pays):
    print(pays[i] + ' se trouve en ' + continents[i])
    i += 1
