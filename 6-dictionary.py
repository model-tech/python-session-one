# 1-definir un dictionnaire vide 

## student = {}

# 2-definir un dictionnaire avec des elements

## student = {"nom": "John", "age": 28}

# 3-ajouter des elements dans un dictionnaire

## student["city"] = "New York"
## print(student)

# 4-supprimer des elements dans un dictionnaire

## del student["city"]
## print(student)

## if "city" in student:
##     del student["city"]
##     print(student)
## else:
##     print("La clef 'city' n'existe pas")


# 5-modifier des elements dans un dictionnaire

## student["age"] = 29
## print(student)

## if "city" in student:
##     student["city"] = "Paris"
##     print(student)
## else:
##     print("La clef 'city' n'existe pas")



# 6-extraire un element dans un dictionnaire via sa clé 

## print(student["age"])

## print(student.get("age"))

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

## students = [
##     {"nom": "John", "age": 28},
##     {"nom": "Jane", "age": 27},
##     {"nom": "Jack", "age": 26}
## ]

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