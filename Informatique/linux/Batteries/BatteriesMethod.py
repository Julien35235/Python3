def openfilleBatteriesMethod():
    import os
    import sys

    # Fonction pour afficher le menu principal
    def afficher_menu():
        print("Menu principal:")
        print("1. Informations sur la batterie d'un Mac OSX")
        print("2. Informations sur la batterie de CentOS")
        print("3. Informations sur la batterie d'OPNsense")
        print("4. Informations sur la batterie d'Ubuntu")
        print("5. Informations sur la batterie de Debian")
        print("6. Informations sur la batterie de Fedora")
        print("7. Informations sur la batterie d'un Raspberry Pi")
        print("8. Informations sur la batterie de Windows XP")
        print("9. Informations sur la batterie de Windows 7")
        print("10. Informations sur la batterie de Windows 8")
        print("11. Informations sur la batterie de Windows 10")
        print("12. Informations sur la batterie de Windows 11")
        print("13. Quitter")

    # Fonction pour afficher les informations sur la batterie d'un Mac OSX
    def informations_batterie_mac():
        # Paramètres personnalisés pour Mac OSX
        pourcentage = 75
        statut = "En charge"

        print("Informations sur la batterie d'un Mac OSX")
        print("Pourcentage de batterie:", pourcentage)
        print("Statut de la batterie:", statut)

    # Fonction pour afficher les informations sur la batterie de CentOS
    def informations_batterie_centos():
        # Paramètres personnalisés pour CentOS
        pourcentage = 60
        statut = "Débranché"

        print("Informations sur la batterie de CentOS")
        print("Pourcentage de batterie:", pourcentage)
        print("Statut de la batterie:", statut)

    # Fonction pour afficher les informations sur la batterie d'OPNsense
    def informations_batterie_opnsense():
        # Paramètres personnalisés pour OPNsense
        pourcentage = 80
        statut = "En charge"

        print("Informations sur la batterie d'OPNsense")
        print("Pourcentage de batterie:", pourcentage)
        print("Statut de la batterie:", statut)

    # Fonction pour afficher les informations sur la batterie d'Ubuntu
    def informations_batterie_ubuntu():
        # Paramètres personnalisés pour Ubuntu
        pourcentage = 50
        statut = "Débranché"

        print("Informations sur la batterie d'Ubuntu")
        print("Pourcentage de batterie:", pourcentage)
        print("Statut de la batterie:", statut)

    # Fonction pour afficher les informations sur la batterie de Debian
    def informations_batterie_debian():
        # Paramètres personnalisés pour Debian
        pourcentage = 70
        statut = "En charge"

        print("Informations sur la batterie de Debian")
        print("Pourcentage de batterie:", pourcentage)
        print("Statut de la batterie:", statut)

    # Fonction pour afficher les informations sur la batterie de Fedora
    def informations_batterie_fedora():
        # Paramètres personnalisés pour Fedora
        pourcentage = 90
        statut = "Débranché"

        print("Informations sur la batterie de Fedora")
        print("Pourcentage de batterie:", pourcentage)
        print("Statut de la batterie:", statut)

    # Fonction pour afficher les informations sur la batterie d'un Raspberry Pi
    def informations_batterie_raspberry_pi():
        # Paramètres personnalisés pour Raspberry Pi
        pourcentage = 80
        statut = "En charge"

        print("Informations sur la batterie d'un Raspberry Pi")
        print("Pourcentage de batterie:", pourcentage)
        print("Statut de la batterie:", statut)

    # Fonction pour afficher les informations sur la batterie de Windows XP
    def informations_batterie_windows_xp():
        # Paramètres personnalisés pour Windows XP
        pourcentage = 55
        statut = "Débranché"

        print("Informations sur la batterie de Windows XP")
        print("Pourcentage de batterie:", pourcentage)
        print("Statut de la batterie:", statut)

    # Fonction pour afficher les informations sur la batterie de Windows 7
    def informations_batterie_windows_7():
        # Paramètres personnalisés pour Windows 7
        pourcentage = 65
        statut = "En charge"

        print("Informations sur la batterie de Windows 7")
        print("Pourcentage de batterie:", pourcentage)
        print("Statut de la batterie:", statut)

    # Fonction pour afficher les informations sur la batterie de Windows 8
    def informations_batterie_windows_8():
        # Paramètres personnalisés pour Windows 8
        pourcentage = 45
        statut = "Débranché"

        print("Informations sur la batterie de Windows 8")
        print("Pourcentage de batterie:", pourcentage)
        print("Statut de la batterie:", statut)

    # Fonction pour afficher les informations sur la batterie de Windows 10
    def informations_batterie_windows_10():
        # Paramètres personnalisés pour Windows 10
        pourcentage = 75
        statut = "En charge"

        print("Informations sur la batterie de Windows 10")
        print("Pourcentage de batterie:", pourcentage)
        print("Statut de la batterie:", statut)

    # Fonction pour afficher les informations sur la batterie de Windows 11
    def informations_batterie_windows_11():
        # Paramètres personnalisés pour Windows 11
        pourcentage = 90
        statut = "Débranché"

        print("Informations sur la batterie de Windows 11")
        print("Pourcentage de batterie:", pourcentage)
        print("Statut de la batterie:", statut)

    # Boucle principale du programme
    while True:
        afficher_menu()
        choix = input("Sélectionnez une option (1-13): ")

        if choix == "1":
            informations_batterie_mac()
        elif choix == "2":
            informations_batterie_centos()
        elif choix == "3":
            informations_batterie_opnsense()
        elif choix == "4":
            informations_batterie_ubuntu()
        elif choix == "5":
            informations_batterie_debian()
        elif choix == "6":
            informations_batterie_fedora()
        elif choix == "7":
            informations_batterie_raspberry_pi()
        elif choix == "8":
            informations_batterie_windows_xp()
        elif choix == "9":
            informations_batterie_windows_7()
        elif choix == "10":
            informations_batterie_windows_8()
        elif choix == "11":
            informations_batterie_windows_10()
        elif choix == "12":
            informations_batterie_windows_11()
        elif choix == "13":
            print("Au revoir !")
            sys.exit()
        else:
            print("Option invalide. Veuillez sélectionner une option valide.")