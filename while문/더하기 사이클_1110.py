n = int(input())
a = n
cycle_length = 0

while a != n or cycle_length == 0:
    units = a % 10
    ten = a // 10
    value = (units + ten) % 10
    a = units * 10 + value
    cycle_length += 1

print(cycle_length)
