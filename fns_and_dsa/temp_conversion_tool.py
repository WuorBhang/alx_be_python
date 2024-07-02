# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Example usage:
fahrenheit_temp = 80
celsius_temp = convert_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp}°F is {celsius_temp:.2f}°C")

celsius_temp = 25
fahrenheit_temp = convert_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is {fahrenheit_temp:.2f}°F")


# User Interaction
try:
    temperature = float(input("Enter the temperature: "))
    unit = input("Enter the unit Celsius or Fahrenheit? (C/F): ").strip().upper()

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

