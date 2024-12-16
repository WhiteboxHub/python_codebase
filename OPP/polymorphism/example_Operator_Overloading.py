class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the '+' operator to add two Point objects
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Creating Point objects
point1 = Point(2, 3)
point2 = Point(4, 5)

# Adding two Point objects using the overloaded '+' operator
result = point1 + point2
print(result)  # Output: Point(6, 8)
