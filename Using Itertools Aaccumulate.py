from itertools import accumulate

def factorial_accumulate(n):
    return list(accumulate(range(1, n + 1)))[-1]

# Example usage:
number = 5
fact = factorial_accumulate(number)
print("Factorial of", number, "is", fact)
