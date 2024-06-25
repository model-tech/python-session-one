#afficher le menu 


print("""
Choisissez parmi les 5 options suivantes: 

1- Ajouter un article dans le panier
2- Supprimer un article du panier
3- Afficher tous les articles 
4- Vider le panier
5- Quitter
""")

#Entrez le choix1

choice=input("Quel est votre choix ?")
#conditions de validité du choix 


while choice not in range(1,6) and choice.isdigit==False:
    print(" ```mauvaise entrée, veuillez entrer une valeur entre 1 et 5```")
    choice=input("Quel est votre choix ?")
    while choice in range(1,6) and choice.isdigit==True:
        print("""```
                    Choisissez parmi les 5 options suivantes: 

                    1- Ajouter un article dans le panier
                    2- Supprimer un article du panier
                    3- Afficher tous les articles 
                    4- Vider le panier
                    5- Quitter


                    ```""")

                    
        choice=input("Quel est votre choix ?")

        if choice== "1":
            print("_**l'article a été bien ajouté dans votre panier**")
                        
            
        elif choice== "2":
            print("**l'article a été bien supprimé de votre panier**")
                        
            
            
        elif choice== "3":
            print("**voici la liste des articles du panier**")
                        
            
        elif choice== "4":
            print("**votre panier a bien été supprimé**")
                        
                
        else:
            print("**Merci pour votre visite!!!*")
                