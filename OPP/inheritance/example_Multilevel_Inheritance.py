class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def whimper(self):
        print("Puppy whimpers")

# Creating an object of Puppy
puppy = Puppy()
puppy.speak()    # Output: Animal speaks
puppy.bark()     # Output: Dog barks
puppy.whimper()  # Output: Puppy whimpers
