# Fonction pour appeler les sapeurs-pompiers
def appeler_sapeurs_pompiers():
    print("Appel en cours aux sapeurs-pompiers...")

    # Code pour appeler les sapeurs-pompiers
    # ...

    print("Les sapeurs-pompiers ont été appelés.")

# Fonction pour appeler le SMUR
def appeler_smur():
    print("Appel en cours au SMUR...")

    # Code pour appeler le SMUR
    # ...

    print("Le SMUR a été appelé.")

# Boucle principale
while True:
    choix = input("Qui voulez-vous appeler ? (sapeurs-pompiers / smur / quitter) ")

    if choix == "sapeurs-pompiers":
        appeler_sapeurs_pompiers()
    elif choix == "smur":
        appeler_smur()
    elif choix == "quitter":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
