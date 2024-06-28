print ("****Bienvenue sur JUMIO S.A.R.L****")

price = input("Combien coute votre article ? : ")
while not price.isdigit():
    price = input("Combien coute votre article ? : ")

quantity = input("Combien d'articles aves vous pris ? : ")
while not quantity.isdigit():
    quantity = input("Combien d'articles aves vous pris ? : ")

montant_ht = int(price)*int(quantity)

tva = montant_ht*0.18

montant_ttc = montant_ht+tva

print( f""" 
    Votre facture: 
 P.U :  {price} CFA 
 Quantité : {quantity} 
 Montant HT :  {montant_ht} CFA 
 TVA :  {tva} CFA
 Montant TTC : {montant_ttc} CFA

 JUMIO vous remercie pour votre achat et vous souhaites de Joyeuses fetes !!!!!!! 
""" )