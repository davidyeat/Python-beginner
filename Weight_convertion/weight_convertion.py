
def kg_to_pound(kg):
    pound = kg * 2.205
    return  round(pound,1)
def pound_to_kilograms(lbs):
    kilogram = lbs / 2.205
    return round(kilogram, 1)
is_running = True
while is_running:
    print("***** Phyton Weight Converter Program *****")
    print("Which type of convertion do you want?")
    print("1. Converts from Kilograms to Pounds (Kgs -> Lbs)")
    print("2. Converts from Pounds to Kilograms (Lbs -> Kgs)")
    print("3. Exit")
    print("*******************************************")
    question = input("Enter your choice: ")
    if question == '1':
        weight = float(input("Enter your weight(Kg): "))
        converted_weight = kg_to_pound(weight)
        print(f"Your weight {weight} kgs = {converted_weight} lbs ")
    elif question == '2':
        weight = float(input("Enter your weight(Lbs): "))
        converted_weight = pound_to_kilograms(weight)
        print(f"Your weight {weight} lbs = {converted_weight} kgs ")
    elif question == '3':
        print("Thank you for using this program. Goodbye!")
        is_running = False
    else:
        print("Invalid input. Please try again.")
    print()