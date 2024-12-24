class Bird:
    def fly(self):
        print("Flying high")

class Airplane:
    def fly(self):
        print("Flying through the clouds")

def take_off(transport):
    transport.fly()

# Creating objects of Bird and Airplane
bird = Bird()
airplane = Airplane()

take_off(bird)      # Output: Flying high
take_off(airplane)  # Output: Flying through the clouds
