class Bird:
    def fly(self):
        print("Flying high in the sky!")

class Airplane:
    def fly(self):
        print("Flying through the clouds!")

def take_off(transport):
    transport.fly()

bird = Bird()
airplane = Airplane()

take_off(bird)      # Output: Flying high in the sky!
take_off(airplane)  # Output: Flying through the clouds!
