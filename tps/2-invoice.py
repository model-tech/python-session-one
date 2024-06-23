#invoice
#Afficher message de Bienvenue 
print("****Bienvenue sur JUMIO S.A.R.L****")
#Demander à l'utilisateur d'entrer le prix de l'article
S = input("le prix de l'article s'il vous plait : ")
#Demander à l'utilisateur d'entrer le nombre d'article
T = input("le nombre d'article s'il vous plait : ")
#ici R représente le taux de la TVA
R = 0.18
#Verifier si s et T son numérique 
if S.isdigit() and T.isdigit() :
    #S et T sont numérique donc on va les transformer en entier 
    A = int(S)
    O = int(T)
    #afficher le prix unitaire 
    print(f"P.U : {A} CFA")
    #afficher la quantité
    print(f"Quantité : {O} ")
    #calculez le Montant HT
    E = A * O
    #Afficher le Montant HT
    print(f"Montant HT : {E} CFA")
    #Calculer ma TVA 
    L = R * E
    #afficher la TVA
    print(f"TVA : {L} CFA")
    #afficher le Montant TTC
    print(f"Montant TTC : {E + L} CFA")
    #afficher le commentaire 
    print("JUMIO vous Merci pour votre achat et vous souhaites de Joyeuses fetes !!!!!!!")
else :
    #Si S ou T n'est pas numérique 
    print("S ou T n'est pas numérique")
    