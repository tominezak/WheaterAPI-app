# python slot machine game

import random


def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🍊', '🔔']

    result = []

    return[random.choice(symbols) for symbol in range(3)] 
'''
    for symbol in range(3): 
        result.append(symbols[random.randint(symbols)])

    return result
'''

def print_row(row):
    print('**********************')
    print(' | '.join(row))  # Assuming row is a list of symbols to be printed
    print('**********************')

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🍊':
            return bet * 6
        elif row[0] == '🔔':
            return bet * 10
    return 0  # No payout if symbols do not match or are not winning symbols

def main():
    balance = 100

    print('**************************')
    print("Welcome to the Python Slots!")
    print('Symbols: 🍒, 🍉, 🍋, 🍊, 🔔')
    print('**************************')

    while balance > 0:
        print(f'Current balance: ${balance}')

        bet = input('Enter your bet amount: ')

        if not bet.isdigit():
            print('Invalid bet amount. Please enter a number.')
            continue
        
        bet = int(bet)

        if bet > balance:
            print('Insufficient balance for this bet.')
            continue

        if bet <= 0:
            print('Bet must be greater than zero.')
            continue

        balance -= bet

        row = spin_row() # returnerer en liste
        print('Spinning the row...\n')
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f'Congratulations! You won ${payout}!')
        else:
            print('Sorry, you did not win this time.')
        
        balance += payout

        play_again = input('Do you want to play again? (y/n): ').lower()
        if play_again != 'y':
            print('Thanks for playing!')
            break
    
    print('********************************************')
    print(f'Game over! Your final balance is ${balance}')
    print('********************************************')

if __name__ == "__main__":
    main()