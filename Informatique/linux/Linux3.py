import os

def afficher_toutes_commandes_linux():
    commande = "compgen -c"
    resultats = os.popen(commande).read()
    commandes = resultats.splitlines()
    for commande in commandes:
        print(commande)

afficher_toutes_commandes_linux()
