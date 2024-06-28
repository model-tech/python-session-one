class Person:

    def __init__(self,p_firstname, p_lastname, p_age):
        self.firstname = p_firstname
        self.lastname = p_lastname
        self.age = p_age

    def get_age(self):
        print(f"Vous avez {self.age} ans ")


person_1 = Person("Gildas", "GAYERI", 23) 
person_2 = Person("khoudia", "DIAO", 17)

print(person_1.lastname)
print(person_2.age)

person_2.get_age()


