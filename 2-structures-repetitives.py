# Affichage des 10 premiers nombres pairs avec une boucle for
print("Les 10 premiers nombres pairs :")
for i in range(2, 21, 2):  # commence à 2, termine à 20 (inclus), pas de 2 en 2
    print(i)

# Affichage des 10 premiers nombres impairs avec une boucle while
print("\nLes 10 premiers nombres impairs :")
count = 1
while count <= 20:
    print(count)
    count += 2
    if count > 20:
        break

