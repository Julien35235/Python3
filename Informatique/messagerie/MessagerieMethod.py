def openfilleMessagerieMethod():
    def afficher_menu_principal():
        print("=== Messagerie ===")
        print("1. Appeler")
        print("2. Envoyer un message")
        print("3. Lire les messages")
        print("4. Écouter la messagerie")
        print("5. Quitter")

    def appeler(numero):
        print(f"=== Appeler {numero} ===")
        # Code pour simuler un appel vers le numéro spécifié

    def envoyer_message(destinataire, message):
        print(f"=== Envoyer un message à {destinataire} ===")
        # Code pour simuler l'envoi d'un message au destinataire spécifié avec le contenu du message

    def lire_messages():
        print("=== Boîte de réception ===")
        # Code pour simuler la lecture des messages dans la boîte de réception

    def ecouter_messagerie():
        print("=== Écouter la messagerie ===")
        # Code pour simuler l'écoute de la messagerie vocale

    # Boucle principale du programme
    while True:
        afficher_menu_principal()
        choix = input("Choisissez une option : ")

        if choix == "1":
            numero = input("Entrez le numéro à appeler : ")
            appeler(numero)
        elif choix == "2":
            destinataire = input("Entrez le destinataire : ")
            message = input("Entrez le contenu du message : ")
            envoyer_message(destinataire, message)
        elif choix == "3":
            lire_messages()
        elif choix == "4":
            ecouter_messagerie()
        elif choix == "5":
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")
