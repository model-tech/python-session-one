# 1) creation d'une liste vide 

students = []

# 2)creation d'une liste avec des elements

fruits = ["pomme", "cerise", "orange", "banane", "mangue", "poire"]
         # 0        1          2           3          4          5 
         # -6       -5         -4          -3         -2         -1

# print(fruits[-6])

# 3)ajouts d'elements dans une liste 

## append

# fruits.append("kiwi")

# print(fruits)

## insert

# fruits.insert(0,"pamplemousse")

# fruits.insert(2,"papaye")

# print(fruits)

# 4)suppression d'elements dans une liste

## pop

# fruits.pop(2)

# print(fruits)

# 5)modification d'elements dans une liste

## splice

# 6)concaténation de listes

## concat

# legumes = ["carotte", "tomate", "courgette", "navet"]
# feculents = ["pain", "sauce", "fromage"]

# legumes_et_feculents = legumes + feculents
# print(legumes_et_feculents)


# 7)compter le nombre d'elements dans une liste

## length

# print(len(legumes_et_feculents))


# 8)inverser une liste

# print(fruits)

# fruits.reverse()

# print(fruits)

## reverse

# 9)rechercher un element dans une liste

## indexOf

# print(fruits)

# print(fruits.index("banane"))

# 10)trier une liste

## sort

# print(fruits)

# fruits.sort()

# print(fruits)


notes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
notes.sort(reverse=True)

print(notes)

