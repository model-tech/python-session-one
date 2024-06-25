print("***Bienvenu sur JUMIO S.A.R.L***")

prix_unit= int(input("Quel est le prix de l'article que vous souhaitez acheter ? "))
quantité= int(input("Quelle est la quantité d'articles acheté ? "))
montant_ht= prix_unit*quantité
tva= montant_ht*0.18
montant_ttc= montant_ht+tva
print(f""" Votre facture :
      P.U : {prix_unit}CFA
      Quantité: {quantité}CFA
      Montant HT: {montant_ht}CFA
      TVA: {tva}CFA
      Montant TTC: {montant_ttc}CFA
      
      JUMIO vous remercie pour votre achat et vous souhaite joyeuses fêtes!!!!!""")