# Legger til lister som elementer i en annen liste
# print(hovedliste[3][3])

"""
for collection in groceries:
    for food in collection:
        print(food, end=' ')
    print()
    
"""

# kalkulator display:
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8 ,9),
           ('*', 0, '#'))
for row in num_pad:
    for num in row:
        print(num, end=' ')
    print()