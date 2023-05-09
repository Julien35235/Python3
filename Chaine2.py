# Ecrire un script qui recopie une chaine (dans une nouvelle variable) en inversion d'une chaine de caractères.
#Chaine fournie au départ
#C'est la correction
ch =  'julien'
# Nombre de caractère total
lc = len(ch)


#Le traitement commence à partir du dernier caractère
i = lc - 1
#Nouvelle chaine à construire (vide au départ)
nch = ""
while i > 0:
    nch =  nch + ch[i]
    i = i - 1
#Affichage
print(nch)
