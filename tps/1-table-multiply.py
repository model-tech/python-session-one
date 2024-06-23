while True:
        nombre = int(input("Entrez un chiffre entre 2 et 9 : "))
        if nombre in range(2,10):
            break
        else:
            print("Veuillez entrer un chiffre entre 2 et 9.")
print("Voici la table de multiplication de,", nombre,":")
for i in range(1, 11):
    produit = nombre * i
    print(f"{nombre} x {i} = {produit}")
