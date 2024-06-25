#Le nombre aléatoire
import random 


nombre=random.randint(1,100)


for i in range(1,6):
    print(f"Essai no {i}")
    devine= int(input("Entrer un entier entre 1 et 100: "))
    if devine < nombre:
        print("Très petit! choisir un autre plus grand")

    elif devine >nombre:
        print("Très grand! choisir un autre plus grand")
    else :
        print("Bravo!!!! vous avez trouvé le bon nombre!!!")
        break

