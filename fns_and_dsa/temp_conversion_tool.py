#checking the definition of global convertor temperature
def convert_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# User Interaction
def main():
    while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

            if unit == 'C':
                converted_temperature = convert_to_fahrenheit(temperature)
                print(f"The temperature in Fahrenheit is: {converted_temperature}°F")

            elif unit == 'F':
                converted_temperature = convert_to_celsius(temperature)
                print(f"The temperature in Celsius is: {converted_temperature}°C")

            else:
                raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

