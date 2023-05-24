class Message:
    def __init__(self, expediteur, contenu):
        self.expediteur = expediteur
        self.contenu = contenu

class AppelTelephonique:
    def __init__(self, numero):
        self.numero = numero
        self.messages = []

    def envoyer_message(self, destinataire, contenu):
        message = Message(destinataire, contenu)
        self.messages.append(message)

    def lire_messages(self):
        if len(self.messages) == 0:
            print("Aucun message.")
        else:
            print("Messages :")
            for message in self.messages:
                print(f"De : {message.expediteur}\nContenu : {message.contenu}\n")
            self.messages = []

    def passer_appel(self, numero):
        print(f"Appel en cours vers le numéro {numero}.")

def messagerie_telephonique():
    numero_telephone = input("Entrez votre numéro de téléphone : ")
    appel = AppelTelephonique(numero_telephone)

    while True:
        choix = input("Que voulez-vous faire ? (appeler/envoyer/lire/quit) ")

        if choix == "appeler":
            numero = input("Entrez le numéro de téléphone : ")
            appel.passer_appel(numero)

        elif choix == "envoyer":
            destinataire = input("Destinataire : ")
            contenu = input("Contenu du message : ")
            appel.envoyer_message(destinataire, contenu)
            print("Message envoyé !")

        elif choix == "lire":
            appel.lire_messages()

        elif choix == "quit":
            print("Au revoir !")
            break

        else:
            print("Commande invalide. Veuillez réessayer.")

# Appeler la fonction de messagerie téléphonique
messagerie_telephonique()
