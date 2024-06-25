while True:
    chiffre = input("Entrez un chiffre entre 2 et 9 : ")
    if chiffre.isdigit() and 2 <= int(chiffre) <= 9:
        break
    else:
        print("Vous devez entrer un chiffre entre 2 et 9.")
C = int(chiffre)
print("Table de multiplication de", C, ":")
for i in range(1, 11):
    print(f"{C} x {i} = {C * i}")
