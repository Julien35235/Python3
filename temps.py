# Le nombre de secondes est fourni au départ
nsd = 123456789

# Nombre de secondes dans une jounée, en une minute, il y a 60 secondes, 
# et en une heure, il y a 60 minutes.
# Donc, en une heure, il y a 60 x 60 = 3600 secondes. En une journée, 
# il y a 24 heures,
# il y a donc 24 x 3600 = 86 400 secondes en une journée
nspj = 3600 * 24

# Nombre de secondes dans un an
nspa = nspj * 365

# Nombre de secondes dans un mois 
# (en admettant pour chaque mois une durée identique de 30 jours)
nspm = nspj * 30

# Nombre d'années contenues dans la durée fournie
na = nsd // nspa  # division entière
nsr = nsd % nspa  # n. de sec. restante

# Nombre de mois restants
nmo = nsr // nspm  # division entière
nsr = nsr % nspm  # n. de sec restants

# Nombre de jours restants
nj = nsr // nspj  # division entière
nsr = nsr % nspj  # n. de sec. restants

# Nombre d'heures restantes
nh = nsr // 3600  # division entière
nsr = nsr % 3600  # n. nombre de sec. restants

# Nombre de minutes restants
nmi = nsr // 60  # division entière
nsr = nsr % 60  # n. sec. restants

print("Nombre de secondes à convertir :", nsd)
print("Cette durée correspond à", na, "années de 365 jours plus")
print(nmo, "mois de 30 jours", end=' ')
print(nh, "heures", end=' ')
print(nmi, "minutes et", end=' ')
print(nsr, "secondes.")
 
