chiffre = input("Veuillez svp entrer un chiffre entre 2 et 9 : ")

while not (chiffre.isdigit() and 2 <= int(chiffre) <= 9) :
    chiffre = input("Entrée invalide! Veuillez svp entrer un chiffre entre 2 et 9 : ")
else:
    for i in range(1,13):
        mutiply = chiffre*i
        print(f"{chiffre} * {i}  = {mutiply}")