# Je demande à l'utilisateur d'entrer un chiffre
chiffre = input("entrer un chiffre entre 2 et 9 ")
# Je vérifie que la valeur entree est un chiffre
if (chiffre.isdigit()):
    chiffre = int(chiffre)
    if (chiffre >= 2) and (chiffre <= 9):
        for i in range(1, 13):
            print(f"{chiffre} x {i} = {chiffre * i}")
    else :
        print("entrer un chiffre entre 2 et 9")
else :
    print("veuillez entrer un chiffre")        
# si c'est un chiffre je verifie que c'est ente 2 et 9

# Sinon j'affiche le message "entre un chiffre entre 2 et 9"

