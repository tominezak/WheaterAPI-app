# inheritance = gir klasser mulighet til å arve egenskaper og metoder fra en annen klasse 
# class Child(Parent): # Child arver fra Parent

class Animal:
    def __init__(self, name):
        self.name = name
        self.isAlive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says Meow!")

class Mouse(Animal):
    def squeak(self):
        print(f"{self.name} says Squeak!")

dog = Dog("Buddy")
cat = Cat("Whiskers")
mouse = Mouse("Mickey")

print(dog.name)  # Output: Buddy
print(dog.isAlive)  # Output: True
dog.eat() # Output: Buddy is eating.
cat.sleep()  # Output: Whiskers is sleeping.

dog.bark()  # Output: Buddy says Woof!
cat.meow()  # Output: Whiskers says Meow!
mouse.squeak()  # Output: Mickey says Squeak!