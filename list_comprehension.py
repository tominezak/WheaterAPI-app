# list comprehension = [x for x in range(1, 11)]  # Creates a list of numbers from 1 to 10
# a concise way to create lists in Python - compact and easier to read than tradiytional for loops

doubles = []
for x in range(1, 11):
    doubles.append(x * 2)
print(doubles)
print()
# Using list comprehension to achieve the same result:
doubles_comp = [x * 2 for x in range(1, 11)]
print(doubles_comp)

triples = [y * 3 for y in range(1, 11)]
print(triples)

squares = [z ** 2 for z in range(1, 11)]
print(squares)

fruits = ['apple', 'orange', 'banana', 'coconut']
fruits_upper = [fruit.upper() for fruit in fruits] #kunne også puttet listen rett inn i fruits
print(fruits_upper)
fruit_chars = [fruit[0] for fruit in fruits]  # første bokstav i hvert element
print(fruit_chars)

numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_numbers = [num for num in numbers if num > 0]  # filtrerer ut negative tall
negative_numbers = [num for num in numbers if num < 0]  # det som returneres settes først
even_numbers = [num for num in numbers if num % 2 == 0]  # filtrere ut partall
odd_numbers = [num for num in numbers if num % 2 != 0]  # filtrere ut oddetall
print(positive_numbers)
print(negative_numbers)
print(even_numbers)
print(odd_numbers)