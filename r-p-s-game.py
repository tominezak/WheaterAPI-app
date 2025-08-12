import random

options = ('ROCK', 'PAPER', 'SCISSORS')
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice (ROCK, PAPER, SCISSORS): ").upper()

    print(f'Player choice: {player}')
    print(f'Computer choice: {computer}')

    if player == computer:
        print("It's a tie!")
    elif player == "ROCK" and computer == "SCISSORS":
        print("Player wins!")
    elif player == "PAPER" and computer == "ROCK":
        print("Player wins!")
    elif player == "SCISSORS" and computer == "PAPER":
        print("Player wins!")
    else:
        print("You lose! Computer wins!")
    if not input("Do you want to play again? (y/n): ").lower() == 'y':
        running = False
        print("Thanks for playing!")