# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius."""
    return ((fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR)

def convert_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32)

def main():
    try:
        # Prompt the user to enter a temperature
        temperature_input = input("Enter the temperature to convert: ").strip()
        
        # Check if the input is a valid number
        if not temperature_input.replace('.', '', 1).isdigit() and not temperature_input.replace('-', '', 1).replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        temperature = float(temperature_input)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature:.1f}°F is {converted_temperature:.2f}°C")
        elif unit == 'C':
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}°C is {converted_temperature:.2f}°F")
        else:
            raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")
    
    except ValueError as e:
        print(f"Error: {e}")
