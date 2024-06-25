import random

print("***** Petit jeu permettant de deviner un nombre entre 1 et 100 en 5 essais *****")
nombre_mystere = random.randint(1, 100)

for essai in range(1, 6):
    try:
        proposition = int(input(f"Essai no {essai}\nEntrer un entier entre 1 et 100 : "))
        if proposition < nombre_mystere:
            print("Très petit ! Choisissez un autre nombre plus grand.")
        elif proposition > nombre_mystere:
            print("Très grand ! Choisissez un autre nombre plus petit.")
        else:
            print("Bravo ! Vous avez trouvé le bon nombre !!!")
            break
    except ValueError:
            print("Veuillez entrer un nombre valide.")
else:
        print(f"Game over !!! Le nombre cherché était {nombre_mystere}")
