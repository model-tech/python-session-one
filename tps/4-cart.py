while True:
    print("""
    Choisissez parmi les 5 options suivantes: 

    1- Ajouter un article dans le panier
    2- Supprimer un article du panier
    3- Afficher tous les articles 
    4- Vider le panier3
    5- Quitter
    """)

    choice = input("Quel est votre choix ? ")

    while not choice.isdigit() or int(choice) not in range(1, 6):
        print("Mauvaise entrée, veuillez entrer une valeur entre 1 et 5.")
        choice = input("Quel est votre choix ? ")

    onechoice = int(choice)

    if onechoice == 1:
        print("** L'article a été bien ajouté dans votre panier **")

    elif onechoice == 2:
        print("** L'article a été bien supprimé de votre panier **")

    elif onechoice == 3:
        print("** Voici la liste des articles du panier **")

    elif onechoice == 4:
        print("** Votre panier a bien été supprimé **")

    elif onechoice == 5:
        print("** Merci pour votre visite!!! **")
        break  