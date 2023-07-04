def addition(a, b):
    return a + b


def soustraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur : division par zéro"


def menu_principal():
    while True:
        print("Menu Principal des :")
        print("1. Addition")
        print("2. Soustraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quitter")

        choix = input("Choisissez une option (1-5): ")

        if choix == "1":
            a = float(input("Entrez le premier nombre: "))
            b = float(input("Entrez le deuxième nombre: "))
            print("Résultat: ", addition(a, b))
        elif choix == "2":
            a = float(input("Entrez le premier nombre: "))
            b = float(input("Entrez le deuxième nombre: "))
            print("Résultat: ", soustraction(a, b))
        elif choix == "3":
            a = float(input("Entrez le premier nombre: "))
            b = float(input("Entrez le deuxième nombre: "))
            print("Résultat: ", multiplication(a, b))
        elif choix == "4":
            a = float(input("Entrez le premier nombre: "))
            b = float(input("Entrez le deuxième nombre: "))
            print("Résultat: ", division(a, b))
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")


menu_principal()