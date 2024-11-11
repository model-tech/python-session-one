<<<<<<< HEAD
#print("Bonjour je suis présent")
#
#x = 20
#if x < 18: 
  #  print("mineur")
#elif x == 18:
 #   print("juste majeur")
#else:
   # print("je suis majeur")
#x = 2
#y = 0
#while x > 0 :
  #    y = y - 1
    #  print(y)
     # print("si on arrive ici, on a fini")
for x in [1,5,7]:
    print(x)
    print("fin de la boucle")
    name = input["lamine"]
    print(name)

=======
#table multi
#demande à l'utilisateur d'entrer un nombre entre 2 et 9 
s = input("entrez un nombre entre 2 et 9: ")
#tant que s est pas numérique et entier de s  n'appartient pas a [2,9] (intervalle ) 
while not (s.isdigit() and 2<=int(s)<=9) :
#on lui affiche les messages d'eereur 
    print("la valeur n'est pas bonne")
    s = input("entrez un nombre entre 2 et 9: ")
#ici on convertie s en entier 
t = int(s)
#ici on prends i entre 1 et 13 comme on veut qu'il s'arrete a 12 
for i in range(1, 13) :
#ici on affiche la multiplication et le résultat 
    print(f"{t}*{i} = {t*i}")

    
            
    
>>>>>>> 0fc541d66c3e5f92c22bd7e04e1a9e0e58a4d893
