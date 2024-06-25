#afficher le message de bienvenue 
print("*****Bienvenue sur JUMIO****")

#demander à l'utilisateur d'entrer le prix unitaire de son article 

price= input("Entrer le prix unitaire de votre article:    ")

#demander à l'utilisateur d'entrer la quantité achetée unitaire de son article 

qtity= input("Entrer la quantité achetée:    ")

#vérification que les valeurs entrées sont des nombres et sont positifs

while not (price.isdigit() and qtity.isdigit() and int(price)>0 and int(qtity)>0):
    print("Les valeurs entrées sont incorrectes.")
    price= input("Entrer le prix unitaire de votre article:    ")
    qtity= input("Entrer la quantité achetée:    ")

#conversion des variables en entier
price= int(price)
qtity= int(qtity)

#calcul du prix hors taxe

ht_price= price*qtity

#montant de la tva
rate=0.18
tva= price*rate

#calcul du prix ttc

total_price=ht_price + tva

#affichage de la facture

print(f"""
    Votre facture: 
    P.U :  {price} CFA 
    Quantité : {qtity} 
    Montant HT :  {ht_price} CFA 
    TVA :  {tva} CFA
    Montant TTC : {total_price} CFA

    JUMIO vous Merci pour votre achat et vous souhaites de Joyeuses fetes !!!!!!!""") 