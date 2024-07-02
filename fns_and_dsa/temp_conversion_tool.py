# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Conversion Functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User Interaction
try:
    temperature = float(input("Enter the temperature: "))
    unit = input("Enter the unit Celsius or Fahrenheit? (C/F): ")

    if unit == 'C':
        converted_temperature = convert_to_fahrenheit(temperature)
        print(f"The temperature in Fahrenheit is: {converted_temperature}°F")

    elif unit == 'F':
        converted_temperature = convert_to_celsius(temperature)
        print(f"The temperature in Celsius is: {converted_temperature}°C")

    else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
    
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")

