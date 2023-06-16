def openfilleDiplomesMethod():
    def afficher_menu_principal():
        print("=== MENU PRINCIPAL ===")
        print("1. ASSR")
        print("2. ETG")
        print("3. PSC")
        print("4. CFG")
        print("5. DNB")
        print("6. BAC")
        print("7. CAP")
        print("0. Quitter")

    def afficher_menu_assr():
        print("=== MENU ASSR ===")
        print("1. ASSR 1 (Attestation scolaire de sécurité routière de premier niveau)")
        print("2. ASSR 2 (Attestation scolaire de sécurité routière du deuxième niveau)")
        print("0. Retour")

    def afficher_menu_etg():
        print("=== MENU ETG ===")
        print("1. ETG (Épreuve Théorique Générale du permis de conduire)")
        print("0. Retour")

    def afficher_menu_psc():
        print("=== MENU PSC ===")
        print("1. PSC1 (Prévention et secours civiques de niveau 1)")
        print("2. PSC2 (Les Premiers Secours Civiques de niveau 2)")
        print("0. Retour")

    def afficher_menu_cfg():
        print("=== MENU CFG ===")
        print("1. CFG (Certificat de Formation Générale)")
        print("0. Retour")

    def afficher_menu_dnb():
        print("=== MENU DNB ===")
        print("1. DNB (Diplôme National du Brevet)")
        print("0. Retour")

    def afficher_menu_bac():
        print("=== MENU NIVEAUX DU BAC ===")
        print("1. BAC L")
        print("2. BAC ES")
        print("3. BAC S")
        print("4. BAC STMG")
        print("0. Retour")

    def afficher_menu_cap():
        print("=== MENU CAP ===")
        print("1. CAP (Certificat d'Aptitude Professionnelle)")
        print("0. Retour")

    # Fonction principale pour exécuter le script
    def main():
        while True:
            afficher_menu_principal()
            choix_principal = input("Choisissez une option : ")

            if choix_principal == "1":
                while True:
                    afficher_menu_assr()
                    choix_assr = input("Choisissez une option : ")

                    if choix_assr == "1":
                        print("Vous avez choisi l'ASSR 1.")
                        # Faites ce que vous voulez avec l'ASSR 1
                    elif choix_assr == "2":
                        print("Vous avez choisi l'ASSR 2.")
                        # Faites ce que vous voulez avec l'ASSR 2
                    elif choix_assr == "0":
                        break
                    else:
                        print("Option invalide. Veuillez choisir une option valide.")

            elif choix_principal == "2":
                while True:
                    afficher_menu_etg()
                    choix_etg = input("Choisissez une option : ")

                    if choix_etg == "1":
                        print("Vous avez choisi l'ETG.")
                        # Faites ce que vous voulez avec l'ETG
                    elif choix_etg == "0":
                        break
                    else:
                        print("Option invalide. Veuillez choisir une option valide.")

            elif choix_principal == "3":
                while True:
                    afficher_menu_psc()
                    choix_psc = input("Choisissez une option : ")

                    if choix_psc == "1":
                        print("Vous avez choisi le PSC1.")
                        # Faites ce que vous voulez avec le PSC1
                    elif choix_psc == "2":
                        print("Vous avez choisi le PSC2.")
                        # Faites ce que vous voulez avec le PSC2
                    elif choix_psc == "0":
                        break
                    else:
                        print("Option invalide. Veuillez choisir une option valide.")

            elif choix_principal == "4":
                while True:
                    afficher_menu_cfg()
                    choix_cfg = input("Choisissez une option : ")

                    if choix_cfg == "1":
                        print("Vous avez choisi le CFG.")
                        # Faites ce que vous voulez avec le CFG
                    elif choix_cfg == "0":
                        break
                    else:
                        print("Option invalide. Veuillez choisir une option valide.")

            elif choix_principal == "5":
                while True:
                    afficher_menu_dnb()
                    choix_dnb = input("Choisissez une option : ")

                    if choix_dnb == "1":
                        print("Vous avez choisi le DNB.")
                        # Faites ce que vous voulez avec le DNB
                    elif choix_dnb == "0":
                        break
                    else:
                        print("Option invalide. Veuillez choisir une option valide.")

            elif choix_principal == "6":
                while True:
                    afficher_menu_bac()
                    choix_bac = input("Choisissez une option : ")

                    if choix_bac == "1":
                        print("Vous avez choisi le BAC L.")
                        # Faites ce que vous voulez avec le BAC L
                    elif choix_bac == "2":
                        print("Vous avez choisi le BAC ES.")
                        # Faites ce que vous voulez avec le BAC ES
                    elif choix_bac == "3":
                        print("Vous avez choisi le BAC S.")
                        # Faites ce que vous voulez avec le BAC S
                    elif choix_bac == "4":
                        print("Vous avez choisi le BAC STMG.")
                        # Faites ce que vous voulez avec le BAC STMG
                    elif choix_bac == "0":
                        break
                    else:
                        print("Option invalide. Veuillez choisir une option valide.")

            elif choix_principal == "7":
                while True:
                    afficher_menu_cap()
                    choix_cap = input("Choisissez une option : ")

                    if choix_cap == "1":
                        print("Vous avez choisi le CAP.")
                        # Faites ce que vous voulez avec le CAP
                    elif choix_cap == "0":
                        break
                    else:
                        print("Option invalide. Veuillez choisir une option valide.")

            elif choix_principal == "0":
                print("Au revoir !")
                break

            else:
                print("Option invalide. Veuillez choisir une option valide.")

    # Appel de la fonction principale pour exécuter le script
    main()
