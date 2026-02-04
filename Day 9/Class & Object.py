class Student:
    def __init__(self, name, age):
        self.name = name   # instance variable
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating object
s1 = Student("Devashish", 22)
s1.display()
