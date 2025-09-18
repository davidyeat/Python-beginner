import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("---------- Welcome to Python Number Guessing Game ----------")
print(f"Select a number between {lowest_num} and {highest_num}")
while is_running:
    player = input("Enter your guess number: ")
    if player.isdigit():
        guesses += 1
        if int(player) < lowest_num or int(player) > highest_num:
            print("That number is out of range!")
            print(f"Select a number between {lowest_num} and {highest_num}")
        elif int(player) < int(answer):
            print(f"=> Too Low. Try again.")
        elif int(player) > int(answer):
            print(f"=> Too High. Try again.")
        else:
            print(f"=> CORRECT! The answer was {answer}.")
            print(f"You guessed {guesses} times.")
            print()
            print("---------------- Thank you for playing! ----------------")
            is_running = False
    else:
        print("Invalid guess.")
        print(f"Select a number between {lowest_num} and {highest_num}")
    print("********************************************************")
