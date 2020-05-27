def cycle(number) :
    x = number
    result = 0
    cycle_lenght = 0
    while result == number :
        units = x % 10
        tens = x // 10
        plus = units + tens
        result = units * 10 + plus if plus < 10 else (plus - 10)
        cycle_lenght += 1
    return cycle_lenght

x = int(input())
print(cycle(x))