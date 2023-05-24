# Fonction pour appeler les renforts des sapeurs-pompiers avec les différents véhicules
def appeler_renforts_sapeurs_pompiers():
    vehicules = [
        "Le véhicule de secours et d’assistance aux victimes (VSAV)",
        "Le véhicule secours routier (VSR)",
        "La grande échelle, ou échelle pivotante automatique (EPA)",
        "Bras (Mât) Elévateur Articulé (BEA (MEA)",
        "Le fourgon pompe-tonne (FPT)",
        "Le camion-citerne feux de forêts (CCF)",
        "Le véhicule poste de commandement (VPC)",
        "Bateau Léger de Sauvetage (BLS)",
        "Bateau de Reconnaissance et de Sauvetage (BRS)",
        "Camion Citerne Grande Capacité (CCGC)",
        "Cellule Mobile d'Intervention Chimique (CMIC)",
        "Fourgon Pompe Tonne / Camion Citerne Rural (FPT, CCR)",
        "Moto Pompe remorquable (MPR)",
        "Remorque Moto Ventilateur Grand Débit (RMVGD)",
        "Véhicule Léger de Commandement / Véhicule Léger Officier Permanence de Secteur (VLC / VLOPS)",
        "Véhicule d'Intervention en Milieux Périlleux (VIMP)",
        "Véhicule d'Intervention sur Risques Technologiques (VIRT)",
        "Véhicule de Liaison Hors-Route (VLHR)",
        "Véhicule Poste de Commandement / Poste de Commandement Mobile (VPC / PCM)",
        "Véhicule Porteur de Cellule (VPCE)",
        "Véhicule de Plongeurs (VPL)",
        "Véhicule de Secours Routier / Fourgon Pompe-Tonne Secours Routier (VSR / FPTSR)",
        "Véhicule de Soutien Sanitaire (VSS)",
        "Dragon",
    ]

    print("Appel en cours aux renforts des sapeurs-pompiers...")

    # Appel des renforts avec chaque véhicule
    for vehicule in vehicules:
        print("Appel des renforts avec :", vehicule)
        # Code pour appeler les renforts avec le véhicule correspondant
        # ...

    print("Les renforts des sapeurs-pompiers ont été appelés.")

# Fonction pour appeler les renforts du SMUR
def appeler_renforts_smur():
    print("Appel en cours aux renforts du SMUR...")

    # Code pour appeler les renforts du SMUR
    # ...

    print("Les renforts du SMUR ont été appelés.")

# Boucle principale
while True:
    choix = input("Qui voulez-vous appeler pour des renforts ? (sapeurs-pompiers / smur / quitter) ")

    if choix == "sapeurs-pompiers":
        appeler_renforts_sapeurs_pompiers()
    elif choix == "smur":
        appeler_renforts_smur()
    elif choix == "quitter":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")