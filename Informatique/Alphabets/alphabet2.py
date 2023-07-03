import keyboard

def afficher_alphabet(alphabet):
    print("L'alphabet sélectionné est :")
    print("".join(alphabet))


def verifier_touche_pressee_azerty():
    touche = input("Entrez une touche : ")
    if keyboard.is_pressed(touche):
        print("La touche", touche, "est pressée.")
    else:
        print("La touche", touche, "n'est pas pressée.")


def verifier_touche_pressee_qwerty():
    touche = input("Entrez une touche : ")
    if keyboard.is_pressed(touche):
        print("La touche", touche, "est pressée.")
    else:
        print("La touche", touche, "n'est pas pressée.")


def obtenir_touches_pressees_azerty():
    touches = keyboard.get_hotkey_name()
    print("Liste des touches pressées (AZERTY) :", touches)


def obtenir_touches_pressees_qwerty():
    touches = keyboard.get_hotkey_name()
    print("Liste des touches pressées (QWERTY) :", touches)


def afficher_chiffres():
    chiffre = 1
    while True:
        print(chiffre)
        chiffre += 1


def menu_principal():
    print("Bienvenue dans le menu principal !")
    print("Veuillez choisir une option :")
    print("1. Afficher l'alphabet standard")
    print("2. Afficher l'alphabet avec les symboles spécifiés")
    print("3. Afficher l'alphabet AZERTY")
    print("4. Afficher l'alphabet QWERTY")
    print("5. Vérifier si une touche est pressée (AZERTY)")
    print("6. Vérifier si une touche est pressée (QWERTY)")
    print("7. Obtenir la liste des touches pressées (AZERTY)")
    print("8. Obtenir la liste des touches pressées (QWERTY)")
    print("9. Afficher les chiffres jusqu'à l'infini")
    print("10. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        alphabet_standard = list("abcdefghijklmnopqrstuvwxyz")
        afficher_alphabet(alphabet_standard)
    elif choix == "2":
        alphabet_symboles = list("abcdefghijklmnopqrstuvwxyz@&é\"'(§è!çà)-=:;,%`*¨<>")
        afficher_alphabet(alphabet_symboles)
    elif choix == "3":
        alphabet_azerty = list("azertyuiopqsdfghjklmwxcvbn")
        afficher_alphabet(alphabet_azerty)
    elif choix == "4":
        alphabet_qwerty = list("qwertyuiopasdfghjklzxcvbnm")
        afficher_alphabet(alphabet_qwerty)
    elif choix == "5":
        verifier_touche_pressee_azerty()
    elif choix == "6":
        verifier_touche_pressee_qwerty()
    elif choix == "7":
        obtenir_touches_pressees_azerty()
    elif choix == "8":
        obtenir_touches_pressees_qwerty()
    elif choix == "9":
        afficher_chiffres()
    elif choix == "10":
        print("Au revoir !")
        return
    else:
        print("Choix invalide. Veuillez réessayer.")

    menu_principal()


# Appel du menu principal
menu_principal()