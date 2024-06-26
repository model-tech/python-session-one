# 1-definir un dictionnaire vide 

# student = {}

# 2-definir un dictionnaire avec des elements

student = {
    "nom": "John", 
    "age": 28
    }
# print(student)

# 3-ajouter des elements dans un dictionnaire

# student["city"] = "Dakar"
# print(student)

# 4-supprimer des elements dans un dictionnaire

# student['test'] = 1234
# print(student)

# try:
#     del student["test"]
#     print(student)
# except KeyError:
#     print("La clé test n'existe pas")

# if "test" in student:
#     del student["city"]
#     print(student)
# else:
#     print("La clef 'test' n'existe pas")


# 5-modifier des elements dans un dictionnaire

# student["nom"] = "Hassan DIOP"
# student["age"] = 30
# print(student)

## if "city" in student:
##     student["city"] = "Paris"
##     print(student)
## else:
##     print("La clef 'city' n'existe pas")



# 6-extraire un element dans un dictionnaire via sa clé 

# print(student["city"])

# print(student.get("city"))

# 7-extraire les clés d'un dictionnaire

## print(student.keys())

## for key in student.keys():
##     print(key)


# 8-extraire les valeurs d'un dictionnaire

## print(student.values())

## for value in student.values():
##     print(value)


# 9-compter le nombre d'elements dans un dictionnaire

## print(len(student))


# 10-une liste de dictionnaire

# students = [
#     {"nom": "John", "age": 28},
#     {"nom": "Jane", "age": 27},
#     {"nom": "Jack", "age": 26}
# ]

# 11-extraire les clés et les valeurs d'un dictionnaire

## for student in students:
##     print(student["nom"], student["age"])

## for student in students:
##     print(student.get("nom"), student.get("age"))

# 12-les dictionnaires imbriques

## student = {
##     "nom": "John",
##     "age": 28,
##     "address": {
##         "street": "Main St",
##         "city": "New York",
##         "zip": 10001
##     },
##     "phone": [ 786310434, 786310435, 786310436 ],
##     "email": "XpJbB@example.com"
##      "is_married": False
## }



# - nom 
# - telephone [principal, secondaire]
# - email 
# - address (- rue, ville, pays )
# - solde 

# customer_one =[
#     "hassan diop", 
#     ["787875656", '776765667'], 
#     "hasan.diop@test.co",
#     ["rue 22", "dakar", "Senegal"],
#      260000 ]


# customers = [
#     [
#     "hassan diop", 
#     ["787875656", '776765667'], 
#     "hasan.diop@test.co",
#     ["rue 22", "dakar", "Senegal"],
#      260000 ],

#     [
#     "asalfo kone", 
#     ["787395656", '767765667'], 
#     "salo.kone@test.co",
#     ["rue 12", "abidjan", "CIV"],
#      20000 ],

#     [
#     "awa", 
#     ["707875656", '766765667'], 
#     "axa@test.co",
#     ["rue 32", "bamako", "Mali"],
#      260000 ]
# ]

# print("premier client", customers[0])
# print("nom premier client", customers[0][0])
# print("phones premier client", customers[0][1])

# [
# #     "hassan diop", 
# #     ["787875656", '776765667'], 
# #     "hasan.diop@test.co",
# #     ["rue 22", "dakar", "Senegal"],
# #      260000 ],

# customer = {
#     "name": "Hassan diop", 
#     "phones": ["787875656", '776765667'],
#     "email":"hasan.diop@test.co",
#     "address": {
#         "street": "rue 22",
#         "city": "Dakar",
#         "country": "Senegal"
#     },
#     "balance": 300000
# }

# print(customer["address"]["country"])

customers = [
{
    "name": "Hassan diop", 
    "phones": ["787875656", '776765667'],
    "email":"hasan.diop@test.co",
    "address": {
        "street": "rue 22",
        "city": "Dakar",
        "country": "Senegal"
    },
    "balance": 300000,
    "is_active": True
}, 
{
    "name": "carlos abachi", 
    "phones": ["787875656", '776765667'],
    "email":"hasan.diop@test.co",
    "address": {
        "street": "rue 22",
        "city": "Abidjan",
        "country": "CIV"
    },
    "balance": 490000,
    "is_active": False
},
{
    "name": "moustapha gaye", 
    "phones": ["787875656", '776765667'],
    "email":"hasan.diop@test.co",
    "address": {
        "street": "rue 22",
        "city": "Douala",
        "country": "Cameroun"
    },
    "balance": 380000,
    "is_active": True
}
]


for custumer in customers : 
    print("Le solde du client est : ", custumer.get("balance"))