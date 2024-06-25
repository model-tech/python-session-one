import random

number= random.randint(1,100)

print("***** Petit jeu permettant de deviner un nombre entre 1 et 100 en 5 essais *****")

for i in range (1,6):
    print(f"Essai no{i}:")
    x= input("Entrer un nombre entre 1 et 100:    ")
    while not (x.isdigit() and 1<=int(x)<=100):
        print("Valeur incorrecte, veuillez réessayer.")
        x= input("Entrer un nombre entre 1 et 100:    ")
    x=int(x)

    if x==number:
        print("Bravo!!! Vous avez gagné") 
        break
    elif x<number:
        print("Très petit! choisir un autre plus grand") 
    else:
        print("Très grand! choisir un autre plus grand")   
else: 
    print(f" Game over!!! 
    le nombre cherché était {number}")