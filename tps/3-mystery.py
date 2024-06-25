import random

nombre_mystere = random.randint(1, 100)
essais_max = 5

print("Petit jeu permettant de deviner un nombre entre 1 et 100 en 5 essais")

for essai in range(1, essais_max + 1):
    print(f"\nEssai no {essai}")
    try :
        nombre_utilisateur = int(input("Entrer un entier entre 1 et 100:"))
        if 1 <= nombre_utilisateur <= 100:
            if nombre_utilisateur < nombre_mystere:
               print("Très petit! choisir un autre plus grand")
            elif nombre_utilisateur > nombre_mystere:
                 print("Très grand! choisir un autre plus petit")
            else:
                 print("Bravo!!!! vous avez trouvé le bon nombre!!!!")
                 break
        else:
            print("Veuillez entrer un nombre entre 1 et 100.")
    
    except ValueError:
        print("Veuillez entrer un nombre valide.")

else:
    print("\nGame over!!!")
    print(f"Le nombre cherché était {nombre_mystere}")