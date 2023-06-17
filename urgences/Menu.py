# Fonction pour afficher le menu principal
def afficher_menu_principal():
    print("=== Menu Principal ===")
    print("1. Stop The Ped")
    print("2. Questions sur la personne")
    print("3. Ultimate Backup")
    print("4. Appeler les sapeurs-pompiers")
    print("5. Quitter")

# Fonction pour afficher le menu Stop The Ped
def afficher_menu_stop_the_ped():
    print("=== Menu Stop The Ped ===")
    print("1. Request Ped Check")
    print("2. Request Vehicle Check")
    print("3. Search The Vehicle")
    print("4. Call Transport for Suspect")
    print("5. Request Tow Service")
    print("6. Call Vehicle Insurance")
    print("7. Slow Down Traffic")
    print("8. Stop Traffic")
    print("9. Request End Callout")
    print("10. Retour au menu principal")

# Fonction pour afficher le menu des questions sur la personne
def afficher_menu_questions_personne():
    print("=== Menu Questions sur la personne ===")
    print("1. Vous avez bu ?")
    print("2. Vous avez consommé de la drogue récemment ?")
    print("3. Vous n'avez rien d'illégal sur vous ?")
    print("4. Que faites-vous ?")
    print("5. Vous allez où ?")
    print("6. Vous habitez dans les environs ?")
    print("7. Êtes-vous recherché ?")
    print("8. Retour au menu principal")

# Fonction pour afficher le menu Ultimate Backup
def afficher_menu_ultimate_backup():
    print("=== Menu Ultimate Backup ===")
    print("1. Appeler du renfort Patrol Unité")
    print("2. Appeler la Police nationale (PN)")
    print("3. Appeler la Police municipale (PM)")
    print("4. Appeler la Police nationale à Vélo ou à VTT")
    print("5. Appeler un Agent de surveillance de la voie publique (ASVP)")
    print("6. Appeler la brigade équestre")
    print("7. Appeler la BAC (anti-criminalité)")
    print("8. Appeler les brigades des stupéfiants (BS)")
    print("9. Appeler une mission de lutte anti-drogue (MILAD)")
    print("10. Appeler les CRS (Les Compagnies Républicaines de la Sécurité)")
    print("11. Appeler le Groupe d'intervention de la Police nationale (GIPN)")
    print("12. Appeler BRAV-M (Brigade de répression des actions violentes motorisées)")
    print("13. Appeler un Officier de police judiciaire (OPJ)")
    print("14. Appeler les Douanes")
    print("15. Appeler la Direction centrale de la Police aux frontières")
    print("16. Appeler Raide (Recherche assistance intervention dissuasion)")
    print("17. Appeler la Brigade de recherche et d'intervention (BRI)")
    print("18. Appeler la Gendarmerie nationale (GN)")
    print("19. Appeler le PSIG (Peloton de surveillance et d'intervention de la Gendarmerie)")
    print("20. Appeler le GIGN (Groupe d'intervention de la gendarmerie nationale)")
    print("21. Retour au menu principal")

# Fonction pour afficher le menu des sapeurs-pompiers
def afficher_menu_sapeurs_pompiers():
    print("=== Menu Sapeurs-Pompiers ===")
    print("1. Ambulance (EMS)")
    print("2. Véhicule de secours et d’assistance aux victimes (VSAV)")
    print("3. Véhicule secours routier (VSR)")
    print("4. Grande échelle, ou échelle pivotante automatique (EPA)")
    print("5. Bras (Mât) Elévateur Articulé (BEA (MEA)")
    print("6. Fourgon pompe-tonne (FPT)")
    print("7. Camion-citerne feux de forêts (CCF)")
    print("8. Véhicule poste de commandement (VPC)")
    print("9. Bateau Léger de Sauvetage (BLS)")
    print("10. Bateau de Reconnaissance et de Sauvetage (BRS)")
    print("11. Camion Citerne Grande Capacité (CCGC)")
    print("12. Cellule Mobile d'Intervention Chimique (CMIC)")
    print("13. Fourgon Pompe Tonne / Camion Citerne Rural (FPT, CCR)")
    print("14. Moto Pompe remorquable (MPR)")
    print("15. Remorque Moto Ventilateur Grand Débit (RMVGD)")
    print("16. Véhicule Léger de Commandement / Véhicule Léger Officier Permanence de Secteur (VLC / VLOPS)")
    print("17. Véhicule d'Intervention en Milieux Périlleux (VIMP)")
    print("18. Véhicule d'Intervention sur Risques Technologiques (VIRT)")
    print("19. Véhicule de Liaison Hors-Route (VLHR)")
    print("20. Véhicule Poste de Commandement / Poste de Commandement Mobile (VPC / PCM)")
    print("21. Véhicule Porteur de Cellule (VPCE)")
    print("22. Véhicule de Plongeurs (VPL)")
    print("23. Véhicule de Secours Routier / Fourgon Pompe-Tonne Secours Routier (VSR / FPTSR)")
    print("24. Véhicule de Soutien Sanitaire (VSS)")
    print("25. Dragon")
    print("26. Smur")
    print("27. Retour au menu principal")

# Boucle principale du programme
while True:
    afficher_menu_principal()
    choix_principal = input("Sélectionnez une option : ")

    if choix_principal == "1":
        while True:
            afficher_menu_stop_the_ped()
            choix_stop_the_ped = input("Sélectionnez une option : ")

            # Effectuer les actions en fonction du choix
            if choix_stop_the_ped == "1":
                nom_personne = input("Entrez le nom de la personne : ")
                print("Action Request Ped Check pour", nom_personne)
            elif choix_stop_the_ped == "2":
                plaque_immatriculation = input("Entrez la plaque d'immatriculation : ")
                print("Action Request Vehicle Check pour la plaque", plaque_immatriculation)
            elif choix_stop_the_ped == "3":
                print("Action Search The Vehicle")
            elif choix_stop_the_ped == "4":
                print("Action Call Transport for Suspect")
            elif choix_stop_the_ped == "5":
                print("Action Request Tow Service")
            elif choix_stop_the_ped == "6":
                print("Action Call Vehicle Insurance")
            elif choix_stop_the_ped == "7":
                print("Action Slow Down Traffic")
            elif choix_stop_the_ped == "8":
                print("Action Stop Traffic")
            elif choix_stop_the_ped == "9":
                print("Action Request End Callout")
            elif choix_stop_the_ped == "10":
                break  # Retourner au menu principal
            else:
                print("Option invalide")

    elif choix_principal == "2":
        while True:
            afficher_menu_questions_personne()
            choix_questions_personne = input("Sélectionnez une option : ")

            # Effectuer les actions en fonction du choix
            if choix_questions_personne == "1":
                print("Action Vous avez bu ?")
            elif choix_questions_personne == "2":
                print("Action Vous avez consommé de la drogue récemment ?")
            elif choix_questions_personne == "3":
                print("Action Vous n'avez rien d'illégal sur vous ?")
            elif choix_questions_personne == "4":
                print("Action Que faites-vous ?")
            elif choix_questions_personne == "5":
                print("Action Vous allez où ?")
            elif choix_questions_personne == "6":
                print("Action Vous habitez dans les environs ?")
            elif choix_questions_personne == "7":
                print("Action Êtes-vous recherché ?")
            elif choix_questions_personne == "8":
                break  # Retourner au menu principal
            else:
                print("Option invalide")

    elif choix_principal == "3":
        while True:
            afficher_menu_ultimate_backup()
            choix_ultimate_backup = input("Sélectionnez une option : ")

            # Effectuer les actions en fonction du choix
            if choix_ultimate_backup == "1":
                print("Action Appeler du renfort Patrol Unité")
            elif choix_ultimate_backup == "2":
                print("Action Appeler la Police nationale (PN)")
            elif choix_ultimate_backup == "3":
                print("Action Appeler la Police municipale (PM)")
            elif choix_ultimate_backup == "27":
                print("Action Appeler les Sapeurs-Pompiers")
            elif choix_ultimate_backup == "28":
                break  # Retourner au menu principal
            else:
                print("Option invalide")

    elif choix_principal == "4":
        while True:
            afficher_menu_sapeurs_pompiers()
            choix_sapeurs_pompiers = input("Sélectionnez une option : ")

            # Effectuer les actions en fonction du choix
            if choix_sapeurs_pompiers == "1":
                print("Action Appeler une ambulance (EMS)")
            elif choix_sapeurs_pompiers == "2":
                print("Action Appeler un Véhicule de secours et d’assistance aux victimes (VSAV)")
            elif choix_sapeurs_pompiers == "3":
                print("Action Appeler un Véhicule secours routier (VSR)")
            elif choix_sapeurs_pompiers == "4":
                print("Action Appeler une grande échelle, ou échelle pivotante automatique (EPA)")
            elif choix_sapeurs_pompiers == "5":
                print("Action Appeler un Bras (Mât) Elévateur Articulé (BEA (MEA))")
            elif choix_sapeurs_pompiers == "26":
                print("Action Appeler les Smur")
            elif choix_sapeurs_pompiers == "27":
                break  # Retourner au menu principal
            else:
                print("Option invalide")

    elif choix_principal == "5":
        print("Programme terminé.")
        break  # Quitter le programme

    else:
        print("Option invalide")
