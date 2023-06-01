print("Devinez quel événement maritime célèbre je suis!")
print("Je suis une course de voile en solitaire qui se déroule tous les quatre ans.")
print("Les participants naviguent autour du monde sur des voiliers.")
print("Je suis connu pour ma difficulté et ma renommée internationale.")

reponse = input("Votre réponse : ")
while reponse.lower() != "vendée globe":
    print("Ce n'est pas la bonne réponse. Essayez encore!")
    reponse = input("Votre réponse : ")

print("Bravo, vous avez deviné! Je suis le Vendée Globe!")
