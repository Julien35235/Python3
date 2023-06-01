import random

# Générer un nombre aléatoire entre 0600000000 et 0699999999
secret_number = "0" + str(random.randint(600000000, 699999999))

# Devinez le numéro
guess = input("Je pense à un numéro de téléphone français à 10 chiffres. Devinez lequel : ")

# Vérifiez si la supposition est correcte
if guess == secret_number:
    print("Bravo, vous avez deviné le numéro de téléphone secret !")
else:
    print("Désolé, ce n'est pas le bon numéro. Le numéro de téléphone secret était", secret_number)
