# Fonction pour afficher le menu
def afficher_menu():
    print("\nMenu :")
    print("1. Ajouter un article")
    print("2. Supprimer un article")
    print("3. Afficher tous les articles du panier")
    print("4. Vider le panier")
    print("5. Quitter")

# Fonction pour ajouter un article dans le panier
def ajouter_article(panier):
    article = input("Entrez le nom de l'article à ajouter : ")
    prix = float(input("Entrez le prix de l'article : "))
    panier[article] = prix
    print(f"L'article '{article}' a été ajouté au panier.")

# Fonction pour supprimer un article du panier
def supprimer_article(panier):
    article = input("Entrez le nom de l'article à supprimer : ")
    if article in panier:
        del panier[article]
        print(f"L'article '{article}' a été supprimé du panier.")
    else:
        print(f"L'article '{article}' n'est pas dans le panier.")

# Fonction pour afficher tous les articles du panier
def afficher_panier(panier):
    if panier:
        print("\nArticles dans le panier :")
        for article, prix in panier.items():
            print(f"{article} - Prix : {prix}")
    else:
        print("\nLe panier est vide.")

# Fonction pour vider le panier
def vider_panier(panier):
    panier.clear()
    print("Le panier a été vidé.")

# Fonction principale du programme
def main():
    panier = {}

    while True:
        afficher_menu()
        choix = input("Entrez votre choix : ")

        if choix == '1':
            ajouter_article(panier)
        elif choix == '2':
            supprimer_article(panier)
        elif choix == '3':
            afficher_panier(panier)
        elif choix == '4':
            vider_panier(panier)
        elif choix == '5':
            print("Programme terminé.")
            break
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")

if __name__ == "__main__":
    main()
