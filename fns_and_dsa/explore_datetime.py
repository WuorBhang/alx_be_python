from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in a readable format."""
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(days):
    """Calculate the future date after adding the specified number of days to the current date."""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

def main():
    # Display the current date and time
    display_current_datetime()
    
    # Prompt the user to enter a number of days
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
