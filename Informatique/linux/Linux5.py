import time


def fake_mise_a_jour(systeme):
    print(f"Démarrage de la mise à jour pour {systeme}...")
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
            "CentOS", "OPNsense", "openSUSE", "pfSense", "Ubuntu", "Debian", "Deepin", "Fedora", "Raspberry Pi",
            "Synology", "Kali Linux", "Parrot OS", "TrueNAS", "Proxmox", "Oracle Linux",
            "Oracle VM VirtualBox", "UTM Virtual Machine", "VMware", "VMware vSphere 8", "VMware ESXi 8"]

while True:
    print("Menu de mise à jour des systèmes d'exploitation :")
    for i, systeme in enumerate(systemes):
        print(f"{i + 1}. Mise à jour de {systeme}")

    print("0. Quitter")
    choix = input("Veuillez entrer le numéro du système à mettre à jour (ou 0 pour quitter) : ")

    if choix == "0":
        print("Au revoir !")
        break
    elif choix.isdigit():
        choix = int(choix)
        if 1 <= choix <= len(systemes):
            systeme = systemes[choix - 1]
            print(f"Mise à jour du système {systeme}:")
            effectuer_mise_a_jour(systeme)
        else:
            print("Choix invalide. Veuillez sélectionner un numéro valide.")
    else:
        print("Choix invalide. Veuillez entrer un numéro.")

    print()