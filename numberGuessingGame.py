import random

#python nymber guessing game

lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number, highest_number)
guesses = 0
is_running = True

print('Python number guessing game')
print(f'Select a number between {lowest_number} and {highest_number}')

while is_running:
    guess = input('Enter your guess: ')
    
    if not guess.isdigit():
        print('Please enter a valid number.')
        continue
    
    guess = int(guess)
    guesses += 1
    
    if guess < lowest_number or guess > highest_number:
        print(f'Your guess must be between {lowest_number} and {highest_number}.')
        continue
    
    if guess < answer:
        print('Too low, try again.')
    elif guess > answer:
        print('Too high, try again.')
    else:
        print(f'Congratulations! You guessed the number {answer} in {guesses} tries.')
        is_running = False