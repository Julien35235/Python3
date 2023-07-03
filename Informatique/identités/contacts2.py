contacts = [
    {
        "nom": "Julien Despagne ",
        "telephone": "06437899658",
        "email": "julien@despagne.com"
    },
    {
        "nom": "Jane Smith",
        "telephone": "9876543210",
        "email": "jane.smith@example.com"
    },
    {
        "nom": "Alice Johnson",
        "telephone": "5555555555",
        "email": "alice.johnson@example.com"
    }
]

quitter = False
while not quitter:
    for contact in contacts:
        print("Nom: " + contact["nom"])
        print("Téléphone: " + contact["telephone"])
        print("Email: " + contact["email"])
        print("-------------------")

    reponse = input("Voulez-vous continuer à afficher les contacts ? (Oui/Non): ")
    if reponse.lower() != "oui":
        quitter = True
