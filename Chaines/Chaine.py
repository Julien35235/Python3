#By Julien Despagne
#Écrivez un script qui détermine si une chaîne contient ou non le caractère « e ».

#Écrivez un script qui compte le nombre d’occurrences du caractère « e » dans une chaîne.

#Écrivez un script qui recopie une chaîne (dans une nouvelle variable), en insérant des astérisques entre les caractères.
#Ainsi par exemple, « gaston » devra devenir « g*a*s*t*o*n »


#Écrivez un script qui recopie une chaîne (dans une nouvelle variable) en l’inversant
#Ainsi par exemple, « zorglub » deviendra « bulgroz ».



#En partant de l’exercice précédent, écrivez un script qui détermine si une chaîne de caractères donnée est un palindrome (c’est-à-dire une chaîne qui peut se lire indifféremment dans les deux sens), comme par exemple « radar » ou « s.o.s ».


#Creations des chaines de caractere qui composee des sequnces diffrences avec un string
chaine = "Bonjour le monde"
#La condition prend e avec une chaine de caractere
#Elle permet d'executer une série d instructions si jamais une condition est ralisee.
if 'e' in chaine:
#Imprimmer une chaine de caractere
    print("La chaîne contient le caractere 'e'")
#C est un booleen entre ses parentheses
#Un else (qui se traduit par sinon) à la suite de ce if, les instructions entre ses accolades sont exécutées.
else:
#Imprimmer une chaine qui ne contient pas de caractere
    print("La chaîne ne contient pas le caractere 'e'")

#Creations des chaines de caractere qui composee des sequnces diffrences avec un string
    chaine = "Bonjour le monde"
    nb_e = chaine.count('e')
#Imprimmer une seule fois le caractere.
#Dans la chaîne de caracteres les accolades sont vides {} précisent  a l'endroit ou le contenu de la variable doit etre insére
    print("La chaîne contient {} fois le caractere 'e'".format(nb_e))

#Creations des chaines de caractere qui composee des sequnces diffrences avec un string de gaston
    chaine = "gaston"
#nouvelle_chaine de cractere va prendre un astérisque au niveau de la multiplication
    nouvelle_chaine = '*'.join(chaine)
#Imprimmer la nouvelle chaine
    print(nouvelle_chaine)

#Creations des chaines de caractere qui composee des sequnces diffrences avec un string de zorglub
chaine = "zorglub"
nouvelle_chaine = chaine[::-1]
#Imprimmer la nouvelle chaine
print(nouvelle_chaine)

#Creations des chaines de caractere qui composee des sequnces diffrences avec un string de radar
chaine = "radar"
i = 0
j = len(chaine) - 1
#Je vais commencer a faire la boule while
#Si while est < j il va prendre le if pour la condition de chaine
while i < j:
    if chaine[i] != chaine[j]:
#Imprimmer la chaine n est pas un palindrome
        print("La chaine n est pas un palindrome")
#Je vais completement arreter la boucle while avec une condition externe
        break
#incrementations de 1
    i += 1
#diminusions de 1
    j -= 1

#C est un booleen entre ses parentheses
else:
#Imprimmer la chaine est un palindrome
    print("La chaine est un palindrome")
