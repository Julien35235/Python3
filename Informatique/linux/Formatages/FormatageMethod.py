def openfilleFormatageMethod():
    import time

    def format_windows_xp():
        print("Formatage du disque dur sur Windows XP en cours...")
        time.sleep(3)
        print("Le disque dur a été formaté avec succès sur Windows XP!")

    def format_windows_7():
        print("Formatage du disque dur sur Windows 7 en cours...")
        time.sleep(3)
        print("Le disque dur a été formaté avec succès sur Windows 7!")

    def format_windows_8():
        print("Formatage du disque dur sur Windows 8 en cours...")
        time.sleep(3)
        print("Le disque dur a été formaté avec succès sur Windows 8!")

    def format_windows_10():
        print("Formatage du disque dur sur Windows 10 en cours...")
        time.sleep(3)
        print("Le disque dur a été formaté avec succès sur Windows 10!")

    def format_windows_11():
        print("Formatage du disque dur sur Windows 11 en cours...")
        time.sleep(3)
        print("Le disque dur a été formaté avec succès sur Windows 11!")

    def format_mac_osx():
        print("Formatage du disque dur sur Mac OSX en cours...")
        time.sleep(3)
        print("Le disque dur a été formaté avec succès sur Mac OSX!")

    def format_centos():
        print("Formatage du disque dur sur CentOS en cours...")
        time.sleep(3)
        print("Le disque dur a été formaté avec succès sur CentOS!")

    def format_kubernetes():
        print("Formatage du disque dur sur Kubernetes en cours...")
        time.sleep(3)
        print("Le disque dur a été formaté avec succès sur Kubernetes!")

    def format_opnsense():
        print("Formatage du disque dur sur OPNsense en cours...")
        time.sleep(3)
        print("Le disque dur a été formaté avec succès sur OPNsense!")

    def format_ubuntu():
        print("Formatage du disque dur sur Ubuntu en cours...")
        time.sleep(3)
        print("Le disque dur a été formaté avec succès sur Ubuntu!")

    def format_ubuntu_server():
        print("Formatage du disque dur sur Ubuntu Server en cours...")
        time.sleep(3)
        print("Le disque dur a été formaté avec succès sur Ubuntu Server!")

    def format_debian():
        print("Formatage du disque dur sur Debian en cours...")
        time.sleep(3)
        print("Le disque dur a été formaté avec succès sur Debian!")

    def format_fedora():
        print("Formatage du disque dur sur Fedora en cours...")
        time.sleep(3)
        print("Le disque dur a été formaté avec succès sur Fedora!")

    def format_raspberry_pi():
        print("Formatage du disque dur sur Raspberry Pi en cours...")
        time.sleep(3)
        print("Le disque dur a été formaté avec succès sur Raspberry Pi!")

    def format_kali():
        print("Formatage du disque dur sur Kali en cours...")
        time.sleep(3)
        print("Le disque dur a été formaté avec succès sur Kali!")

    def format_arduino():
        print("Formatage du disque dur sur Arduino en cours...")
        time.sleep(3)
        print("Le disque dur a été formaté avec succès sur Arduino!")

    # Fonction principale pour afficher le menu et traiter les choix de l'utilisateur
    def menu_principal():
        while True:
            print("\n------ MENU PRINCIPAL ------")
            print("1. Formatage du disque dur sur Windows XP")
            print("2. Formatage du disque dur sur Windows 7")
            print("3. Formatage du disque dur sur Windows 8")
            print("4. Formatage du disque dur sur Windows 10")
            print("5. Formatage du disque dur sur Windows 11")
            print("6. Formatage du disque dur sur Mac OSX")
            print("7. Formatage du disque dur sur CentOS")
            print("8. Formatage du disque dur sur Kubernetes")
            print("9. Formatage du disque dur sur OPNsense")
            print("10. Formatage du disque dur sur Ubuntu")
            print("11. Formatage du disque dur sur Ubuntu Server")
            print("12. Formatage du disque dur sur Debian")
            print("13. Formatage du disque dur sur Fedora")
            print("14. Formatage du disque dur sur Raspberry Pi")
            print("15. Formatage du disque dur sur Kali")
            print("16. Formatage du disque dur sur Arduino")
            print("0. Quitter")

            choix = input("Sélectionnez une option : ")

            if choix == "0":
                print("Au revoir!")
                break
            elif choix == "1":
                format_windows_xp()
            elif choix == "2":
                format_windows_7()
            elif choix == "3":
                format_windows_8()
            elif choix == "4":
                format_windows_10()
            elif choix == "5":
                format_windows_11()
            elif choix == "6":
                format_mac_osx()
            elif choix == "7":
                format_centos()
            elif choix == "8":
                format_kubernetes()
            elif choix == "9":
                format_opnsense()
            elif choix == "10":
                format_ubuntu()
            elif choix == "11":
                format_ubuntu_server()
            elif choix == "12":
                format_debian()
            elif choix == "13":
                format_fedora()
            elif choix == "14":
                format_raspberry_pi()
            elif choix == "15":
                format_kali()
            elif choix == "16":
                format_arduino()
            else:
                print("Option invalide. Veuillez sélectionner une option valide.")

    # Appel de la fonction principale pour lancer le menu
    menu_principal()