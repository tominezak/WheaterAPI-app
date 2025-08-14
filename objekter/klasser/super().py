# super() = brukt i en child klasse for å kalle på metoder i en parent klasse (super class)

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def describe(self):
        print(f"Shape: Color={self.color}, Filled={self.is_filled}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled) # kaller parent class Shape's constructor
        self.radius = radius
    
    def describe(self):
        super().describe()
        print(f'Its a circle with area {3.14 * self.radius ** 2}')

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled) # kaller parent class Shape's constructor
        self.width = width
    
    def describe(self):
        super().describe()
        print(f'Its a square with area {self.width ** 2}')


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled) # kaller parent class Shape's constructor
        self.width = width
        self.height = height
    
    def describe(self):
        super().describe()
        print(f'Its a triangle with area {0.5 * self.width * self.height}')

circle = Circle("Red", True, 5)
# print(f"Circle: Color={circle.color}, Filled={circle.is_filled}, Radius={circle.radius}")

square = Square("Blue", False, 4)
# print(f"Square: Color={square.color}, Filled={square.is_filled}, Width={square.width}")

triangle = Triangle("Green", True, 3, 4)
# print(f"Triangle: Color={triangle.color}, Filled={triangle.is_filled}, Width={triangle.width}, Height={triangle.height}")

circle.describe()  # method overriding - barn deler samme metode som parent - brukes child