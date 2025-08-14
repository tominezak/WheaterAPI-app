# object = er en instans av en klasse med relaterte attributter (variabler) og metoder(funksjoner).
# class = en mal for å lage objekter. Den definerer attributtene og metodene som objektene vil ha.

from car import Car

car1 = Car("Toyota Corolla", 2020, "Red", True)
car2 = Car("Honda Civic", 2019, "Blue", False)
car3 = Car("Ford Focus", 2021, "Black", True)

print(car1.model)  # Output: Toyota Corolla
print(car1.year)   # Output: 2020
print(car1.color)  # Output: Red
print(car1.for_sale)  # Output: True

car2.drive()  # Output: You are driving the car!
car3.stop()   # Output: You have stopped the car!
car1.describe()  # Output: 2020 Red Toyota Corolla - For Sale: True