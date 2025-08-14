# multiple inheritance = inherit from more than one parent class C(A, B)
# multilevel inheritance = inherit from a parent class that inherits from another parent class C(A(B)) = C(B) <- B(A) <- A
# tenk at animal er besteforeldre og at prey og predator er foreldre og at rabbit og hawk er barn

class Animal:
    def __init__(self, name): # konstruktøren arves
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing!")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting!")

class Rabbit(Prey):
    def hop(self):
        print(f"{self.name} is hopping!")

class Hawk(Predator):
    def soar(self):
        print(f"{self.name} is soaring!")

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bunny")
rabbit.flee()  # Output: Bunny is fleeing!
rabbit.sleep()  # Output: This animal is sleeping.

hawk = Hawk("Eagle")
hawk.hunt()  # Output: Eagle is hunting!

fish = Fish("Goldfish")
fish.flee()  # Output: Goldfish is fleeing!
fish.hunt()  # Output: Goldfish is hunting!

