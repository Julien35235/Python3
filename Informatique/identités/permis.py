# Initialisation des variables
nom = ""
prenom = ""
date_naissance = ""
lieu_naissance = ""
date_delivrance = ""
numero_permis = ""

# Demande des informations jusqu'à ce que tous les champs soient remplis
while not (nom and prenom and date_naissance and lieu_naissance and date_delivrance and numero_permis):
    # Demande du nom et prénom
    nom = input("Entrez votre nom : ")
    prenom = input("Entrez votre prénom : ")

    # Demande de la date de naissance
    date_naissance = input("Entrez votre date de naissance (format JJ/MM/AAAA) : ")

    # Demande du lieu de naissance
    lieu_naissance = input("Entrez votre lieu de naissance : ")

    # Demande de la date de délivrance du permis
    date_delivrance = input("Entrez la date de délivrance du permis (format JJ/MM/AAAA) : ")

    # Demande du numéro de permis
    numero_permis = input("Entrez le numéro de permis : ")

# Affichage du permis de conduire
print("\n========================================")
print("PERMIS DE CONDUIRE")
print("Nom complet :", prenom, nom)
print("Date de naissance :", date_naissance)
print("Lieu de naissance :", lieu_naissance)
print("Date de délivrance :", date_delivrance)
print("Numéro de permis :", numero_permis)
print("========================================")
