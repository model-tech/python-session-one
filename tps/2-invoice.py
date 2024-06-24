### La résolution de cet exercice nous amenera à produire un programme
# Le programme nous demandera le montant de l'achat et la quantité acheté 
# Après avoir entré les informations necessaire le programme exécutura le 
# calcul et nous verrons apparaitre le montant ht la quantité la tva 
# et le montant ttc .###

 
prix_achat = input("Veuillez entrer le prix d'achat:") 
quantite_acheté = input("Veuillez entrer la quantité acheté :") 
tva = 0.18
print("*****Bienvenue sur JUMIO S.A.R.L*****")

if prix_achat.isdigit() and quantite_acheté.isdigit():
    p = int(prix_achat) 
    q = int(quantite_acheté) 
    print("Votre facture :")
    print(f"P.U : {p}CFA") 
    print(f"Quantité : {q}") 
    montant_ht = p * q
    print(f"Montant HT : {montant_ht} CFA") 
    montant_tva = montant_ht * tva 
    print(f"TVA : {montant_tva} CFA") 
    montant_ttc = montant_ht + montant_tva 
    print(f"Montant TTC : {montant_ht + montant_tva}CFA")
    print("JUMIO vous remercie pour votre achat et vous souhaites de Joyeuses fête !!!!") 
else : 
     print(" Veuillez entrer une valeur numérique ")

   