class Person:

    def __init__(self, name="Person", age=30):
        self.age = age
        self.name = name


    def display(self):
        print(f"Student {self.name} is {self.age} years old")


class Student(Person):

    def __init__(self, name="Student", age=18, major="Math"):
        Person.__init__(self, name, age)
        self.major = major

