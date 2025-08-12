# input returnerer input data som en streng

"""
name = input('Hva er navnet ditt?: ')
age = input('alder: ')

age = int(age) # Kan integrere denne i linjen over
age += 1

print(f'{age}')
print(f'Hello {name}')
"""

# Shooping cart program
item = input('Hva vil du kjøpe?: ')
price = float(input('Hva er prisen?: '))
quantity = int(input('Hvor mange?: '))

total = price * quantity

print(f'Du har kjøpt {quantity} x {item}/s')
print(f'Totalen blir: ${total}')