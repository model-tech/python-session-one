print("***** Petit jeu permettant de deviner un nombre entre 1   et 100 en 5 essais *****")
import random
n = random.randint(1,100)
for i in range ( 1 , 6 ) : 
  var = int(input("saisir un nombre entre 1 et 100: "))
  if var >n : 
        print ("Très grand! choisir un autre plus petit")
  elif var < n :
      print ( "Très petit! choisir un autre plus grand")
  else : 
        break
if  i < 6 and var ==n : 
 print ( "Bravo!!!! vous avez trouvé le bon nombre!!!","en",i,"essais")
else :  
 print( "Game over!!! le nombre etait :",n)