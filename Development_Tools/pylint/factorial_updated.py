
"""
This module contains a function to calculate the factorial of a number.
It also includes a main function that demonstrates the calculation with an example.
"""

def calculate_factorial(n):
    """ 
    Calculate the factorial of a number.
    
    Args:
    n (int): The number to calculate the factorial for.
    
    Returns:
    int: The factorial of the input number.
    """
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)  # Remove the unnecessary 'else'

def main():
    """
    Main function to demonstrate the factorial calculation.
    """
    print(calculate_factorial(5))

if __name__ == "__main__":
    main()
