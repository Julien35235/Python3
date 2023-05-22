import platform
import os

# Vérifier le système d'exploitation
if platform.system() == "Windows":
    print("Ce code s'exécute sous Windows 10.")
    # Ouvrir l'Explorateur de fichiers
    os.startfile("explorer.exe")

elif platform.system() == "Julien":
    print("Ce code s'exécute sous macOS.")
    # Ouvrir le Finder
    os.system("open -a Finder")

else:
    print("Ce code s'exécute sur un système d'exploitation inconnu.")

# Obtenir le nom d'utilisateur actuel
username = os.getlogin()
print("L'utilisateur actuel est :", username)

# Écrire dans un fichier texte
with open("mon_fichier.txt", "w") as f:
    f.write("Ceci est un exemple de fichier texte écrit en Python.")

# Lire le contenu du fichier texte
with open("mon_fichier.txt", "r") as f:
    contenu = f.read()
    print("Contenu du fichier :", contenu)
