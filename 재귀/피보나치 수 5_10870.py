def fibonacci_5(n):
    if n < 2:
        return n
    return fibonacci_5(n-1) + fibonacci_5(n-2)

print(fibonacci_5(int(input())))