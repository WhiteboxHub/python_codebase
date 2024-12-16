class Animal:
    def speak(self):
        print("Animal speaks")

class Flyer:
    def fly(self):
        print("Flying high")

class Bird(Animal, Flyer):
    pass

# Creating an object of Bird
bird = Bird()
bird.speak()  # Output: Animal speaks
bird.fly()    # Output: Flying high
