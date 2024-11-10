class Person:
    def __init__(self, name, age, gender):
        self.name=name
        self.gender=gender
        self.age=age


    def movement(self):
            print("Person is walking")

person1 = Person("Evans", 12, "Male")
print(person1.name)

person2 = Person("Faith",10, "Female")
print(person2.name)

person3 = Person("Gladys", 10, "Female")
print(person3.name)













