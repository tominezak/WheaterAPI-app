# polymorphism = many forms
# two ways to achieve polymorphism:
# 1. Inheritance = an object could be treated of the same type as its parent class.
# 2. duck typing = object must have necessary methods and attributes to be treated as a certain type.

from abc import ABC, abstractmethod # Abstract Base Class for polymorphism

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height
    
class Pizza(Circle):
    def __init__(self, toppings, radius):
        super().__init__(radius)
        self.toppings = toppings

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 15)] # List of different shapes

for shape in shapes:
    print(shape.area())  # Calls the area method of each shape, demonstrating polymorphism