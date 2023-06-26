from datetime import datetime

# Classe représentant un événement dans l'agenda
class Evenement:
    def __init__(self, titre, date_heure):
        self.titre = titre
        self.date_heure = date_heure

# Classe représentant un agenda
class Agenda:
    def __init__(self):
        self.evenements = []

    def ajouter_evenement(self, titre, date_heure):
        evenement = Evenement(titre, date_heure)
        self.evenements.append(evenement)
        print("Événement ajouté à l'agenda.")

    def afficher_evenements(self):
        if len(self.evenements) == 0:
            print("Aucun événement dans l'agenda.")
        else:
            print("Événements dans l'agenda:")
            for evenement in self.evenements:
                print("Titre: {}, Date et heure: {}".format(evenement.titre, evenement.date_heure))

# Fonction pour afficher le menu principal
def afficher_menu():
    print("\nMenu principal:")
    print("1. Afficher les événements de l'agenda")
    print("2. Ajouter un événement à l'agenda")
    print("3. Quitter")

# Fonction principale
def main():
    agenda = Agenda()
    while True:
        afficher_menu()
        choix = input("Veuillez choisir une option (1-3): ")
        if choix == '1':
            agenda.afficher_evenements()
        elif choix == '2':
            titre = input("Veuillez entrer le titre de l'événement: ")
            date_heure_str = input("Veuillez entrer la date et l'heure de l'événement (format: dd/mm/yyyy HH:MM): ")
            try:
                date_heure = datetime.strptime(date_heure_str, "%d/%m/%Y %H:%M")
                agenda.ajouter_evenement(titre, date_heure)
            except ValueError:
                print("Format de date et heure invalide. Veuillez utiliser le format dd/mm/yyyy HH:MM.")
        elif choix == '3':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

# Exécution du programme
if __name__ == '__main__':
    main()