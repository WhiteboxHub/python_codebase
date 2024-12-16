class Calculator:
    def add(self, *args):
        return sum(args)

# Creating an object of Calculator
calc = Calculator()

print(calc.add(1, 2))            # Output: 3
print(calc.add(1, 2, 3, 4))      # Output: 10
print(calc.add(1, 2, 3, 4, 5))  # Output: 15
