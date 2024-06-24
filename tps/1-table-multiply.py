### Entrer un nombre compris entre 2 et 9 
# si le nombre entré remplie les conditions, 
# effectuer une table de multiplication de ce nombre ###

nombre_choisi = input(" Entrer un nombre comprit entre 2 et 9 : ")
if nombre_choisi.isdigit() :
    nombre = int(nombre_choisi)
    if 2 <= nombre <= 9 :
        for i in range(1,13) :
            print(f"{nombre} * {i} = {nombre * i}") 
    else :
        print("Entrer un nombre entre 2 et 9") 
else :
    print("Entrer un nombre numérique")

