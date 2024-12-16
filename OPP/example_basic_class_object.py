class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

# Creating an object
dog1 = Dog("Buddy", 5)
dog1.bark()  # Output: Buddy says woof!
