print("**** Bienvenue sur JUMIO S.A.R.L ****")
try:
        prix_unitaire = float(input("Entrez le prix unitaire de l'article (en CFA) : "))
        quantite = int(input("Entrez la quantité achetée : "))

        montant_ht = prix_unitaire * quantite
        tva = 0.18 * montant_ht
        montant_ttc = montant_ht + tva

        print("\nVotre facture :")
        print(f"P.U : {prix_unitaire:.2f} CFA")
        print(f"Quantité : {quantite}")
        print(f"Montant HT : {montant_ht:.2f} CFA")
        print(f"TVA : {tva:.2f} CFA")
        print(f"Montant TTC : {montant_ttc:.2f} CFA")

        print("\nJUMIO vous remercie pour votre achat et vous souhaite de joyeuses fêtes!")
except ValueError:
        print("Veuillez entrer des valeurs numériques valides.")