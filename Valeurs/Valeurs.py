liste = []
# J'ai commancer à faire la boucle while avec un booléen en True pour lui dire que c'est vrai
while True:
    # La valeur input permet de saisir une chaine de caractères
    valeur = input("Entrez une valeur (ou appuyez sur Entrée pour terminer) : ")

    # Je dit à if de prendre la valeur commme une chaine de caractères
    # IF c'est une condition
    if valeur == "":
        # Je lui dit d'arreter completement la boucle while avec break
        break
    # Les éléments peuvent être ajoutés à la liste en utilisant la fonction append()
    liste.append(valeur)
# Je lui est dit d'imprimer la liste finale
print("Liste finale :", liste)
