class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print("Bow bow")
pet=Dog("Jade",2)
pet.bark()
print(pet.name)
print(pet.age)
