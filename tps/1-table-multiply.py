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

    
            
    
