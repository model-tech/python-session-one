#invoice
#Afficher message de Bienvenue 
print("****Bienvenue sur JUMIO S.A.R.L****")
#Demander à l'utilisateur d'entrer le prix de l'article
S = input("le prix de l'article s'il vous plait : ")
#Demander à l'utilisateur d'entrer le nombre d'article
T = input("le nombre d'article s'il vous plait : ")
#ici R représente le taux de la TVA
R = 0.18
#ici tant que s et t sont pas numérique on affiche les messages
while not (S.isdigit() and T.isdigit()) : 
    print("Entrez des valeurs numériques")
    S = input("le prix de l'article s'il vous plait : ")
    T = input("le nombre d'article s'il vous plait : ")
#S et T sont numérique donc on va les transformer en entier 
A = int(S)
O = int(T) 
#on va calculer le prix , la TVA et le prix totale 
price=A*O
tva=price*R
total_price=price+tva
#on affiche le message avec les différent calcule effectué en haut
print(f"""
P.U : {A} CFA
Quantité : {O}
Montant HT : {price} CFA
TVA : {tva} CFA
Montant TTC : {total_price} CFA
JUMIO vous Merci pour votre achat et vous souhaites de Joyeuses fetes !!!!!!!""")  

    