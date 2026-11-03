class Animal:
    def __init__(self, name: str):
        self.name = name

class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Elly")
print(my_dog.bark())