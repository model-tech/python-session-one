class Client:
    def __init__(self, code, nom, telephone, adresse, email):
        self.code = code
        self.nom = nom
        self.telephone = telephone
        self.adresse = adresse
        self.email = email
        self.solde = 0  # solde initial à zéro
        
    def afficher_infos(self):
        print(f"Code: {self.code}")
        print(f"Nom: {self.nom}")
        print(f"Téléphone: {self.telephone}")
        print(f"Adresse: {self.adresse}")
        print(f"Email: {self.email}")
        print(f"Solde: {self.solde}")

    def modifier_infos(self, nom=None, telephone=None, adresse=None, email=None):
        if nom:
            self.nom = nom
        if telephone:
            self.telephone = telephone
        if adresse:
            self.adresse = adresse
        if email:
            self.email = email

    def ajouter_solde(self, montant):
        self.solde += montant

    def retirer_solde(self, montant):
        if self.solde >= montant:
            self.solde -= montant
        else:
            print("Solde insuffisant.")

    def afficher_solde(self):
        print(f"Solde actuel du client {self.nom}: {self.solde}")

class Transaction:
    def __init__(self, ref_paiement, code_emetteur, code_recepteur, date_transaction, montant, canal):
        self.ref_paiement = ref_paiement
        self.code_emetteur = code_emetteur
        self.code_recepteur = code_recepteur
        self.date_transaction = date_transaction
        self.montant = montant
        self.canal = canal

def afficher_clients(customers):
    for client in customers:
        client.afficher_infos()
        print("--------------------")

def ajouter_client(customers):
    code = input("Code du client: ")
    nom = input("Nom du client: ")
    telephone = input("Téléphone du client: ")
    adresse = input("Adresse du client: ")
    email = input("Email du client: ")

    # Vérifier si le client existe déjà (par exemple, en vérifiant le code)
    # Ajouter le nouveau client à la liste
    customers.append(Client(code, nom, telephone, adresse, email))

def supprimer_client(customers, code_client):
    for client in customers:
        if client.code == code_client:
            customers.remove(client)
            print(f"Client avec code {code_client} supprimé.")
            return
    print(f"Client avec code {code_client} non trouvé.")

def modifier_infos_client(customers, code_client):
    for client in customers:
        if client.code == code_client:
            nom = input("Nouveau nom (Laissez vide pour ne pas modifier): ")
            telephone = input("Nouveau téléphone (Laissez vide pour ne pas modifier): ")
            adresse = input("Nouvelle adresse (Laissez vide pour ne pas modifier): ")
            email = input("Nouvel email (Laissez vide pour ne pas modifier): ")
            client.modifier_infos(nom, telephone, adresse, email)
            print("Informations mises à jour.")
            return
    print(f"Client avec code {code_client} non trouvé.")

def afficher_solde_client(customers, code_client):
    for client in customers:
        if client.code == code_client:
            client.afficher_solde()
            return
    print(f"Client avec code {code_client} non trouvé.")

def afficher_transactions(transactions):
    for transaction in transactions:
        print(f"Référence: {transaction.ref_paiement}")
        print(f"Émetteur: {transaction.code_emetteur}")
        print(f"Recepteur: {transaction.code_recepteur}")
        print(f"Date: {transaction.date_transaction}")
        print(f"Montant: {transaction.montant}")
        print(f"Canal: {transaction.canal}")
        print("--------------------")

def ajouter_transaction(transactions, customers):
    ref_paiement = input("Référence de paiement: ")
    code_emetteur = input("Code émetteur: ")
    code_recepteur = input("Code récepteur: ")
    date_transaction = input("Date de transaction: ")
    montant = float(input("Montant: "))
    canal = input("Canal de transaction: ")

    # Vérifier si les codes émetteur et récepteur existent
    emetteur_existe = False
    recepteur_existe = False
    for client in customers:
        if client.code == code_emetteur:
            emetteur_existe = True
        if client.code == code_recepteur:
            recepteur_existe = True
    
    if emetteur_existe and recepteur_existe:
        transactions.append(Transaction(ref_paiement, code_emetteur, code_recepteur, date_transaction, montant, canal))
        print("Transaction ajoutée.")
    else:
        print("Émetteur ou récepteur non trouvé.")

def modifier_solde_client(customers, code_client, montant):
    for client in customers:
        if client.code == code_client:
            client.ajouter_solde(montant)
            print(f"Solde du client {client.nom} mis à jour.")
            return
    print(f"Client avec code {code_client} non trouvé.")

def main():
    customers = []
    transactions = []

    while True:
        print("Menu Principal")
        print("1 - Gestion des clients")
        print("2 - Gestion des transactions")
        print("3 - Sortir")
        choix = input("Choix: ")

        if choix == "1":
            print("Menu Gestion des clients")
            print("1 - Afficher la liste des clients")
            print("2 - Ajouter un client")
            print("3 - Supprimer un client")
            print("4 - Modifier les informations d'un client")
            print("5 - Afficher le solde d'un client")
            sous_choix = input("Choix: ")

            if sous_choix == "1":
                afficher_clients(customers)
            elif sous_choix == "2":
                ajouter_client(customers)
            elif sous_choix == "3":
                code_client = input("Code du client à supprimer: ")
                supprimer_client(customers, code_client)
            elif sous_choix == "4":
                code_client = input("Code du client à modifier: ")
                modifier_infos_client(customers, code_client)
            elif sous_choix == "5":
                code_client = input("Code du client dont vous voulez afficher le solde: ")
                afficher_solde_client(customers, code_client)
            else:
                print("Choix invalide.")

        elif choix == "2":
            print("Menu Gestion des transactions")
            print("1 - Afficher toutes les transactions")
            print("2 - Ajouter une transaction")
            print("3 - Modifier le solde d'un client")
            sous_choix = input("Choix: ")

            if sous_choix == "1":
                afficher_transactions(transactions)
            elif sous_choix == "2":
                ajouter_transaction(transactions, customers)
            elif sous_choix == "3":
                code_client = input("Code du client à modifier le solde: ")
                montant = float(input("Montant à ajouter: "))
                modifier_solde_client(customers, code_client, montant)
            else:
                print("Choix invalide.")

        elif choix == "3":
            print("Merci, à bientôt!")
            break

        else:
            print("Choix invalide. Veuillez choisir à nouveau.")

if __name__ == "__main__":
    main()
