# initialisation de la variable 'symbole'
symbole = ''

# définition de la liste des symboles autorisés
symboles_autorises = ['@', '&', 'é', '"', '(', 'è', '§', '!', 'ç', '$', '^', '=', '+', '/', ':', '.', '?', ',', '*', '$', '*', '¨', '-']

# boucle while qui continue tant que 'symbole' n'est pas égal à 'q'
while symbole != 'q':
    # demande à l'utilisateur d'entrer un symbole
    symbole = input("Entrez un symbole (ou 'q' pour quitter) : ")

    # vérifie que le symbole entré est autorisé
    if symbole in symboles_autorises:
        # affiche le symbole entré par l'utilisateur
        print("Vous avez entré le symbole :", symbole)
    else:
        # affiche un message d'erreur si le symbole entré n'est pas autorisé
        print("Symbole non autorisé !")

# affiche un message de sortie
print("Au revoir !")
