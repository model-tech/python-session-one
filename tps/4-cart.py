while True :
    print("""
    1. Ajouter un article dans le panier
    2. Supprimer un article du panier
    3. Afficher tous les articles
    4. Vider le panier
    5. Quitter """)
    sc = input("Quel est votre choix? ")
#tant que sc n'est pas numérique et l'entier de sc n'est entre 1 et 5
#il affiche le message d'erreur et le menu
    while not (sc.isdigit() and int(sc) in range(1,6)) : 
        print("erreur, entrez un nombre entre 1 et 5")
        
        print(f"""
        1. Ajouter un article dans le panier
        2. Supprimer un article du panier
        3. Afficher tous les articles
        4. Vider le panier
        5. Quitter  """)
        sc = input("Quel est votre choix?" )
      #si le choix est 1  
    if sc == "1":
        print("l'article a été bien ajouté dans votre panier")
            # Si le choix est 2
    elif sc == "2":
        print("l'article a été bien supprimé de votre panier")
            # Si le choix est 3
    elif sc == "3":
        print("voici la liste des articles du panier")
            
            # Si le choix est 4
    elif sc == "4":
        print("votre panier a bien été supprimé")
            # Si le choix est 5
    else :        # Affichage d'un message de fin et on arrete le programme 
        print("Merci pour votre visite!!!")
        break