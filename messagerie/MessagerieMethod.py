def openfilleMessagerieMethod():
    messages = []

    def envoyer_message(destinataire, contenu):
        message = {"destinataire": destinataire, "contenu": contenu}
        messages.append(message)

    def lire_messages(destinataire):
        messages_non_lus = []
        for message in messages:
            if message["destinataire"] == destinataire:
                messages_non_lus.append(message)

        for message in messages_non_lus:
            print(f"De: {message['destinataire']}\nContenu: {message['contenu']}\n")

    def messagerie():
        while True:
            choix = input("Que voulez-vous faire ? (envoyer/lire/quit) ")

            if choix == "envoyer":
                destinataire = input("Destinataire : ")
                contenu = input("Contenu du message : ")
                envoyer_message(destinataire, contenu)
                print("Message envoyé !")

            elif choix == "lire":
                destinataire = input("Destinataire : ")
                print(f"Messages pour {destinataire}:")
                lire_messages(destinataire)

            elif choix == "quit":
                print("Au revoir !")
                break

            else:
                print("Commande invalide. Veuillez réessayer.")

    # Appeler la fonction de messagerie
    messagerie()
