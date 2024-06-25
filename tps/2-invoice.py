### Pour résoudre cet exercice, nous aurons à concevoir un programme
# Ce programme nous présentera le prix d'achat et la quantité achetée
# Une fois que nous renseignions les informations sollicitées, le programme fera le calcul et il fera appaître
# le monatant HT, la quantité achetée, la TVA et le montant TTC .###


prix_achat = input("Veuillez entrer le prix d'achat:")
quantité_acheté = input("Veuillez entrer la quantité acheté:")
tva=0.18
print("*****Bienvenue sur JUMIO S.A.R.L")
if prix_achat.isdigit() and quantité_acheté.isdigit():
    p = int(prix_achat)
    q = int(quantité_acheté)
    print("Votre facture :")
    print(f"P.U {p}CFA")
    print(f"Quantité : {q}")
    montant_ht = p * q
    print(f"Montant HT :{montant_ht} CFA")
    montant_tva = montant_ht * tva
    print(f"TVA :{montant_tva} CFA")
    montant_ttc = montant_ht + montant_ht + montant_tva
    print(f"montant TTC :{montant_ht + montant_tva}CFA")
    print("JUMIO vous remercie pour votre achat et vous souhaites de Joyeuses !!!!!")
else :
    print(" Veuillez entrer une valeur numérique ")
