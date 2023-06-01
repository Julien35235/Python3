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

index = 0
while index < len(contacts):
    contact = contacts[index]
    print("Nom: " + contact["nom"])
    print("Téléphone: " + contact["telephone"])
    print("Email: " + contact["email"])
    print("-------------------")
    index += 1
