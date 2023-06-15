def openfilleConfigurationsMethod():
    import time

    def transferer_fichier(format, serveur_reception, nom_hote, nom_utilisateur, mot_de_passe, serveur_envoi,
                           serveur_primaire, port, chemin_imap, utiliser_ssl):
        print("Transfert du fichier {} en cours...".format(format))
        print("Serveur de réception : {}".format(serveur_reception))
        print("Nom d'hôte : {}".format(nom_hote))
        print("Nom d'utilisateur : {}".format(nom_utilisateur))
        print("Mot de passe : {}".format(mot_de_passe))
        print("Serveur d'envoi : {}".format(serveur_envoi))
        print("Serveur primaire : {}".format(serveur_primaire))
        print("Port : {}".format(port))
        print("Chemin préfixe du IMAP : {}".format(chemin_imap))
        print("Utiliser SSL : {}".format(utiliser_ssl))
        # Simuler le transfert
        time.sleep(2)
        print("Transfert du fichier {} terminé!".format(format))
        print("-----------------------------")

    # Menu principal de configuration
    while True:
        print("---- Menu Configuration ----")
        print("1. Configurer les paramètres de serveur")
        print("0. Quitter")
        print("-----------------------------")

        choix_config = input("Choisissez une option : ")

        if choix_config == "0":
            print("Merci d'avoir utilisé notre programme de transfert de fichiers!")
            break
        elif choix_config == "1":
            serveur_reception = input("Serveur de réception : ")
            nom_hote = input("Nom d'hôte : ")
            nom_utilisateur = input("Nom d'utilisateur : ")
            mot_de_passe = input("Mot de passe : ")
            serveur_envoi = input("Serveur d'envoi : ")
            serveur_primaire = input("Serveur primaire : ")
            port = input("Port : ")
            chemin_imap = input("Chemin préfixe du IMAP : ")
            utiliser_ssl = input("Utiliser SSL (oui/non) : ")
            print("Paramètres de serveur configurés avec succès!")
            print("-----------------------------")
