#on va générer des nombres aléatoire grâce à la fonction random#
import random
#on va définir une fonction pour mettre en place notre jeu de hasard#
def jeu_devinette():
    print("***** Petit jeu permettant de deviner un nombre entre 1 et 100 en 5 essais *****")
    nombre_mystere = random.randint(1, 100)
    essais = 5
    
    for i in range(1, essais + 1):
        print(f"Essai no {i}")
        try:
            devine = int(input("Entrer un entier entre 1 et 100: "))
            
            if devine < 1 or devine > 100:
                print("S'il vous plaît, entrer un entier entre 1 et 100.")
                continue
            
            if devine == nombre_mystere:
                print("Bravo!!!! vous avez trouvé le bon nombre!!!")
                return
            elif devine < nombre_mystere:
                print("Très petit! choisir un autre plus grand")
            else:
                print("Très grand! choisir un autre plus petit")
        
        except ValueError:
            print("Entrée invalide. S'il vous plaît, entrer un entier.")
    
    print("Game over!!!")
    print(f"Le nombre cherché était {nombre_mystere}")

# Exécution du jeu#
jeu_devinette()
print("fin du jeu")






