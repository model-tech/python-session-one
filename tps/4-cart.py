#nous allons établire une affiche  des options disponibles pour l'utilisateur#
def afficher_menu():
    print("\nChoisissez parmi les 5 options suivantes:")
    print("1- Ajouter un article dans le panier")
    print("2- Supprimer un article du panier")
    print("3- Afficher tous les articles")
    print("4- Vider le panier")
    print("5- Quitter")
    print("Quel est votre choix?")
#nous allons établire une fonction pour s'assurer que l'utilisateur entre une valeur valide#
def obtenir_choix():
    while True:
        choix = input()
        if choix.isdigit() and int(choix) in range(1, 6):
            return int(choix)
        else:
            print("mauvaise entrée, veuillez entrer une valeur entre 1 et 5")
# la fonction main va nous permettre de mettre en place une boucle indefinie jusqu'a ce qu'il décide de quitter avec le bouton 5#
def main():
    while True:
        afficher_menu()
        choix = obtenir_choix()
        
        if choix == 1:
            print("l'article a été bien ajouté dans votre panier")
        elif choix == 2:
            print("l'article a été bien supprimé de votre panier")
        elif choix == 3:
            print("voici la liste des articles du panier")
        elif choix == 4:
            print("votre panier a bien été supprimé")
        elif choix == 5:
            print("Merci pour votre visite!!!")
            break

if __name__ == "__main__":
    main()


