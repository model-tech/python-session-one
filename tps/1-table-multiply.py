#demande à l'utilisateur d'entrer un nombre entre 2 et 9 
S = input("entrez un nombre entre 2 et 9: ")
#verifier que le nombre entré est numérique 
if S.isdigit()  :
    #le nombre entré est numérique donc on le convertis en entier 
    T = int(S)
    #on vérifie que le nombre entier est compris entre 2 et 9
    if 2<= T <= 9 :
     # le nombre entré est compris entre 2 et 9 
     #comme on veut la multiplication de 1 à 12 on va prendre de 1 a 13    
        for i in range(1, 13):
            #il va prendre 1 et multiplier par le nombre entré  et afficher ainsi de suite 
            """une chose a ne surtout pas oublier , c'est de s'assurer que b est vraiment un nombre 
            sinon on pourra pas faire la multiplication """
            print(f"{T} * {i} = {T * i}" )
    else :
        #si le nombre n'est pas compris entre 2 et 9 
        print("entrez un nombre entre 2 et 9" )
        
else :
    #si ce n'est pas un nombre ce que l'utilisateur a entré
    print("entrez un nombre numérique")
    
            
    
