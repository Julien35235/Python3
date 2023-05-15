import re

texte = "Voici quelques adresses email: julien@despagne.com, julien.despagne@icloud.com, jdespagne18@gmail.com, julien.despagne@institutsolacroup.com"

adresses_email = []
i = 0

while i < len(texte):
    match = re.search(r'\S+@\S+', texte[i:])
    if match:
        adresses_email.append(match.group())
        i += match.end()
    else:
        break

for adresse in adresses_email:
    print(adresse)
