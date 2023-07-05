def cours_maths(classe):
    print("Cours de Mathématiques pour la", classe)
    # Votre code pour le cours de mathématiques

def cours_histoire_geo_emc(classe):
    print("Cours d'Histoire-Géographie-EMC pour la", classe)
    # Votre code pour le cours d'histoire-géographie-EMC

def cours_francais(classe):
    print("Cours de Français pour la", classe)
    # Votre code pour le cours de français

def cours_anglais(classe):
    print("Cours d'Anglais pour la", classe)
    # Votre code pour le cours d'anglais

def cours_latin(classe):
    print("Cours de Latin pour la", classe)
    # Votre code pour le cours de latin

def cours_physique_chimie(classe):
    print("Cours de Physique-Chimie pour la", classe)
    # Votre code pour le cours de physique-chimie

def cours_technologie(classe):
    print("Cours de Technologie pour la", classe)
    # Votre code pour le cours de technologie

def cours_svt(classe):
    print("Cours de SVT pour la", classe)
    # Votre code pour le cours de SVT

def menu_principal():
    print("Bienvenue dans le menu principal !")
    print("Veuillez choisir une classe :")
    print("1. 6ème")
    print("2. 5ème")
    print("3. 4ème")
    print("4. 3ème")
    print("5. 2nde")
    print("6. Quitter")

    choix_classe = input("Entrez le numéro de la classe : ")

    if choix_classe == '1':
        menu_cours('6ème')
    elif choix_classe == '2':
        menu_cours('5ème')
    elif choix_classe == '3':
        menu_cours('4ème')
    elif choix_classe == '4':
        menu_cours('3ème')
    elif choix_classe == '5':
        menu_cours('2nde')
    elif choix_classe == '6':
        print("Au revoir !")
    else:
        print("Choix invalide. Veuillez entrer un numéro valide.")

def menu_cours(classe):
    print("Veuillez choisir un cours pour la", classe, ":")
    print("1. Mathématiques")
    print("2. Histoire-Géographie-EMC")
    print("3. Français")
    print("4. Anglais")
    print("5. Latin")
    print("6. Physique-Chimie")
    print("7. Technologie")
    print("8. SVT")
    print("9. Retour au menu principal")

    choix_cours = input("Entrez le numéro du cours : ")

    if choix_cours == '1':
        cours_maths(classe)
    elif choix_cours == '2':
        cours_histoire_geo_emc(classe)
    elif choix_cours == '3':
        cours_francais(classe)
    elif choix_cours == '4':
        cours_anglais(classe)
    elif choix_cours == '5':
        cours_latin(classe)
    elif choix_cours == '6':
        cours_physique_chimie(classe)
    elif choix_cours == '7':
        cours_technologie(classe)
    elif choix_cours == '8':
        cours_svt(classe)
    elif choix_cours == '9':
        menu_principal()
    else:
        print("Choix invalide. Veuillez entrer un numéro valide.")

# Appel de la fonction menu_principal pour exécuter le script
menu_principal()