# duck typing = if it walks like a duck and quacks like a duck, it is a duck

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Car:

    alive = False  # This class does not inherit from Animal
    
    def speak(self):
        print("Beep beep!")

animals = [Dog(), Cat(), Car()]  # List of different objects

for animal in animals:
    animal.speak() 
    print(animal.alive)  # This will raise an AttributeError for Car, demonstrating duck typing
