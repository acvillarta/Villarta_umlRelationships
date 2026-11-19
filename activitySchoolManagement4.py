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

class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching.")

teacher = Teacher("Mr. Smith", 40)
teacher.display_name()
teacher.get_age()
teacher.teach()