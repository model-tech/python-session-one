def afficher_menu():
    print("Choisissez parmi les 5 options suivantes:")
    print("1- Ajouter un article dans le panier")
    print("2- Supprimer un article du panier")
    print("3- Afficher tous les articles")
    print("4- Vider le panier")
    print("5- Quitter")

def ajouter_article(panier):
    nom_article = input("Entrez le nom de l'article à ajouter : ")
    prix_article = float(input("Entrez le prix de l'article : "))
    article = {'name': nom_article, 'price': prix_article}
    panier.append(article)
    print(f"L'article '{nom_article}' a été ajouté au panier.")

def supprimer_article(panier):
    nom_article = input("Entrez le nom de l'article à supprimer : ")
    article_trouve = False
    for article in panier[:]:  # parcourt une copie de la liste pour pouvoir supprimer en cours de parcours
        if article['name'] == nom_article:
            panier.remove(article)
            print(f"L'article '{nom_article}' a été supprimé du panier.")
            article_trouve = True
    if not article_trouve:
        print("Aucun article avec ce nom dans le panier.")

def afficher_articles(panier):
    if not panier:
        print("Le panier est vide.")
    else:
        print("Contenu du panier :")
        for idx, article in enumerate(panier, 1):
            print(f"{idx}. {article['name']} - Prix : {article['price']} XOF")

def vider_panier(panier):
    panier.clear()
    print("Le panier a été vidé.")

# Programme principal
panier = []

while True:
    afficher_menu()
    choix = input("Quel est votre choix? ")

    if choix == '1':
        ajouter_article(panier)
    elif choix == '2':
        supprimer_article(panier)
    elif choix == '3':
        afficher_articles(panier)
    elif choix == '4':
        vider_panier(panier)
    elif choix == '5':
        print("Fin du programme.")
        break
    else:
        print("Choix invalide. Veuillez entrer un chiffre de 1 à 5.")
