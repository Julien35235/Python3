def afficher_menu():
    print("Menu Principal:")
    print("1. Vérifier le solde")
    print("2. Acheter un forfait")
    print("3. Consulter les informations du réseau")
    print("4. Quitter")

def verifier_solde(reseau):
    if reseau == "3G":
        tarif = 45
    elif reseau == "4G":
        tarif = 65
    elif reseau == "5G":
        tarif = 75

    return tarif

def acheter_forfait(reseau, solde):
    tarif = verifier_solde(reseau)
    if solde >= tarif:
        solde -= tarif
        print("Forfait pour le réseau", reseau, "acheté avec succès! Montant débité :", tarif, "€.")
    else:
        print("Solde insuffisant. Veuillez recharger votre compte.")

    return solde

def consulter_informations_reseau(reseau):
    print("Informations du réseau", reseau, ":")
    print("Signal: Fort")

reseau_actuel = "3G"
solde = 100

while True:
    afficher_menu()
    choix = input("Entrez votre choix (1-4): ")

    if choix == "1":
        tarif = verifier_solde(reseau_actuel)
        print("Votre solde pour le réseau", reseau_actuel, "est de", solde, "€.")
    elif choix == "2":
        solde = acheter_forfait(reseau_actuel, solde)
    elif choix == "3":
        consulter_informations_reseau(reseau_actuel)
    elif choix == "4":
        print("Merci d'avoir utilisé notre service. Votre solde final est de", solde, "€.")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
