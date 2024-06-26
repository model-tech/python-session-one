# 1)definir une chaine de charactères
first_name = "Hassan"
last_name  = "Diop"

# 2)afficher une chaine de charactères
## print()
# Bonjour Nom: Hassan Prenom: DIOP
# print("bonjour", first_name, last_name)
# print("Bonjour Nom:", first_name, "Prenom:",last_name )
# print(f"Bonjour Mr Nom: {first_name} Prenom: {last_name}")

# 3)trouver un charactere dans une chaine de charateres
## find() 
## string.find(value, start, end)
description = """A Data Analyst is a professional who collects and analyzes 
            data across the business to make informed decisions1. 
            They work with large datasets and use tools to interpret data 
            and extract relevant insights. Data Analysts complement Data 
            Scientists by analyzing existing data or creating new datasets"""

# print(description.find("."))

# 4)la position d'une chaine de charactères
## index()
## string.index(value, start, end)

# print(description.index("is"))

# 5)la sous chaine d'une chaine de charactères
## slice()
## string.slice(start, end)

# print

# 6)les methodes de chaine de charactères
    ## isalnum() --> alpha numeric
    ## isalpha() --> alphabetique
    ## isdigit() --> uniquement des chiffres
    ## islower() --> minuscule
    ## isupper() --> majuscule

# test = "UPDAS"
# print(test.isupper())



# 7) remplacer un element dans une chaine de charactères
## replace()
## string.replace(old, new, count)

# print(description)

# description_with_toto = description.replace("Data", "TOTO")

# print(description)

# print(description_with_toto)


# 8) supprimer les espaces dans une chaine de charactères
## strip()
# string.strip()

# email = "   test@gmail.co    "
# print(email.strip())

# 9) verifier si une chaine de charactères commence par une chaine de charactères
## startswith()
## string.startswith(value, start, end)

# 10)verifier si une chaine de charactères se termine par une chaine de charactères
## endswith() 
## string.endswith(value, start, end)

# 11) met en minuscule une chaine de charactères
## lower()
## string.lower()

# 12) met en majuscule une chaine de charactères
## upper()
## string.upper()

