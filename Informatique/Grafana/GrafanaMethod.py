def openfilleGrafanaMethod():
    import sys

    # Fonction pour afficher le menu principal
    def afficher_menu_principal():
        print("=== MENU PRINCIPAL ===")
        print("1. Créer un tableau de bord")
        print("2. Lister les tableaux de bord existants")
        print("3. Supprimer un tableau de bord")
        print("4. Quitter")
        print("======================")

    # Fonction pour créer un tableau de bord
    def creer_tableau_de_bord():
        print("=== CRÉER UN TABLEAU DE BORD ===")
        nom_tableau_de_bord = input("Entrez le nom du tableau de bord : ")
        description = input("Entrez la description du tableau de bord : ")

        # Code pour créer un tableau de bord dans Grafana
        # Remplacez cette partie avec la logique appropriée pour interagir avec Grafana

        print("Le tableau de bord a été créé avec succès !")

    # Fonction pour lister les tableaux de bord existants
    def lister_tableaux_de_bord():
        print("=== LISTE DES TABLEAUX DE BORD ===")
        # Code pour récupérer et afficher la liste des tableaux de bord depuis Grafana
        # Remplacez cette partie avec la logique appropriée pour interagir avec Grafana

        print("Tableaux de bord non disponibles.")

    # Fonction pour supprimer un tableau de bord
    def supprimer_tableau_de_bord():
        print("=== SUPPRIMER UN TABLEAU DE BORD ===")
        id_tableau_de_bord = input("Entrez l'ID du tableau de bord à supprimer : ")

        # Code pour supprimer un tableau de bord dans Grafana
        # Remplacez cette partie avec la logique appropriée pour interagir avec Grafana

        print("Le tableau de bord a été supprimé avec succès !")

    # Boucle principale du menu
    while True:
        afficher_menu_principal()
        choix = input("Votre choix : ")

        if choix == "1":
            creer_tableau_de_bord()
        elif choix == "2":
            lister_tableaux_de_bord()
        elif choix == "3":
            supprimer_tableau_de_bord()
        elif choix == "4":
            print("Au revoir !")
            sys.exit(0)
        else:
            print("Choix invalide. Veuillez réessayer.")