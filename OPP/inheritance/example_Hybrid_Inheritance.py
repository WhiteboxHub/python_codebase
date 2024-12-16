class Animal:
    def speak(self):
        print("Animal speaks")

class Flyer:
    def fly(self):
        print("Flying high")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Bird(Dog, Flyer):
    pass

# Creating an object of Bird
bird = Bird()
bird.speak()  # Output: Animal speaks
bird.bark()   # Output: Dog barks
bird.fly()    # Output: Flying high
