# Définir la variable de départ
letter = 'a'

# Définir la limite de boucle
while letter <= 'z':
    # Afficher la lettre actuelle
    print(letter)
    # Passer à la lettre suivante
    letter = chr(ord(letter) + 1)
