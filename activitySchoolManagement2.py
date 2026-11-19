class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def get_name(self):
        return self.name

    def get_age(self):
        return self.__age

person1 = Person("AV", 14)
print(f"Name: {person1.get_name()}")
print(f"Age: {person1.get_age()}")

# Reflection
# I think it is better to access __age through the get_age() method because it is private and cannot be accessed directly from outside the class. 