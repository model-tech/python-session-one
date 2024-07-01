a=print("Bienvenue sur JUMIO S.A.R.L")
prix_unitaire=float(input("entrez le  prix unitaire"))
quantite=float(input("entrez la quantite"))
prix_ht=prix_unitaire*quantite
prix_tva=prix_ht*0.18
prix_ttc=prix_ht+prix_tva
print("\nVOTRE FACTURE")
print(f"p.u :{prix_unitaire:} CFA")
print(f"quantite :{quantite:}")
print(f"montant HT est:{prix_ht}  CFA")
print(f"TVA est:{prix_tva} CFA")
print(f"montant TTC est:{prix_ttc} CFA") 
print("JUMIO vous remercie pour votre achat et vous souhaite de joyeuses fetes!")
