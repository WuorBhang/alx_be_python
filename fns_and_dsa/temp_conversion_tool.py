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
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Ensure this line is present

def get_temperature_and_unit():
    """Gets temperature and unit from user input."""
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit not in ['C', 'F']:
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
        return temperature, unit
    except ValueError as e:
        print(f"Error: {e}")
        return None, None

# User Interaction
def main():
    while True:
        temperature, unit = get_temperature_and_unit()
        if temperature is None or unit is None:
            continue
        
        if unit == 'C':
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"The temperature in Fahrenheit is: {converted_temperature}°F")
        elif unit == 'F':
            converted_temperature = convert_to_celsius(temperature)
            print(f"The temperature in Celsius is: {converted_temperature}°C")
        
        if input("Do you want to convert another temperature? (yes/no): ").strip().lower() != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
