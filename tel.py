import phonenumbers

# Saisissez le numéro de téléphone à vérifier
numero_telephone = "+33612345678"

# Utilisez la fonction parse pour analyser le numéro de téléphone
numero = phonenumbers.parse(numero_telephone)

# Vérifiez si le numéro de téléphone est valide
if phonenumbers.is_valid_number(numero):
    print("Numéro de téléphone valide !")
else:
    print("Numéro de téléphone invalide.")

# Obtenez le pays d'origine du numéro de téléphone
pays = phonenumbers.region_code_for_number(numero)
print("Pays d'origine :", pays)
