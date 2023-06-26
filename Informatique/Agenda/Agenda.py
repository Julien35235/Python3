from datetime import datetime

def afficher_menu():
    print("MENU PRINCIPAL")
    print("1. Afficher l'emploi du temps")
    print("2. Ajouter un événement à l'emploi du temps")
    print("3. Supprimer un événement de l'emploi du temps")
    print("4. Quitter")

def afficher_emploi_du_temps(emploi_du_temps):
    if not emploi_du_temps:
        print("L'emploi du temps est vide.")
    else:
        print("EMPLOI DU TEMPS")
        for date, evenements in emploi_du_temps.items():
            print(f"{date}:")
            for heure, evenement in evenements.items():
                print(f"  {heure}: {evenement}")

def ajouter_evenement(emploi_du_temps):
    date_str = input("Date de l'événement (JJ/MM/AAAA) : ")
    heure = input("Heure de l'événement (HH:MM) : ")
    evenement = input("Description de l'événement : ")

    try:
        date = datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        print("Format de date invalide. Veuillez utiliser le format JJ/MM/AAAA.")
        return

    if date not in emploi_du_temps:
        emploi_du_temps[date] = {}

    emploi_du_temps[date][heure] = evenement
    print("Événement ajouté avec succès à l'emploi du temps.")

def supprimer_evenement(emploi_du_temps):
    date_str = input("Date de l'événement à supprimer (JJ/MM/AAAA) : ")
    heure = input("Heure de l'événement à supprimer (HH:MM) : ")

    try:
        date = datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        print("Format de date invalide. Veuillez utiliser le format JJ/MM/AAAA.")
        return

    if date in emploi_du_temps and heure in emploi_du_temps[date]:
        del emploi_du_temps[date][heure]
        print("Événement supprimé avec succès de l'emploi du temps.")
        if not emploi_du_temps[date]:
            del emploi_du_temps[date]
    else:
        print("Aucun événement trouvé à cette date et heure.")

emploi_du_temps = {}

while True:
    afficher_menu()
    choix = input("Votre choix : ")

    if choix == "1":
        afficher_emploi_du_temps(emploi_du_temps)
    elif choix == "2":
        ajouter_evenement(emploi_du_temps)
    elif choix == "3":
        supprimer_evenement(emploi_du_temps)
    elif choix == "4":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")