class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def display_name(self):
        print(f"Name: {self.name}")

    def get_age(self):
        print(f"Age: {self.__age}")

class Student(Person):
    def study(self):
        print(f"{self.name} is studying.")

student1 = Student("AV", 14)
student1.display_name()
student1.get_age()
student1.study()