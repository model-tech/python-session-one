# créer une fonction qui affiche votre age en fonction de votre
# année de naissance 

price = 20000


def calcul_age(annee_naissance):
    age = 2024 - int(annee_naissance)
    print(f"Vous avez {age} ans")


def calcul_ttc(mt_ht, tax_rate):
    result = mt_ht * (1 + tax_rate)
    return result


calcul_age(2002)
calcul_ttc(100000, 0.17)




# def salutation():
#     print("Bonjour tout le monde !!!!!")


# def affiche_notes(*notes):
#     print(f"la première note est {notes[0]}")
#     print(f"la seconde note est {notes[1]}")
#     print(f"la troisième note est {notes[2]}")
#     print(f"la quatrième note est {notes[3]}")





# affiche_notes(12, 6,18)


# salutation()


# ttc = calcul_ttc(100000, 0.18)
# print("Le montant ttc est ", ttc, " XOF")


# input_age = input("Entrez votre année de naissance: ")

# while not input_age.isdigit():
#     print("Error !!!! Invalid input")
#     input_age = input("Entrez votre année de naissance: ")

# calcul_age(input_age)

# if(input_age.isdigit()):
#     calcul_age(input_age)
# else: 
#     print("Veuillez entrer uniquement des chiffres ou nombre!")