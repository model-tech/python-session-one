chiffre = input("Veuillez svp entrer un chiffre entre 2 et 9 : ")


while not chiffre in range(2,10) :
    chiffre = input("Veuillez svp entrer un chiffre entre 2 et 9 : ")
    for i in range(1,13):
        multiply = chiffre * i
        print(f"{chiffre} * {i} = {multiply}")
#elif  not chiffre.isalpha :
    #chiffre = input("Veuillez svp entrer un chiffre entre 2 et 9 : ")
    # else:
    # for i in range(1,13):
    # multiply = chiffre * i
    #  print(f"{chiffre} * {i} = {multiply}")



    

    #break
#else:
    #chiffre = input("Veuillez svp entrer un chiffre entre 2 et 9 : ")
    
    #for chiffre in range(2,10):
        #for i in range(1,13):
            #multiply = chiffre * i
            #print(f"{chiffre} *{i} = {multiply}")
        #break