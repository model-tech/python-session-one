import random

print("***** Petit jeu permettant de deviner un nombre entre 1 et 100 en 5 essais *****")

the_number = random.randint(1,100)

for the_try in range(1,6):
    print(f"Essai n{the_try}")
    number = input("Entrer un entier entre 1 et 100: ")
    if int(number) == the_number :
        print("Vous avez trouvé! BRAVO!")
    
    elif int(number) < the_number:
        print("Très petit! choisir un autre plus grand")
    else:
        print("Très grand! choisir un autre plus petit")