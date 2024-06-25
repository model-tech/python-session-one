x= input("Entrer un chiffre entre 2 et 9:    ")

while not (x.isdigit() and 2<=int(x)<=9):
    print("La valeur entrée est incorrecte. Veuillez réessayer")
    x= input("Entrer un chiffre entre 2 et 9:    ")

x= int(x)

print(f"Table de multiplication de {x}:")
for i in range(1,13):
    print(f"{x} x {i} = {x*i}")