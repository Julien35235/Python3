def openfileTVMethod():
    # Fonction pour afficher les options du menu
    def afficher_menu():
        print("Menu :")
        print("1. Allumer/Éteindre la télévision")
        print("2. Changer de chaîne")
        print("3. Augmenter le volume")
        print("4. Baisser le volume")
        print("5. Quitter le programme")

    # Paramètres personnalisables
    allume = False
    chaine = input("Entrez le numéro de la chaîne actuelle : ")
    volume = int(input("Entrez le niveau de volume actuel (entre 0 et 10) : "))

    # Boucle principale à vrai
    while True:
        afficher_menu()
        choix = input("Choisissez une option : ")

        if choix == "1":
            allume = not allume
            if allume:
                print("La télévision est allumée.")
            else:
                print("La télévision est éteinte.")

        elif choix == "2":
            if allume:
                chaine = input("Entrez le numéro de la nouvelle chaîne : ")
                if chaine.isdigit() and int(chaine) <= 131:
                    print("La chaîne a été changée en", chaine)
                else:
                    print("Numéro de chaîne invalide.")
            else:
                print("Veuillez allumer la télévision pour changer de chaîne.")

        elif choix == "3":
            if allume and volume < 10:
                volume += 1
                print("Le volume a été augmenté. Volume actuel :", volume)
            else:
                print("La télévision est éteinte ou le volume est déjà au maximum.")

        elif choix == "4":
            if allume and volume > 0:
                volume -= 1
                print("Le volume a été baissé. Volume actuel :", volume)
            else:
                print("La télévision est éteinte ou le volume est déjà au minimum.")

        elif choix == "5":
            print("Programme terminé.")
            break

        else:
            print("Option invalide. Veuillez sélectionner une option valide.")
