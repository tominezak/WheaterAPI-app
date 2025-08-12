import random

# print(help(random))

low = 1
high = 100
options = ('ROCK', 'PAPER', 'SCISSORS')
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "JACK", "QUEEN", "KING", "ACE"]

random_number = random.randint(low, high)  # Generates a random integer between low and high (inclusive)
print(f'Random number between 1 and 100: {random_number}')

number = random.random() # Generates a random float between 0.0 and 1.0

option = random.choice(options)  # Randomly selects an element from the options tuple
print(f'Random choice from options: {option}')

random.shuffle(cards)  # Randomly shuffles the list of cards
print(f'Shuffled cards: {cards}')

