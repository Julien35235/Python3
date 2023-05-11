import random

special_chars = "@#&é\"'(§è!çà)°-¨^*$%ù`£+=/:.;?,>"

length = 10000  # longueur de la chaîne de caractères spéciaux

result = ""  # chaîne de caractères spéciaux générée

while len(result) < length:
    result += random.choice(special_chars)

print(result)
