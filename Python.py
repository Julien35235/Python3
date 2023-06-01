# Fonction pour afficher le menu
def afficher_menu():
    print("=== MENU PRINCIPAL ===")
    print("1. Boucles")
    print("2. Calculs personnalisés")
    print("3. Fonctions")
    print("4. Variables")
    print("5. Conditions booléennes")
    print("6. Quitter")

# Boucle principale du menu
choix = 0
while choix != 6:
    afficher_menu()
    choix = int(input("Entrez votre choix : "))

    if choix == 1:
        # Boucles
        print("Exemple de boucle while :")
        counter = 0
        while counter < 5:
            print("Tour :", counter)
            counter += 1
        print()

    elif choix == 2:
        # Calculs personnalisés
        print("Calculs personnalisés :")
        a = int(input("Entrez le premier nombre : "))
        b = int(input("Entrez le deuxième nombre : "))
        # Effectuez ici vos calculs personnalisés en utilisant les variables a et b
        print("Résultat du calcul :", a + b)  # Exemple d'addition
        print()

    elif choix == 3:
        # Fonctions
        def carre(nombre):
            return nombre ** 2

        def cube(nombre):
            return nombre ** 3

        print("Fonctions :")
        print("Le carré de 3 est", carre(3))
        print("Le cube de 4 est", cube(4))
        print()

    elif choix == 4:
        # Variables
        x = 7
        y = 12
        est_superieur = x > y
        est_egale = x == y

        print("Variables :")
        print("x est supérieur à y :", est_superieur)
        print("x est égal à y :", est_egale)
        print()

    elif choix == 5:
        # Conditions booléennes
        z = int(input("Entrez un nombre : "))
        if z > 0:
            print("z est positif")
        elif z < 0:
            print("z est négatif")
        else:
            print("z est nul")
        print()

    elif choix == 6:
        # Quitter
        print("Au revoir !")

    else:
        print("Choix invalide. Veuillez réessayer.")
        print()