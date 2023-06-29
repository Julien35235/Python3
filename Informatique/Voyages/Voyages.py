from datetime import datetime, timedelta

class Voyage:
    def __init__(self, depart, arrivee, heure_depart, duree):
        self.depart = depart
        self.arrivee = arrivee
        self.heure_depart = heure_depart
        self.duree = duree

class Itineraire:
    def __init__(self):
        self.voyages = []

    def ajouter_voyage(self, voyage):
        self.voyages.append(voyage)

    def supprimer_voyage(self, index):
        if index >= 0 and index < len(self.voyages):
            del self.voyages[index]

    def afficher_itineraires(self):
        print("Itinéraires de voyage:")
        for i, voyage in enumerate(self.voyages):
            print(f"{i + 1}. Départ: {voyage.depart} | Arrivée: {voyage.arrivee} | Heure de départ: {voyage.heure_depart} | Durée: {voyage.duree} heures")

    def calculer_eta(self, voyage):
        heure_depart = datetime.strptime(voyage.heure_depart, "%Y-%m-%d %H:%M")
        duree = timedelta(hours=voyage.duree)
        heure_arrivee = heure_depart + duree
        return heure_arrivee.strftime("%Y-%m-%d %H:%M")

# Fonction pour afficher le menu principal
def afficher_menu():
    print("\nMenu principal:")
    print("1. Afficher les itinéraires de voyage")
    print("2. Ajouter un nouvel itinéraire")
    print("3. Supprimer un itinéraire")
    print("4. Quitter")

# Créer un objet Itineraire pour stocker les voyages
itineraire = Itineraire()

while True:
    afficher_menu()
    choix = input("Sélectionnez une option: ")

    if choix == "1":
        itineraire.afficher_itineraires()
    elif choix == "2":
        depart = input("Lieu de départ: ")
        arrivee = input("Lieu d'arrivée: ")
        heure_depart = input("Heure de départ (format: AAAA-MM-JJ HH:MM): ")
        duree = float(input("Durée du voyage (en heures): "))

        nouveau_voyage = Voyage(depart, arrivee, heure_depart, duree)
        itineraire.ajouter_voyage(nouveau_voyage)

        print("L'itinéraire a été ajouté avec succès!")
    elif choix == "3":
        itineraire.afficher_itineraires()
        index_supprimer = int(input("Sélectionnez l'index de l'itinéraire à supprimer: ")) - 1
        itineraire.supprimer_voyage(index_supprimer)
        print("L'itinéraire a été supprimé avec succès!")
    elif choix == "4":
        print("Merci d'avoir utilisé le programme. Au revoir!")
        break
    else:
        print("Option invalide. Veuillez sélectionner une option valide.")