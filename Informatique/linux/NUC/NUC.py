def afficher_menu():
    print("=== Menu principal ===")
    print("1. Afficher les spécifications du NUC")
    print("2. Modifier les paramètres du NUC")
    print("3. Changer le système d'exploitation")
    print("4. Afficher la liste des systèmes d'exploitation")
    print("5. Quitter")

def afficher_specifications():
    # Ici, tu peux ajouter le code pour afficher les spécifications du NUC
    print("Spécifications du NUC :")
    print("- Marque : Intel")
    print("- Modèle : NUC7i5BNK")
    print("- Processeur : Intel Core i5")
    print("- Mémoire : 8 Go")
    print("- Stockage : 256 Go SSD")
    print("- Système d'exploitation : Windows 10")

def modifier_parametres():
    # Ici, tu peux ajouter le code pour modifier les paramètres du NUC
    print("Modifier les paramètres du NUC :")
    print("1. Changer la mémoire")
    print("2. Changer le stockage")
    choix = input("Saisis ton choix : ")
    if choix == "1":
        nouvelle_memoire = input("Nouvelle taille de mémoire : ")
        print("La mémoire a été changée pour", nouvelle_memoire)
    elif choix == "2":
        nouveau_stockage = input("Nouvelle taille de stockage : ")
        print("Le stockage a été changé pour", nouveau_stockage)
    else:
        print("Choix invalide")

def changer_systeme_exploitation():
    print("Changer le système d'exploitation :")
    nouveau_os = input("Nouveau système d'exploitation : ")
    print("Le système d'exploitation a été changé pour", nouveau_os)

def afficher_liste_systemes_exploitation():
    print("Liste des systèmes d'exploitation :")
    print("- Windows XP (32 bits x86)")
    print("- Windows 7 (32 bits x86) (64 bits x86)")
    print("- Windows 8 (32 bits x86)" )
    print("- Windows 10 (32 bits x86)")
    print("- Windows 11 (32 bits x86) (64 bits x86)")
    print("- Windows Server (32 bits x86) (64 bits x86)")
    print("- Mac OSX")
    print("- CentOS")
    print("- OPNsense")
    print("- Ubuntu")
    print("- Ubuntu Server")
    print("- Debian")
    print("- Fedora")
    print("- Raspberry Pi")
    print("- Arduino")

# Mises à jour de Windows XP
windows_xp_updates = [
    "KB1234567",
    "KB2345678",
    "KB3456789",
    "KB4567890"
]

# Mises à jour de Windows 7
windows7_updates = [
    "KB1234567",
    "KB2345678",
    "KB3456789",
    "KB4567890"
]

# Mises à jour de Windows 11
windows11_updates = [
    "KB1234567",
    "KB2345678",
    "KB3456789",
    "KB4567890",
    "KB5678901",
    "KB6789012"
]

# Versions et mises à jour de Windows XP
versions_windows_xp = {
    "Windows XP": ["Service Pack 1", "Service Pack 2", "Service Pack 3"] + windows_xp_updates,
}

# Versions et mises à jour de Windows 7
versions_windows_7 = {
    "Windows 7": ["Service Pack 1"] + windows7_updates,
}

# Versions et mises à jour de Windows 11
versions_windows_11 = {
    "Windows 11": windows11_updates,
}

# Versions de macOS
versions_macos = {
    "Cheetah": "10.0",
    "Puma": "10.1",
    "Jaguar": "10.2",
    "Panther": "10.3",
    "Tiger": "10.4",
    "Leopard": "10.5",
    "Snow Leopard": "10.6",
    "Lion": "10.7",
    "Mountain Lion": "10.8",
    "Mavericks": "10.9",
    "Yosemite": "10.10",
    "El Capitan": "10.11",
    "Sierra": "10.12",
    "High Sierra": "10.13",
    "Mojave": "10.14",
    "Catalina": "10.15",
    "Big Sur": "11.0",
    "Monterey": "12.0",
    "Ventura": "13.1",
}
# Versions de Raspberry Pi
raspberry_pi_versions = {
    "Raspberry Pi": ["1 Model B", "2 Model B", "3 Model B+", "4 Model B"]
}

# Versions d'Arduino
arduino_versions = {
    "Arduino": ["Uno", "Nano", "Mega"]
}

# Programme principal
while True:
    afficher_menu()
    choix = input("Saisis ton choix : ")
    if choix == "1":
        afficher_specifications()
    elif choix == "2":
        modifier_parametres()
    elif choix == "3":
        changer_systeme_exploitation()
    elif choix == "4":
        afficher_liste_systemes_exploitation()
    elif choix == "5":
        print("Au revoir !")
        break
    else:
        print("Choix invalide")
