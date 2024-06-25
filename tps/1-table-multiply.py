#Le user entre une valeur 
valeur=input("entrer un chiffre entre 2 et 9: ")

while not valeur.isdigit() and valeur not in  range(2,10):
    valeur=input("entrer un chiffre entre 2 et 9: ")
for i in range(2,10):
    multiplicateur= range(1,13)
    for m in multiplicateur:
        result=int(valeur)*m
        print(f"{valeur}* {m}={result}")

