### veillez entrez un nombre compris entre 2 et 9
# si il entre un nombre compris entre 2 et 9
#effectuez la table de multiplication de ce nombre ###

nombre_choisi = input ("entrez un nombre compris entre 2 et 9: ")
if nombre_choisi.isdigit(): 
    nombre= int(nombre_choisi)
    if (nombre >=2) and (nombre <=9):
        for i in range (1,13):
            print(f"{nombre} x {i}) = {nombre*i}")
    else:
            print("enter un nombre entre 2 et 9")
   else
          print("entrez un nombre numérique") 
 
