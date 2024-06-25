#demander à l'utilisateur d'entrer un nombre 
x= input("Entrer un chiffre entre 2 et 9:    ")

#vérification que la valeur entrée est un nombre et est compris entre 2 et 9
while not (x.isdigit() and 2<=int(x)<=9):
    print("La valeur entrée est incorrecte. Veuillez réessayer")
    x= input("Entrer un chiffre entre 2 et 9:    ")

#après vérification on va convertir la valeur en entier
x= int(x)

#affichage de la table de multiplication
print(f"Table de multiplication de {x}:")
for i in range(1,13):
    print(f"{x} x {i} = {x*i}")