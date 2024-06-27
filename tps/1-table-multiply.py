### Veuillez entrer un nombre compris entre 2 et 9
# si le nombre choisi est compris entre 2 et 9
# effectuer une table de multiplication de ce nombre ###

nombre_choisi = input("Entrer un nombre compris entre 2 et 9 : ")
if nombre_choisi.isdigit():
    nombre = int(nombre_choisi)
    if (nombre >=2) and (nombre<=9):
        for i in range(1,13):
            print(f"{nombre} x {i} = {nombre*i}")
    else:
            print("Entrer un nombre entre 2 et 9")
else:
     print("Entrer un nombre numérique ") 

