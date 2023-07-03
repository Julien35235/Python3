from datetime import datetime

def ajouter_rendez_vous():
    titre = input("Entrez le titre du rendez-vous: ")
    date_str = input("Entrez la date du rendez-vous (format: JJ/MM/AAAA): ")
    heure_str = input("Entrez l'heure du rendez-vous (format: HH:MM AM/PM): ")
    date_heure_str = date_str + " " + heure_str
    date_heure = datetime.strptime(date_heure_str, "%d/%m/%Y %I:%M %p")
    rendez_vous = {"titre": titre, "date_heure": date_heure}
    emploi_du_temps.append(rendez_vous)
    print("Rendez-vous ajouté avec succès.")


def afficher_rendez_vous():
    if not emploi_du_temps:
        print("Aucun rendez-vous dans l'emploi du temps.")
    else:
        print("Voici les rendez-vous dans l'emploi du temps:")
        for idx, rendez_vous in enumerate(emploi_du_temps):
            print(f"{idx + 1}. {rendez_vous['titre']}")
            print(f"   Date et heure: {rendez_vous['date_heure']}")

def supprimer_rendez_vous():
    afficher_rendez_vous()
    choix = input("Entrez le numéro du rendez-vous à supprimer: ")
    try:
        index = int(choix) - 1
        if 0 <= index < len(emploi_du_temps):
            rendez_vous_supprime = emploi_du_temps.pop(index)
            print(f"Le rendez-vous '{rendez_vous_supprime['titre']}' a été supprimé.")
        else:
            print("Numéro de rendez-vous invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")

# Emploi du temps initial
emploi_du_temps = []

# Menu principal
while True:
    print("\n=== Menu Principal ===")
    print("1. Ajouter un rendez-vous")
    print("2. Afficher les rendez-vous")
    print("3. Supprimer un rendez-vous")
    print("4. Quitter")

    choix = input("Entrez votre choix (1-4): ")

    if choix == "1":
        ajouter_rendez_vous()
    elif choix == "2":
        afficher_rendez_vous()
    elif choix == "3":
        supprimer_rendez_vous()
    elif choix == "4":
        print("Au revoir!")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")