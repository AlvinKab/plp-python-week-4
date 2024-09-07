class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print(f"This user is called {self.name}, is {self.age} years old, and is {self.gender}.")

person1 = Person("John", 27, "male")
person1.introduce()