def openfilleDiplomesMethod():
    def afficher_menu():
        print("Menu principal :")
        print("1. CFG")
        print("2. DNB")
        print("3. BAC")
        print("4. CAP")
        print("5. BTS")
        print("6. DUT")
        print("7. BUT")
        print("8. Quitter")

    def afficher_niveaux_bac():
        print("Niveaux du BAC :")
        print("1. BAC L")
        print("2. BAC ES")
        print("3. BAC S")
        print("4. BAC STMG")
        print("5. Retour")

    def diplome_cfg():
        print("Le Certificat de Formation Générale (CFG).")

    def diplome_dnb():
        print("Le Diplôme National du Brevet (DNB) est un diplôme de fin d'études secondaires en France.")

    def diplome_bac():
        choix_bac = 0
        while choix_bac != 5:
            afficher_niveaux_bac()
            choix_bac = int(input("Choisissez un niveau du BAC (1-5) : "))
            if choix_bac == 1:
                print("BAC L : Bac Littéraire")
            elif choix_bac == 2:
                print("BAC ES : Bac Économique et Social")
            elif choix_bac == 3:
                print("BAC S : Bac Scientifique")
            elif choix_bac == 4:
                print("BAC STMG : Bac Sciences et Technologies du Management et de la Gestion")
            elif choix_bac == 5:
                print("Retour au menu principal")

    def diplome_cap():
        print("Le Certificat d'Aptitude Professionnelle (CAP) est un diplôme d'études professionnelles en France.")

    def diplome_bts():
        print("Le Brevet de Technicien Supérieur (BTS) est un diplôme national de l'enseignement supérieur en France.")

    def diplome_dut():
        print("Le Diplôme Universitaire de Technologie (DUT) est un diplôme de niveau 3 dans le système français.")

    def diplome_but():
        print("Le Bachelor Universitaire de Technologie (BUT) est un diplôme de niveau 2 dans le système français.")

    choix = 0
    while choix != 8:
        afficher_menu()
        choix = int(input("Choisissez une option (1-8) : "))
        if choix == 1:
            diplome_cfg()
        elif choix == 2:
            diplome_dnb()
        elif choix == 3:
            diplome_bac()
        elif choix == 4:
            diplome_cap()
        elif choix == 5:
            diplome_bts()
        elif choix == 6:
            diplome_dut()
        elif choix == 7:
            diplome_but()
        elif choix == 8:
            print("Merci d'avoir utilisé le programme !")
        else:
            print("Option invalide. Veuillez sélectionner une option valide (1-8).")