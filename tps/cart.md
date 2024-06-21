# Instructions  

Vous devez écrire un programme qui va afficher à l'utilisateur le menu suivant pour un panier numérique : 

```
Choisissez parmi les 5 options suivantes: 

1- Ajouter un article dans le panier
2- Supprimer un article du panier
3- Afficher tous les articles 
4- Vider le panier
5- Quitter

Quel est votre choix?
```

Et en fonction de ce que l'utilisateur va entrer, le programme va afficher un message particulier et demander à nouveau quelle action il veut pour la suite. 

Si l'utilisateur entre une valeur qui n'est pas permise par le menu, le programme lui affiche le message ```mauvaise entrée, veuillez entrer une valeur entre 1 et 5```   et lui demander à nouveau d'entrer une valeur entre 1 et 5. 

Si l'utilisateur entre du texte ou alors n'entre rien, alors vous allez lui afficher le même message d'erreur et lui demander d'entrer la bonne valeur. 

## PS: Vous devez repeter cela tant qu'il rentre une mauvaise valeur. 

Si il entre une valeur entre 1 et 5 alors : 

- Si c'est 1, vous affichez _**l'article a été bien ajouté dans votre panier**_  et ensuite vous lui affichez le menu et vous lui demander quel est son choix.
- Si c'est 2, vous affichez _**l'article a été bien supprimé de votre panier**_  et ensuite vous lui affichez le menu et vous lui demander quel est son choix.
- Si c'est 3, vous affichez _**voici la liste des articles du panier**_  et ensuite vous lui affichez le menu et vous lui demander quel est son choix.
- Si c'est 4, vous affichez _**votre panier a bien été supprimé**_  et ensuite vous lui affichez le menu et vous lui demander quel est son choix.
- Si c'est 5, vous affichez _**Merci pour votre visite!!!**_ .



## Indices 
``` 
1- Pensez à la boucle While 
2- Pensez à la methode isdigit()
3- Pensez à la fonction range()
4- Pensez à utiliser les condition If-Elif-Else 
```

