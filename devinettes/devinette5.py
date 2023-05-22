# Liste des urgences
urgences = ["pompiers", "police", "SAMU"]

# Boucle de jeu
while True:
    # Demander à l'utilisateur de saisir une réponse
    reponse = input("Quelle est l'urgence dont je parle ? ")

    # Vérifier si la réponse est correcte
    if reponse.lower() in urgences:
        print("Bravo, c'est la bonne réponse !")
        break
    else:
        print("Désolé, ce n'est pas la bonne réponse. Essayez encore.")
