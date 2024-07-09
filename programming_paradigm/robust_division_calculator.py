def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Both inputs must be numeric."

# Test cases
if __name__ == "__main__":
    print(safe_divide(10, 2))  # Should print: Result: 5.0
    print(safe_divide(10, 0))  # Should print: Error: Division by zero is not allowed.
    print(safe_divide(10, 'a'))  # Should print: Error: Both inputs must be numeric.
    print(safe_divide('x', 2))  # Should print: Error: Both inputs must be numeric.
    print(safe_divide(10, 3))
