print("Devinez une chaîne de télévision jusqu'à RMC Sport !")
devinette = input("Quelle est votre réponse ? ")

while devinette != "RMC Sport":
    print("Ce n'est pas la bonne réponse. Essayez encore !")
    devinette = input("Quelle est votre réponse ? ")

print("Félicitations ! Vous avez deviné la chaîne de télévision RMC Sport !")
