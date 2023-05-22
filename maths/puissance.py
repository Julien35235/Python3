# By Julien Despagne

chiffre = int(input("Nombre: "))

puissance = 0

resultat = {
    'valeurs': [],
    'puissances': []
}

while chiffre:

    puissance += 1
    if 2 ** puissance > chiffre:
        previous = 2 ** (puissance - 1)
        resultat['puissances'].append(puissance)
        resultat['valeurs'].append(previous)
        chiffre -= previous
        puissance = 0

print(resultat)