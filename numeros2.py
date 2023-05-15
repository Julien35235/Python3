telephone = ""
while len(telephone) != 10:  # tant que le numéro n'a pas 10 chiffres
    telephone = input("Composez votre numéro de téléphone (10 chiffres) : ")
    if len(telephone) != 10:
        print("Le numéro doit avoir 10 chiffres. Veuillez réessayer.")
print("Votre numéro de téléphone est : ", telephone)
