import os

# Chemin vers le répertoire contenant les commandes Linux
path = "/bin"

# Liste des fichiers du répertoire /bin
files = os.listdir(path)

# Compteur d'index
i = 0

# Boucle while pour parcourir tous les fichiers du répertoire /bin
while i < len(files):
    print(files[i])
    i += 1
