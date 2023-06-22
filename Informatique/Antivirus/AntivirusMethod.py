def openfilleAntivirusMethod():
    import os

    def clear_screen():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def bitdefender():
        clear_screen()
        print("Bitdefender est un puissant antivirus !")

    def norton():
        clear_screen()
        print("Norton est un antivirus populaire avec de nombreuses fonctionnalités.")

    def nordvpn_antivirus():
        clear_screen()
        print("NordVPN Antivirus protège votre système tout en vous offrant une connexion sécurisée.")

    def avast_antivirus():
        clear_screen()
        print("Avast Antivirus propose une protection complète contre les menaces en ligne.")

    def mcafee():
        clear_screen()
        print("McAfee est un antivirus réputé avec une technologie avancée de détection des virus.")

    def avg_ultimate():
        clear_screen()
        print("AVG Ultimate offre une protection complète pour tous vos appareils.")

    def ccleaner():
        clear_screen()
        print("CCleaner est un outil de nettoyage pour optimiser les performances de votre système.")

    def main():
        while True:
            clear_screen()
            print("===== MENU PRINCIPAL - ANTIVIRUS =====")
            print("1. Bitdefender")
            print("2. Norton")
            print("3. NordVPN Antivirus")
            print("4. Avast Antivirus")
            print("5. McAfee")
            print("6. AVG Ultimate")
            print("7. CCleaner")
            print("8. Quitter")

            choice = input("Choisissez un antivirus (1-8) : ")

            if choice == "1":
                bitdefender()
            elif choice == "2":
                norton()
            elif choice == "3":
                nordvpn_antivirus()
            elif choice == "4":
                avast_antivirus()
            elif choice == "5":
                mcafee()
            elif choice == "6":
                avg_ultimate()
            elif choice == "7":
                ccleaner()
            elif choice == "8":
                clear_screen()
                print("Au revoir !")
                break
            else:
                input("Choix invalide. Appuyez sur Entrée pour continuer.")

    if __name__ == "__main__":
        main()
