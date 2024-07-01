#afficher au début: Bienvenue sur JUMIO S.A.R.L#
print ("Bienvenue sur JUMIO S.A.R.L")
#  demandera le prix de l'article et la quantité acheté#
prix_unitaire = float(input("entrez le prix unitaire de l'article en (cfa):"))
quantite = int(input("Entrez la quantité achetée : "))
#calculs#
montant_ht = prix_unitaire * quantite
tva = montant_ht * 0.18
montant_ttc = montant_ht + tva
#afficher la facture#
print("\nVotre facture :")
print(f"P.U : {prix_unitaire} CFA")
print(f"Quantité : {quantite}")
print(f"Montant HT : {montant_ht} CFA")
print(f"TVA : {tva} CFA")
print(f"Montant TTC : {montant_ttc} CFA")
print("JUMIO vous remercie pour votre achat et vous souhaite de Joyeuses fêtes !!!!!")







 