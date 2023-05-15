import re

texte = "Voici quelques adresses email: john.doe@example.com, jane.doe@example.com"

adresses_email = re.findall(r'\S+@\S+', texte)

for adresse in adresses_email:
    print(adresse)
