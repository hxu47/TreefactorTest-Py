class Circle:
    def __init__(self):
        self.radius = 5  # Attribute

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

circle = Circle()
print(circle.calculate_area())