
class Invoice:

    def __init__(self, p_price, p_qty):
        self.price = p_price
        self.qty = p_qty

    def montant_ht(self):
        result = self.price * self.qty 
        return result
    
    def montant_tva(self,  tax_rate):
        result = self.price * self.qty * tax_rate
        return result
    
    def montant_ttc(self, mt_ht, mt_tva):
        result = mt_ht + mt_tva
        return result
    

    def display_invoice(self):
        ht = self.montant_ht()
        tva = self.montant_tva(0.18)
        print(f"""
    Votre facture: 
        P.U :  {self.price} CFA 
        Quantité : {self.qty}
        Montant HT :  {ht} CFA 
        TVA :  {tva} CFA
        Montant TTC : {self.montant_ttc(ht, tva)} CFA
    """)
        

    @staticmethod
    def get_and_validate_price():
        # demander le prix de l'article 
        price_input = input("Entrez le prix de l'article: ")

        # je fais les vérifications 

        while not price_input.isdigit():
            print("Input error ! ❌❌❌, please number only")
            price_input = input("Entrez le prix de l'article: ")


        return int(price_input) 
    
    @staticmethod
    def get_and_validate_qty():
        qty_input = input("Entrez la quantite d'article: ")

        # je fais les vérifications 

        while not qty_input.isdigit():
            print("Input error ! ❌❌❌, please number only")
            qty_input = input("Entrez la quantite d'article: ")

        return int(qty_input)








 

price = Invoice.get_and_validate_price()
qty = Invoice.get_and_validate_qty()

my_invoice = Invoice(price, qty)

my_invoice.display_invoice()