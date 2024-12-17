
def factorial(n):
    """Calculate factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    print(factorial(5))
