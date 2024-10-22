class Circle:
    def __init__(self, radius):
        self.radius = radius  # Now initialized with a parameter

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print(circle.calculate_area())