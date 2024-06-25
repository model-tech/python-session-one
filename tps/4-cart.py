choix = ""
while choix !="5":
      print("1-Ajouter un article")
      print("2-Supprimer un article")
      print("3-Afficher tous les articles")
      print("4-Vider le panier")
      print("5-Quitter")
      choix =  input("Quel est votre choix?")
      if choix.isdigit():
            if choix == "1":
                print("L'article a été bien ajouté dans votre panier")
            elif choix == "2":
                print("L'article a été bien supprimé de votre panier")
            elif choix == "3":
                print("Voici la liste des articles du panier")
            elif choix == "4":
                print("Votre panier a bien été supprimé")
            elif choix == "5":
                print("Merci pour votre visite!!!!")
            else:
                print("Mauvaise entrée, veuillez entrer une valeur entre 1 et 5")
      else:
         print("Mauvaise entrée, veuillez entrer une valeur entre 1 et 5")
