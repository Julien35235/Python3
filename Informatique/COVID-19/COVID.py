import pycountry


def afficher_statistiques_mondiales():
    total_cas_confirmes = 1234567
    total_deces = 23456
    total_recuperations = 345678

    print('Statistiques mondiales COVID-19 :')
    print('-------------------------------')
    print(f"Total de cas confirmés : {total_cas_confirmes}")
    print(f"Total de décès : {total_deces}")
    print(f"Total de récupérations : {total_recuperations}")
    print('')


def afficher_statistiques_par_pays():
    pays = input("Entrez le nom du pays : ")
    try:
        country = pycountry.countries.search_fuzzy(pays)[0]
        code_pays = country.alpha_2
        # Vos statistiques COVID-19 par pays ici
        cas_confirmes = 12345
        deces = 234
        recuperations = 3456

        print(f"Statistiques COVID-19 pour {country.name} :")
        print('-------------------------------')
        print(f"Total de cas confirmés : {cas_confirmes}")
        print(f"Total de décès : {deces}")
        print(f"Total de récupérations : {recuperations}")
    except LookupError:
        print("Pays non trouvé.")
    print('')


def verifier_symptomes():
    symptomes = ['fièvre', 'toux sèche', 'fatigue', 'courbatures', 'maux de gorge', 'maux de tête', 'perte de goût ou d'
                 'odorat', 'congestion nasale', 'difficultés respiratoires', 'nausées ou vomissements']
    print('Veuillez répondre par "oui" ou "non".')

    for symptome in symptomes:
        reponse = input(f"Avez-vous {symptome} ? ")
    if reponse.lower() == "oui":
        print("Il est recommandé de consulter un professionnel de la santé.")
    return

    print("Il ne semble pas y avoir de symptômes préoccupants.")


# Menu principal
while True:
    print('Menu principal :')
    print('1. Afficher les statistiques mondiales')
    print('2. Afficher les statistiques par pays')
    print('3. Vérifier les symptômes')
    print('4. Quitter')

    choix = input("Entrez votre choix : ")

    if choix == '1':
        afficher_statistiques_mondiales()
    elif choix == '2':
        afficher_statistiques_par_pays()
    elif choix == '3':
        verifier_symptomes()
    elif choix == '4':
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
    print('')