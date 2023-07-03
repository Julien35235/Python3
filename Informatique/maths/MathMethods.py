def openfilleMathMethods():
    import math

    def afficher_message_genre(nom, genre):
        if genre == "M":
            print("Cher Monsieur", nom)
        elif genre == "F":
            print("Chère Mademoiselle", nom)
        else:
            print("Genre non valide.")

    def determiner_type_triangle(a, b, c):
        if a + b > c and a + c > b and b + c > a:
            print("Un triangle peut être construit.")
            if a == b and b == c:
                print("Le triangle est équilatéral.")
            elif a == b or b == c or a == c:
                if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
                    print("Le triangle est isocèle et rectangle.")
                else:
                    print("Le triangle est isocèle.")
            elif a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
                print("Le triangle est rectangle.")
            else:
                print("Le triangle est quelconque.")
        else:
            print("Un triangle ne peut pas être construit.")

    def calculer_racine_carree(nombre):
        if nombre >= 0:
            racine_carree = math.sqrt(nombre)
            print("La racine carrée de", nombre, "est", racine_carree)
        else:
            print("La racine carrée de ce nombre ne peut être calculée.")

    def afficher_noms_caracteres(noms):
        for nom in noms:
            nb_caracteres = len(nom)
            print(nom, "-", nb_caracteres, "caractères.")

    def calculer_force_gravitation():
        masse1 = 10000  # kg
        masse2 = 10000  # kg
        distance = 0.05  # mètre

        # Augmentation de la distance jusqu'à 100 mètres
        while distance <= 100:
            force_gravitation = (6.67430 * 10 ** -11) * (masse1 * masse2) / distance ** 2
            print("Distance :", distance, "m - Force de gravitation :", force_gravitation, "N")
            distance *= 2  # Progression géométrique de raison 2

    # Menu principal
    while True:
        print("Menu principal:")
        print("1. Afficher le message de genre")
        print("2. Déterminer le type de triangle")
        print("3. Calculer la racine carrée d'un nombre")
        print("4. Afficher les noms avec le nombre de caractères correspondant")
        print("5. Calculer la force de gravitation")
        print("0. Quitter")

        choix = input("Entrez votre choix : ")

        if choix == "0":
            break
        elif choix == "1":
            nom = input("Entrez votre nom : ")
            genre = input("Entrez votre genre (M ou F) : ")
            afficher_message_genre(nom, genre)
        elif choix == "2":
            a = float(input("Entrez la longueur a : "))
            b = float(input("Entrez la longueur b : "))
            c = float(input("Entrez la longueur c : "))
            determiner_type_triangle(a, b, c)
        elif choix == "3":
            nombre = float(input("Entrez un nombre : "))
            calculer_racine_carree(nombre)
        elif choix == "4":
            noms = ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'Alexandre-Benoît', 'Louise']
            afficher_noms_caracteres(noms)
        elif choix == "5":
            calculer_force_gravitation()
        else:
            print("Choix non valide.")

    print("Au revoir!")
