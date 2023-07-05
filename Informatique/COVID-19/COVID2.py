def afficher_menu():
    print("=== Menu ===")
    print("1. Vérifier la température corporelle")
    print("2. Quitter")
    print()


def verifier_temperature():
    seuil_fievre = float(input("Entrez le seuil de fièvre en degrés Celsius : "))
    temperature = float(input("Entrez la température corporelle en degrés Celsius : "))
    if temperature >= seuil_fievre:
        print("Vous avez de la fièvre.")
    else:
        print("Votre température est normale.")


# Boucle principale du programme
while True:
    afficher_menu()
    choix = input("Entrez votre choix (1-2) : ")

    if choix == "1":
        verifier_temperature()
    elif choix == "2":
        print("Merci d'avoir utilisé notre programme. Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")

    print()