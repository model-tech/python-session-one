#Afficher message du debut
print('****Bienvenue sur JUMIO S.A.R.L****')
 #demandera la prix de l'article et la quantité acheté
price=int(input("Entrez le prix de l'article:  "))
qte=int(input("Quel quantité achetez vous:  "))

#Calcul du montant HT , TVA, Montant TTC

montantHT= price * qte
tva= montantHT*0.18
montantTTC=montantHT+ tva

print(f"""Votre facture: 
P.U :  {price} CFA 
 Quantité : {qte}
 Montant HT :  {montantHT} CFA 
 TVA :  {tva} CFA
 Montant TTC : {montantTTC} CFA

 JUMIO vous Merci pour votre achat et vous souhaites de Joyeuses fetes !!!!!!! """)