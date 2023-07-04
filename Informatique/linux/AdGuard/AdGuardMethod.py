def openfilleAdGuardMethod():
    import os
    import subprocess
    from adguardspy import AdGuard

    # Installer AdGuard
    def install_adguard():
        subprocess.call(["bash", "-c",
                         "$(curl -s -S -L https://release.adguard.com/files/AdGuardHome/latest/AdGuardHome_linux_amd64.tar.gz | tar xzf -)"])
        subprocess.call(["./AdGuardHome/AdGuardHome", "-s install"])

    # Démarrer AdGuard
    def start_adguard():
        subprocess.call(["./AdGuardHome/AdGuardHome", "-s start"])

    # Afficher le menu principal
    def show_menu():
        print("\n=== Menu principal ===")
        print("1. Démarrer AdGuard")
        print("2. Arrêter AdGuard")
        print("3. Ajouter un filtre")
        print("4. Supprimer un filtre")
        print("5. Mettre à jour les filtres")
        print("6. Quitter")

    # Créer une instance de l'objet AdGuard
    adguard = AdGuard()

    # Installer AdGuard s'il n'est pas déjà installé
    if not os.path.exists("./AdGuardHome"):
        print("Installation d'AdGuard...")
        install_adguard()

    while True:
        show_menu()
        choice = input("Entrez votre choix : ")

        if choice == "1":
            # Démarrer AdGuard
            start_adguard()
            print("AdGuard démarré.")

            # Connexion à AdGuard
            adguard.connect()

            # Vérifier l'état de connexion
            if adguard.is_connected():
                print("Connecté à AdGuard.")
            else:
                print("Impossible de se connecter à AdGuard.")

        elif choice == "2":
            # Arrêter AdGuard
            subprocess.call(["./AdGuardHome/AdGuardHome", "-s stop"])
            print("AdGuard arrêté.")

        elif choice == "3":
            # Ajouter un filtre
            filter_url = input("Entrez l'URL du filtre à ajouter : ")
            adguard.add_filter(filter_url)
            print("Filtre ajouté : " + filter_url)

        elif choice == "4":
            # Supprimer un filtre
            filter_url = input("Entrez l'URL du filtre à supprimer : ")
            adguard.remove_filter(filter_url)
            print("Filtre supprimé : " + filter_url)

        elif choice == "5":
            # Mettre à jour les filtres
            adguard.update_filters()
            print("Filtres mis à jour.")

        elif choice == "6":
            # Quitter le programme
            break

        else:
            print("Choix invalide. Veuillez réessayer.")