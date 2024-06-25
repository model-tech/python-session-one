# Initialisation du panier vide
panier = []

while True:
    # Affichage du menu
    print("\nChoisissez parmi les 5 options suivantes :")
    print("1- Ajouter un article dans le panier")
    print("2- Supprimer un article du panier")
    print("3- Afficher tous les articles du panier")
    print("4- Vider le panier")
    print("5- Quitter")

    # Demande à l'utilisateur de faire un choix
    choix = input("Quel est votre choix? ")

    if choix.isdigit():
        choix = int(choix)
        if 1 <= choix <= 5:
            if choix == 1:
                # Ajout d'un article dans le panier
                article = input("Entrez le nom de l'article à ajouter : ")
                panier.append(article)
                print(f"L'article '{article}' a été ajouté dans votre panier.")
            elif choix == 2:
                # Suppression d'un article du panier
                article = input("Entrez le nom de l'article à supprimer : ")
                if article in panier:
                    panier.remove(article)
                    print(f"L'article '{article}' a été supprimé de votre panier.")
                else:
                    print(f"L'article '{article}' n'est pas dans votre panier.")
            elif choix == 3:
                # Affichage de tous les articles du panier
                print("Voici la liste des articles dans votre panier :")
                for item in panier:
                    print(item)
            elif choix == 4:
                # Vidage du panier
                panier.clear()
                print("Votre panier a bien été vidé.")
            elif choix == 5:
                # Quitter le programme
                print("Merci pour votre visite !!!")
                break
        else:
            print("Mauvaise entrée. Veuillez choisir une valeur entre 1 et 5.")
    else:
        print("Mauvaise entrée. Veuillez entrer un nombre entre 1 et 5.")
