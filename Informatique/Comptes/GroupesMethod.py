def openfilleGrouoesMethod():
    def afficher_menu():
        print("Bienvenue dans notre groupe sur les réseaux sociaux !")
        print("1. Youtube")
        print("2. Twitch")
        print("3. Discord")
        print("4. Signal")
        print("5. WhatsApp")
        print("6. Microsoft Teams")
        print("7. Google Drive")
        print("8. Google Chat")
        print("9. Google Docs")
        print("10. Team Viewer")
        print("11. Google Agenda")
        print("12. FaceTime")
        print("13. Messages")
        print("14. Contacts")
        print("15. Téléphone")
        print("16. Google Classroom")
        print("17. Gmail")
        print("0. Quitter")

    def executer_option(option):
        if option == 1:
            print("Vous avez choisi Youtube.")
            # Code pour Youtube
        elif option == 2:
            print("Vous avez choisi Twitch.")
            # Code pour Twitch
        elif option == 3:
            print("Vous avez choisi Discord.")
            # Code pour Discord
        elif option == 4:
            print("Vous avez choisi Signal.")
            # Code pour Signal
        elif option == 5:
            print("Vous avez choisi WhatsApp.")
            # Code pour WhatsApp
        elif option == 6:
            print("Vous avez choisi Microsoft Teams.")
            # Code pour Microsoft Teams
        elif option == 7:
            print("Vous avez choisi Google Drive.")
            # Code pour Google Drive
        elif option == 8:
            print("Vous avez choisi Google Chat.")
            # Code pour Google Chat
        elif option == 9:
            print("Vous avez choisi Google Docs.")
            # Code pour Google Docs
        elif option == 10:
            print("Vous avez choisi Team Viewer.")
            # Code pour Team Viewer
        elif option == 11:
            print("Vous avez choisi Google Agenda.")
            # Code pour Google Agenda
        elif option == 12:
            print("Vous avez choisi FaceTime.")
            # Code pour FaceTime
        elif option == 13:
            print("Vous avez choisi Messages.")
            # Code pour Messages
        elif option == 14:
            print("Vous avez choisi Contacts.")
            # Code pour Contacts
        elif option == 15:
            print("Vous avez choisi Téléphone.")
            # Code pour Téléphone
        elif option == 16:
            print("Vous avez choisi Google Classroom.")
            # Code pour Google Classroom
        elif option == 17:
            print("Vous avez choisi Gmail.")
            # Code pour Gmail
        elif option == 0:
            print("Au revoir !")
        else:
            print("Option invalide. Veuillez choisir une option valide.")

    # Boucle principale
    while True:
        afficher_menu()
        choix = int(input("Choisissez une option : "))
        executer_option(choix)
        if choix == 0:
            break
