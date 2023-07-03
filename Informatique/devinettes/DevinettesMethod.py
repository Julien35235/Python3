def openfilleDevinettesMethod():
    import random

    # Définir une liste de devinettes et leurs réponses correspondantes
    devinettes = [
        ("Qu'est-ce qui est toujours devant vous mais vous ne pouvez jamais l'atteindre?", "L'horizon"),
        (
            "Je suis prise en quittant, je suis prise en restant, je suis prise en mangeant, mais jamais en buvant. Qu'est-ce que je suis ?",
            "Une photo"),
        ("Qu'est-ce qui peut être mesuré mais n'a pas de longueur, de largeur ou de hauteur ?", "Le temps"),
        (
            "Il y a un pont de 50 mètres de long. Des chiens y circulent en laisse à une vitesse de 4 km/h. Combien de temps leur faudra-t-il pour traverser le pont ?",
            "Aucun, les chiens ne conduisent pas et ne peuvent pas traverser le pont sans être accompagnés par une personne"),
        ("Qu'est-ce qui commence par E, qui ne contient qu'une lettre, mais qui contient toutes les autres lettres?",
         "Une enveloppe")
    ]

    # Choisir une devinette aléatoire
    devinette, reponse = random.choice(devinettes)

    # Initialiser les variables pour le jeu de "pendu"
    lettres_trouvees = set()
    lettres_tentees = set()
    nb_coups_restants = 6

    # Boucle principale du jeu
    while nb_coups_restants > 0:
        # Afficher la devinette avec des underscores pour les lettres non trouvées
        affichage = ""
        for lettre in reponse:
            if lettre in lettres_trouvees:
                affichage += lettre
            else:
                affichage += "_"
        print("Devinez la réponse: ", affichage)

        # Demander une lettre à l'utilisateur
        lettre = input("Entrez une lettre: ")
        if lettre in lettres_tentees:
            print("Vous avez déjà essayé cette lettre!")
        elif lettre in reponse:
            lettres_trouvees.add(lettre)
            print("Bravo! La lettre est dans la réponse.")
        else:
            nb_coups_restants -= 1
            print("Dommage, la lettre n'est pas dans la réponse.")

        lettres_tentees.add(lettre)

        # Vérifier si l'utilisateur a trouvé toutes les lettres de la réponse
        if set(reponse) == lettres_trouvees:
            print("Félicitations, vous avez deviné la réponse!")
            break

    # Si l'utilisateur n'a pas trouvé la réponse, afficher la réponse correcte
    if nb_coups_restants == 0:
        print("Dommage, vous avez perdu. La réponse était:", reponse)
