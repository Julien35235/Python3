import time


def fake_mise_a_jour(systeme):
    print(f"Démarrage de la fausse mise à jour pour {systeme}...")
    time.sleep(2)

    print("Vérification des mises à jour disponibles...")
    time.sleep(2)

    print("Téléchargement de la mise à jour...")
    time.sleep(4)

    print("Installation de la mise à jour...")
    time.sleep(3)

    print("Redémarrage du système...")
    time.sleep(2)

    print(f"Mise à jour terminée avec succès pour {systeme}!")


def demander_confirmation(systeme):
    while True:
        reponse = input(f"Voulez-vous effectuer une mise à jour du système {systeme} ? (oui/non) ")
        if reponse.lower() == "oui":
            return True
        elif reponse.lower() == "non":
            return False
        else:
            print("Veuillez répondre par 'oui' ou 'non'.")


def effectuer_mise_a_jour(systeme):
    confirmation = demander_confirmation(systeme)

    if confirmation:
        fake_mise_a_jour(systeme)
    else:
        print(f"Aucune mise à jour ne sera effectuée pour {systeme}.")


# Liste des systèmes d'exploitation
systemes = ["Mac OS", "Windows XP", "Windows 7", "Windows 8", "Windows 10", "Windows 11",
            "CentOS", "OpenSUSE", "Ubuntu", "Debian", "Fedora", "Raspberry Pi"]

# Itération sur chaque système d'exploitation
for systeme in systemes:
    print(f"Mise à jour du système {systeme}:")
    effectuer_mise_a_jour(systeme)
    print()

