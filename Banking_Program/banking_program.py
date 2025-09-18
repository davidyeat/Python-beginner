# Python Banking Program
def show_balance(balance):
    print(f"=> Your balance is ${balance:.2f}")
def deposit():
    amount = float(input("Enter your deposit amount: $"))
    if amount <= 0:
        print("That's not a valid amount!")
        return 0
    else:
        return amount
def withdraw(balance):
    amount = float(input("Enter your withdraw amount: $"))
    if amount <= 0:
        print("That's not a valid amount!")
        return 0
    elif amount > balance:
        print("You don't have enough Amount!")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True
    while is_running:
        print("***** WELCOME TO THE BANKING PROGRAM *****")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit Program")
        print("******************************************")
        option = int(input("Which option do you want to use? (1-4): "))
        if option == 1:
            show_balance(balance)
        elif option == 2:
            balance += deposit()
        elif option == 3:
            balance -= withdraw(balance)
        elif option == 4:
            print("Thanks for using Banking Program. Goodbye!")
            is_running = False
        else:
            print("Invalid option. Please try again.")
        print()
if __name__ == "__main__":
    main()