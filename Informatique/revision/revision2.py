# Instructions composées ‹while> - cif> - celifs
print('Choisissez un nombre de 1 à 3 (ou 0 pour terminer) ', end='')
ch = input()
a = int(ch) # conversion de la chaine entrée en entier while a: #équivolent d : < while a 1= 0: >
while a:
    if a == 1:
        print("Vous avez choisi un :")
        print("le premier, l'unique, l'unité...")
    elif a == 2:
        print ("Vous préférez le deux :")
        print("La paire, le couple, le duo…")
    elif a == 3:
        print("Vous optez pour le plus grand des trois :")
        print("le trio, la trinité, le triplet ...")
    else:
        print("Un nombre entre UN et TROIS, s.v.p.")
    print('Choisissez un nombre de 1 à 3 (ou 0 pour terminer) ', end='')
    a = int(input())
print ("Vous avez entré zero :")
print ("L'exercice est donc terminé.")
