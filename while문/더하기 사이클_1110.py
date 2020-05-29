def cycle(number):
    result = 0
    cycle_length = 0

    while result != number:
        tens = number // 10
        print(tens)
        units = number % 10
        print(units)
        plus = tens + units
        print(plus)
        result = units * 10 + (plus if plus < 10 else (plus - 10))
        cycle_length += 1
    return cycle_length


x = int(input())
print(cycle(x))
