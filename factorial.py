def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
num = 5
print(f"Factorial of {num} (iterative):", factorial_iterative(num))
