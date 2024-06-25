print("*****Bienvenue sur JUMIO****")

price= input("Entrer le prix unitaire de votre article:    ")

qtity= input("Entrer la quantité achetée:    ")

while not (price.isdigit() and qtity.isdigit() and int(price)>0 and int(qtity)>0):
    print("Les valeurs entrées sont incorrectes.")
    price= input("Entrer le prix unitaire de votre article:    ")
    qtity= input("Entrer la quantité achetée:    ")

#conversion des variables en entier
price= int(price)
qtity= int(qtity)

#prix hors taxe

ht_price= price*qtity

#tva
rate=0.18
tva= price*rate

#prix ttc

total_price=ht_price + tva

#resultat à afficher

print(f"""
    Votre facture: 
    P.U :  {price} CFA 
    Quantité : {qtity} 
    Montant HT :  {ht_price} CFA 
    TVA :  {tva} CFA
    Montant TTC : {total_price} CFA

    JUMIO vous Merci pour votre achat et vous souhaites de Joyeuses fetes !!!!!!!""") 