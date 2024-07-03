# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
# Conversion Functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
# User Interaction
try:
    temperature = float(input("Enter a temperature to be converted: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if unit.upper() == 'C':
        print(f"{temperature} degrees Celsius is {convert_to_fahrenheit(temperature)}°F")
    elif unit.upper() == 'F':
        print(f"{temperature} degrees Fahrenheit is {convert_to_celsius(temperature)}°C")
    else:
        print("Invalid unit. Please enter 'C'/'F'.")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")