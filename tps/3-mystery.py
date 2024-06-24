#mystery
#on importe la fonction random qui permet de générer des nombres aléatoire
import random 
#on met la valeur entier choisie de façon aléatoire dans une variable
a = random.randint(1, 100)
#on initialise les variables
t = 0
n = 0
#on utilise le tant que pour répéter l'action puisque l'utilisateur a 5 chances
while n < 5 :
#on incrémente la variable n c'est la meme chose que n = n +1  
    n += 1
#ici déja le int veut dire directement que la valeur de t est un entier , je voulais pas utiliser isdigit 
    t = int(input("entrez un nombre entre 1 et 100 " ))
#ici on vérifie que la valeur entré est inférieur à notre valeur choisie aléatoirement
    if t < a : 
#ici il affiche le message car t < a
        print("Très petit! choisir un autre plus grand")
#ici on vérifie que la valeur entré est supérieur à notre valeur choisie aléatoirement
    elif t > a : 
#ici on affiche le message car t > a
        print("Très grand! choisir un autre plus petit")
#ici on vérifie que la valeur entré est égale à notre valeur choisie aléatoirement
    elif t == a :
#ici on affiche le message car t = a
        print("Bravo!!!! vous avez trouvé le bon nombre!!!")

"""ici nous sommes or de la boucle, c'est à dire que l'utilisateur a épuisé ses 5 chances
et n'a pas trouvé donc on affiche les 2 messages """
print("Game over!!!")  
print(f"le nombre cherché était {a}")         

        
