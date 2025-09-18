print("----- Welcome to Python Dice Roller Program -----")
import random
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│    ●    │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘")
}
playing = True
while playing:
    dice_list = []
    total = 0
    num_of_dice = int(input("How many dice do you want to roll? (Enter 0 to quit): "))
    if num_of_dice != 0:
        # Display dices as Horizontal line
        for dice in range(num_of_dice):
            dice_list.append(random.randint(1, 6))

        # Display as Vertical line
        # for dice in range(num_of_dice):
        #     for line in dice_art.get(dice_list[dice]):
        #         print(line)
        for line in range(5):
            for dice in dice_list:
                print(dice_art.get(dice)[line], end="")
            print()

        for dice in dice_list:
            total += dice
        print(f"Total: {total}")
        print("***************************************************")
    else:
        print()
        print("*************** Thanks for playing! ***************")
        playing = False
