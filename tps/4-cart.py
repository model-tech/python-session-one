#on va premierement creer une fonction permettant d'afficher le menu plus facilement

def menu():

    print("""  
        Choisissez parmi les 5 options suivantes: 

        1- Ajouter un article dans le panier
        2- Supprimer un article du panier
        3- Afficher tous les articles 
        4- Vider le panier
        5- Quitter         
""")

#on affiche le menu et on demande à l'utilisateur de choisir une option

menu()  
choice = input("Quel est votre choix ? : ")

#Ici on verifie que l'option choisie est valide, tant que ce n'est pas le cas, on redemande à l'utilisateur de choisir

while not (choice.isdigit() and 1 <= int(choice) <= 5):
    print("mauvaise entrée, veuillez entrer une valeur entre 1 et 5")
    menu()
    choice = input("Quel est votre choix ? : ")

#maintenant qu'il a entré une option valide, on va afficher pour chaque entrée, le message correspondant

else:

    #tant que l'option choisie est differente de 5, on va afficher pour chaque entrée, le message correspondant, suivi du menu, en redemandant à l'utilisateur de choisir

    while int(choice) != 5 :
        if int(choice) == 1 :
            print("**l'article a été bien ajouté dans votre panier**")
        elif int(choice) == 2 :
            print("**l'article a été bien supprimé de votre panier**")
        elif int(choice) == 3 :
            print("**voici la liste des articles du panier**")
        elif int(choice) == 4 :
            print("**votre panier a bien été supprimé**")

        menu()  
        choice = input("Quel est votre choix ? : ")

        #on verifie toujours que l'option choisie est valide, tant que ce n'est pas le cas, on redemande à l'utilisateur de choisir
        while not (choice.isdigit() and 1 <= int(choice) <= 5):
            print("mauvaise entrée, veuillez entrer une valeur entre 1 et 5")
            menu()
            choice = input("Quel est votre choix ? : ")
    else:

        #lorsque l'option choisie est 5, on n'affiche plus de menu et on ne demande plus à l'utilisateur de choisir.

        print("**Merci pour votre visite!!!**")
