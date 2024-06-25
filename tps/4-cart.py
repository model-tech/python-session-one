while True:
    print("""
    Choisissez parmi les 5 options suivantes: 

    1- Ajouter un article dans le panier
    2- Supprimer un article du panier
    3- Afficher tous les articles 
    4- Vider le panier
    5- Quitter""")

    choice= input("Quel est votre choix?:   ")

    while not (choice.isdigit() and int(choice) in range(1,6)):
        print("Erreur! Veuillez choisir parmis les optionsd disponibles")
        
    choice=int(choice)
    if choice==1:
        print("l'article a été bien ajouté dans votre panier")
    elif choice==2:
        print("l'article a été bien supprimé de votre panier")
        choice= input("Quel est votre choix?:   ")
    elif choice==3:
        print("voici la liste des articles du panier")
        choice= input("Quel est votre choix?:   ")
    elif choice==4:
        print("voici la liste des articles du panier")
        choice= input("Quel est votre choix?:   ")
    else: 
        print("Merci pour votre visite!!!")
        break
