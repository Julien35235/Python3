def calculer_nombre_paiements(principal, taux_annuel, paiement_mensuel):
    """Calcule le nombre de paiements nécessaires pour rembourser un prêt."""
    taux_mensuel = taux_annuel / 100 / 12
    nombre_paiements = 0

    while principal > 0:
        principal += principal * taux_mensuel - paiement_mensuel
        nombre_paiements += 1

    return nombre_paiements


# Saisie des informations du prêt
principal = float(input("Montant du prêt : "))
taux_annuel = float(input("Taux d'intérêt annuel (%) : "))
paiement_mensuel = float(input("Montant du paiement mensuel : "))

# Calcul du nombre de paiements
nombre_paiements = calculer_nombre_paiements(principal, taux_annuel, paiement_mensuel)

# Affichage du résultat
print(f"Le nombre de paiements nécessaires pour rembourser le prêt est de : {nombre_paiements}")