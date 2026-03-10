def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b


def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b


def divide(a, b):
    """Divide a by b and return the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


def power(base, exponent):
    """Calculate base raised to the power of exponent."""
    return base**exponent


def square_root(number):
    """Calculate the square root of a number."""
    if number < 0:
        raise ValueError("Cannot calculate square root of negative number!")
    return number**0.5


# Example usage
if __name__ == "__main__":
    # Test basic operations
    print("Basic Math Operations:")
    print(f"Addition: 5 + 3 = {add(5, 3)}")
    print(f"Subtraction: 10 - 4 = {subtract(10, 4)}")
    print(f"Multiplication: 6 * 7 = {multiply(6, 7)}")
    print(f"Division: 15 / 3 = {divide(15, 3)}")

    # Test advanced operations
    print("\nAdvanced Math Operations:")
    print(f"Power: 2^3 = {power(2, 3)}")
    print(f"Square root of 16 = {square_root(16)}")

    # Example with error handling
    try:
        print("\nError Handling Example:")
        print(divide(10, 0))
    except ValueError as e:
        print(f"Error: {e}")
