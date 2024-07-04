import random

print("***** Petit jeu permettant de deviner un nombre entre 1 et 100 en 5 essais *****")

the_number = random.randint(1,100)
the_try = range(1,6)

for i in the_try:
    print(f"Essai n°{i}")
    number = input("Entrer un entier entre 1 et 100: ")
    while not (number.isdigit() and 1 <= int(number) <= 100):
        print(f"Essai n°{i}")
        number = input("Entrer un entier entre 1 et 100: ")
    else:
        if 1<=i<5:
            if int(number) == the_number :
                print("Vous avez trouvé! BRAVO!")
                break

            elif int(number) < the_number:
                print("Très petit! choisir un autre plus grand")
            else:
                print("Très grand! choisir un autre plus petit")

        else:
            if int(number) == the_number :
                print("Vous avez trouvé! BRAVO!")
                break
            else:
                print(f""" 
                    Game over!!! 

                    le nombre cherché était {the_number}
                        """)


