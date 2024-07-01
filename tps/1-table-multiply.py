a=input("entrez un chiffre entre 2 et 9 ")
while not (a.isdigit() and 2<=int(a)<=9) :
    print("erreur")
    a=input("entrez un chiffre entre 2 et 9 ")
b=int(a)
for i in range(1,13) :
    print(f"{b}*{i}={b*i}")