# Afficher un message de bienvenue.
print("****Bienvenue sur JUMIO S.A.R.L****")
# Je demande à l'utilisateur d'entrer le prix unitaire de l'article.
prix_unitaire = float(input("Entrez le prix unitaire de l'article en CFA : "))
# Je demander à l'utilisateur d'entrer la quantité achetée.
quantite = int(input("Entrez la quantité achetée : "))
# Je calcule le montant HT en multipliant le prix unitaire par la quantité.
montant_ht = prix_unitaire * quantite
# Je calcule la TVA sur le montant HT (supposant un taux de TVA de 18%)
tva = 0.18 * montant_ht
# Je calcule le montant TTC (Toutes Taxes Comprises) en ajoutant la TVA au montant HT.
montant_ttc = montant_ht + tva
# Afficher la facture avec les détails
print("Votre facture :")
print(f"P.U :  {prix_unitaire} CFA")
print(f"Quantité : {quantite}")
print(f"Montant HT : {montant_ht} CFA")
print(f"TVA : {tva} CFA")
print(f"Montant TTC : {montant_ttc} CFA")

# Message de remerciement
print("JUMIO vous remercie pour votre achat et vous souhaite de Joyeuses fêtes !!!!!!!")