import random
print("Petit jeu permettant de deviner un nombre entre 1 et 100 en 5 essais")
a=random.randint(1,100)
i=0
while i<5:
    #print(a)
    b=input("entrez un chiffre entre 1 et 100: ")
    c=int(b)
    if c<a :
        print("tres petit! choisir un autre")
    elif c>a :
        print("tres grand! choisir un plus petit")
    elif c==a :
        print("bravooo!")
        break

    i = i+1
else :
    print("Game over")
    print(f"le nombre chercher est: {a}")

