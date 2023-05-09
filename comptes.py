#Creation d'un compte bancaire

from CBancaire import CBancaire
def traiterCompte(cb):
    mt = float(input("Votre montant (0==fin)? "))
while (mt != 0.0):
    if (mt > 0.0):
        cb.crediter(mt)
else:
    cb.debiter(-mt)
print("Etat du compte: ", cb.getSolde(), " euros", sep="")
if (cb.getSolde() < 0.0):
    print("OUPS... cb en negatif -- veuillez alimenter")
mt = float(input("Votre montant (0==fin)? "))