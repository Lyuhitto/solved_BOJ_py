numbers = list(filter(lambda x: x % 2 == 1, [int(input()) for _ in range(7)]))
if numbers:
    print(sum(numbers))
    print(min(numbers))
else:
    print(-1)