#générer un nombre au hasard
import random

number= random.randint(1,100)

print("***** Petit jeu permettant de deviner un nombre entre 1 et 100 en 5 essais *****")

#Pour le nombre i d'essai,

for i in range (1,6):
    print(f"Essai no{i}:")

    #on demande à l'utilisateur d'entrer un nombre
    
    x= input("Entrer un nombre entre 1 et 100:    ")

    #on vérifie que la valeur entrée est effectivement un nombre et est compris entre 1 et 100
    
    while not (x.isdigit() and 1<=int(x)<=100):
        print("Valeur incorrecte, veuillez réessayer.")
        x= input("Entrer un nombre entre 1 et 100:    ")

    #si la valeur entrée respecte les conditions ci-dessus, on convertit en entier
    
    x=int(x)

    # on compare le nombre entré à celui qui a été généré pour voir si l'utilisateur a trouvé
    
    if x==number:
        print("Bravo!!! Vous avez gagné") 
        break
    elif x<number:
        print("Très petit! choisir un autre plus grand") 
    else:
        print("Très grand! choisir un autre plus grand")   

#après 5 essais, s'il n'a pas trouvé, on affiche le resultat

else: 
    print(f""" Game over!!! 
    le nombre cherché était {number}""")