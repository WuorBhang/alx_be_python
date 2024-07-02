# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Conversion functions
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# User interaction
try:
    temperature = float(input("Enter the temperature: "))
    unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ")

    if unit.upper() == "C":
        converted_temperature = convert_to_fahrenheit(temperature)
        print(f"The temperature {temperature}°C is equivalent to {converted_temperature}°F.")
    elif unit.upper() == "F":
        converted_temperature = convert_to_celsius(temperature)
        print(f"The temperature {temperature}°F is equivalent to {converted_temperature}°C.")
    else:
        raise ValueError("Invalid temperature unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
