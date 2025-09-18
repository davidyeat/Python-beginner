import random

print("---------- Welcome to Python Rock, Paper, Scissors Game ---------")
options = ('rock', 'paper', 'scissors')
is_running = True
player_score = 0
computer_score = 0
while is_running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a choice (Rock, Paper, Scissors): ").lower()
        if player not in options:
            print("Invalid choice. Please try again.")
            print("--------------------")
    print(f"Player Sign: {player}")
    print(f"Computer Sign: {computer}")
    if player == computer:
        print("It's a tie!")
    elif player == 'rock' and computer == 'scissors':
        player_score += 1
        if computer_score > 0:
            computer_score -= 1
    elif player == 'scissors' and computer == 'paper':
        player_score += 1
        if computer_score > 0:
            computer_score -= 1
    elif player == 'paper' and computer == 'rock':
        player_score += 1
        if computer_score > 0:
            computer_score -= 1
    else:
        computer_score += 1
        if player_score > 0:
            player_score -= 1
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")
    print("--------------------")
    if player_score == 3:
        print(f"=> CONGRATULATIONS! You win!")
        is_running = False
    elif computer_score == 3:
        print(f"=> Game Over! You lose!")
        is_running = False
print("Thanks for playing!")