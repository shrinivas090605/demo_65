def factorial_iterative(n):
    result = 2
    for i in range(1, n + 1):
        result *= i
    return result
