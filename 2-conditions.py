# 1) if 

age = input("Quel est votre age ? ")
# "28" != 28
# int("28") ===> 28
# float("28.6") ===> 28.6
# str(10) ===> "10"
# str(28.6) ===> "28.6"
# int(28.6) ===> 28
# float(28) ===> 28.0

# if int(age) >= 18:
#     print("Vous etes majeur")

# 2) if - else 

# if int(age) >= 18:
#     print("Vous etes majeur")
# else:
#     print("Vous etes mineur")

# 3) if - elif - else

# 20 ans . ===> "20 ans ."
# int("20 ans .") ===> 20
# "36783635278282736383833"

# age = "20 ans"
# int(age) ==> int("20 ans")


if age.isdigit():
    age = int(age)
    if age > 18:
        print("Vous etes majeur")
    elif age == 18:
        print("Vous êtes juste majeur")
    else:
        print("Vous etes mineur")
else:
    print("Veuillez entrer une valeur numerique")



# 4) verifier qu'une variable est vide

# name = input("Quel est votre nom ? ")

# if name != "":
#     print(name)
# else:
#     print("Aucun nom")

# 5) operateur de comparaison

# ## ==
# a = 10 
# b = 20

# if a == b:
#     print("a est egale a b")
# else:
#     print("a est different de b")
## !=

## <

## >

## <=

## >=


# 6) operateur arithmetique

## +

## -

## *

# montant_ht = 10000 
# tva = 0.18 

# montant_ttc = montant_ht * (1 + tva)

# print(montant_ttc)

## /

## %

# restulat = 7%2
# print(restulat)
## **

# restulat = 7**2
# print(restulat)

## // 

# restulat = 7//2
# print(restulat)

# 7)operateur logique 

## and

# note = input("Quelle est votre note ? ")

# if int(note) < 10:
#     print("Insuffisant")
# elif int(note) >= 10 and int(note) < 12:
#     print("Passable")
# elif int(note)>= 12 and int(note) < 14:
#     print("Assez bien")
# elif int(note)>= 14 and int(note) < 16:
#     print("Bien")
# elif int(note)>= 16 and int(note) < 18:
#     print("Tres bien")
# elif int(note)>= 18:
#     print("Excellent")

## or

## not

# 8) verifier qu'une variable est alphabetique

# name = input("Quel est votre nom ? ")
# name = "2233333"
# if (name.isdigit()):
#     print("Le nom est numerique")
# else:
#     print("Le nom n'est pas numerique")

## isalpha

# 9)verifier qu'une variable est numerique

## isdigit

# 10) verifier qu'une variable est alphabetique et numerique

## isalnum


