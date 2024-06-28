print("****Bienvenue sur JUMIO S.A.R.L****")


TVA = 0.18

def calcul_montant_ht(price, qty):
    montant_ht = price * qty 
    return montant_ht

def calcul_montant_tva(mt_ht):
    montant_tva = mt_ht *  TVA
    return montant_tva

def calcul_montant_ttc(mt_ht, mt_tva): 
    montant_ttc = mt_ht + mt_tva
    return montant_ttc

def display_invoice(price, qty, montant_ht, montant_tva, montant_ttc):
    print(f"""
    Votre facture: 
        P.U :  {price} CFA 
        Quantité : {qty}
        Montant HT :  {montant_ht} CFA 
        TVA :  {montant_tva} CFA
        Montant TTC : {montant_ttc} CFA
    """)

def get_and_validate_price():
    # demander le prix de l'article 
    price_input = input("Entrez le prix de l'article: ")

    # je fais les vérifications 

    while not price_input.isdigit():
        print("Input error ! ❌❌❌, please number only")
        price_input = input("Entrez le prix de l'article: ")


    return int(price_input) 

def get_and_validate_qty():
    qty_input = input("Entrez la quantite d'article: ")

    # je fais les vérifications 

    while not qty_input.isdigit():
        print("Input error ! ❌❌❌, please number only")
        qty_input = input("Entrez la quantite d'article: ")

    return int(qty_input)



price = get_and_validate_price()
qty = get_and_validate_qty()

montant_ht = calcul_montant_ht(price, qty)
montant_tva = calcul_montant_tva(montant_ht)
montant_ttc = calcul_montant_ttc(montant_ht, montant_tva)

# Afficher les résultats 
display_invoice(price, qty, montant_ht, montant_tva, montant_ttc)

# Afficher le message de fin

print(" JUMIO vous Merci pour votre achat et vous souhaites de Joyeuses fetes !!!!!!!")