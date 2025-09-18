# Python Temperature Convertion
is_running = True
print("*** Welcome to Python Temperature Convertion ***")
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius, 2)
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 2)
while is_running:
    print("1. Converts from Celsius to Fahrenheit (°C -> °F)")
    print("2. Converts from Fahrenheit to Celsius (°F -> °C)")
    print("3. Exit")
    print("********************************************")
    option = input("Please choose one of the following options:")
    if option == "1":
        degree_celsius = float(input("Please enter your Celsius degree(°C): "))
        result = celsius_to_fahrenheit(degree_celsius)
        print(f"The temperature {degree_celsius}°C = {result}°F.")
    elif option == "2":
        degree_fahrenheit = float(input("Please enter your Fahrenheit degree(°F): "))
        result = fahrenheit_to_celsius(degree_fahrenheit)
        print(f"The temperature {degree_fahrenheit}°F = {result}°C")
    elif option == "3":
        print("Thank you for using Python Temperature Convertion! Goodbye!")
        is_running = False
    else:
        print("Please enter a valid option.")
    print()