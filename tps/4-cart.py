#Tant que les élémens écrits sont vrais, les étapes se déroulent

while True:
    print("""
    Choisissez parmi les 5 options suivantes: 

    1- Ajouter un article dans le panier
    2- Supprimer un article du panier
    3- Afficher tous les articles 
    4- Vider le panier
    5- Quitter""")

    choice= input("Quel est votre choix?:   ")

    #on vérifie que la valeur entrée est effectivement un nombre et est compris entre 1 et 5.
    #si ce n'est pas respecté, on lui reaffice le menu et la question

    while not (choice.isdigit() and int(choice) in range(1,6)):
        print("Erreur dans le choix !")
        print("""
        Choisissez parmi les 5 options suivantes: 

        1- Ajouter un article dans le panier
        2- Supprimer un article du panier
        3- Afficher tous les articles 
        4- Vider le panier
        5- Quitter""")

        choice= input("Quel est votre choix?:   ")


    #si la valeur entrée respecte les conditions ci-dessus, on convertit en entier

    choice=int(choice)

    #pour chaque entier choisi, on affiche le message

    if choice==1:
        print("l'article a été bien ajouté dans votre panier")
    elif choice==2:
        print("l'article a été bien supprimé de votre panier")
    elif choice==3:
        print("voici la liste des articles du panier")
    elif choice==4:
        print("voici la liste des articles du panier")
    else: 
        print("Merci pour votre visite!!!")
        break

