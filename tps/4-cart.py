#cart
# Initialisation de la variable choix
choix = ""

# Boucle while (tant que) :
while choix != "5":
    # Affichage du menu
    
    print("1. Ajouter un article dans le panier")
    print("2. Supprimer un article du panier")
    print("3. Afficher tous les articles")
    print("4. Vider le panier")
    print("5. Quitter")
    # Saisie du choix par l'utilisateur
    choix = input("Quel est votre choix? ")
    if choix.isdigit() :
        # Si le choix est 1
        if choix == "1":
            print("l'article a été bien ajouté dans votre panier")
        # Si le choix est 2
        elif choix == "2":
            print("l'article a été bien supprimé de votre panier")
        # Si le choix est 3
        elif choix == "3":
            print("voici la liste des articles du panier")
        
        # Si le choix est 4
        elif choix == "4":
            print("votre panier a bien été supprimé")
        # Si le choix est 5
        elif choix == "5":
            # Affichage d'un message de fin
            print("Merci pour votre visite!!!")
      # Sinon
    else:
        # Affichage d'un message d'erreur
        print("mauvaise entrée, veuillez entrer une valeur entre 1 et 5")