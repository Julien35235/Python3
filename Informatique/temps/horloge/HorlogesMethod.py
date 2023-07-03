def openfileHorlogeMethod():
    import time

    def alarme():
        heure = input("À quelle heure voulez-vous définir l'alarme (format HH:MM:SS) ? ")
        heure_alarme = time.strptime(heure, "%H:%M:%S")  # Convertit l'heure de l'alarme en objet struct_time

        while True:
            heure_actuelle = time.localtime()  # Récupère l'heure actuelle
            if heure_actuelle >= heure_alarme:  # Vérifie si l'heure actuelle est supérieure ou égale à l'heure de l'alarme
                print("Réveillez-vous ! L'heure de l'alarme est arrivée.")
                break

            # Notification : Attente avant de vérifier à nouveau
            time.sleep(1)

    def chronometre():
        heures = int(input("Entrez le nombre d'heures du chronomètre : "))
        minutes = int(input("Entrez le nombre de minutes du chronomètre : "))
        secondes = int(input("Entrez le nombre de secondes du chronomètre : "))

        duree = heures * 3600 + minutes * 60 + secondes  # Convertit la durée en secondes
        start_time = time.time()  # Récupère le temps de départ du chronomètre

        while True:
            temps_ecoule = int(time.time() - start_time)  # Calcule le temps écoulé depuis le départ
            temps_restant = duree - temps_ecoule  # Calcule le temps restant

            if temps_restant <= 0:  # Vérifie si la durée est écoulée
                print("Le chronomètre est terminé.")
                break

            heures_restantes = temps_restant // 3600  # Calcule les heures restantes
            minutes_restantes = (temps_restant % 3600) // 60  # Calcule les minutes restantes
            secondes_restantes = temps_restant % 60  # Calcule les secondes restantes

            # Notification : Affiche le temps écoulé
            print("Temps écoulé :", heures_restantes, "heures", minutes_restantes, "minutes", secondes_restantes,
                  "secondes")

            # Notification : Attente avant de vérifier à nouveau
            time.sleep(1)

    def minuteur():
        heures = int(input("Entrez le nombre d'heures du minuteur : "))
        minutes = int(input("Entrez le nombre de minutes du minuteur : "))
        secondes = int(input("Entrez le nombre de secondes du minuteur : "))

        duree = heures * 3600 + minutes * 60 + secondes  # Convertit la durée en secondes
        start_time = time.time()  # Récupère le temps de départ du minuteur

        while True:
            temps_ecoule = int(time.time() - start_time)  # Calcule le temps écoulé depuis le départ
            temps_restant = duree - temps_ecoule  # Calcule le temps restant

            if temps_restant <= 0:  # Vérifie si le temps restant est inférieur ou égal à zéro
                print("Le minuteur est terminé.")
                break

            heures_restantes = temps_restant // 3600  # Calcule les heures restantes
            minutes_restantes = (temps_restant % 3600) // 60  # Calcule les minutes restantes
            secondes_restantes = temps_restant % 60  # Calcule les secondes restantes

            # Notification : Affiche le temps restant
            print("Temps restant :", heures_restantes, "heures", minutes_restantes, "minutes", secondes_restantes,
                  "secondes")

            # Notification : Attente avant de vérifier à nouveau
            time.sleep(1)

    # Menu principal
    while True:
        print("\n------ MENU ------")
        print("1. Définir une alarme")
        print("2. Lancer un chronomètre")
        print("3. Lancer un minuteur")
        print("4. Quitter")
        choix = input("Choisissez une option : ")

        if choix == "1":
            alarme()
        elif choix == "2":
            chronometre()
        elif choix == "3":
            minuteur()
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")