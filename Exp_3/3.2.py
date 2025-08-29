# Expt 3.2 – Factorial Using Recursion
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print("Factorial:", factorial(5))
