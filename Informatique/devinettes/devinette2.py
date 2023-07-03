import random

# Définir une liste de devinettes et leurs réponses correspondantes
devinettes = [
    ("Qu'est-ce qui est petit, noir et qui saute ?", "Une puce"),
    ("Qu'est-ce qui est jaune et qui attend ?", "Jonathan"),
    ("Qu'est-ce qui est transparent et qui court dans un pré ?", "Un troupeau de vitres")
]

# Mélanger les devinettes
random.shuffle(devinettes)

# Parcourir chaque devinette et demander à l'utilisateur de deviner
for devinette, reponse in devinettes:
    print(devinette)
    guess = input("Quelle est votre réponse? ")
    if guess.lower() == reponse.lower():
        print("Bravo, vous avez deviné!")
    else:
        print("Désolé, la réponse était", reponse)
