class Person:
    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def eat(self):
        print("eating")


def walk(self):
    print("walking")


def getName(self):
    return self.name


def getAge(self):
    return self.age


class Student(Person):
    rollnumber = 1
    marks = 100

    def takeClass(self):
        print("taking Class")


student = Student("rina", 20, "female", 10)
student.eat()
student.walk()
