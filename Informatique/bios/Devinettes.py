print("Devinez le nom du programme de démarrage utilisé par les ordinateurs modernes.")
print("Indice : Il remplace progressivement le BIOS et offre une interface plus moderne.")

reponse = input("Votre réponse : ")
while reponse.lower() not in ["uefi", "efi"]:
    print("Ce n'est pas la bonne réponse. Réessayez !")
    reponse = input("Votre réponse : ")

print("Félicitations ! Vous avez trouvé la bonne réponse : UEFI.")
