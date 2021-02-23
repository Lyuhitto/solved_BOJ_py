import sys


r = sys.stdin.readline


numbers = []
for _ in range(9):
    numbers.append(list(map(int, r().split())))
max_n = 0
max_location = 0

for i in range(9):
    if max_n < max(numbers[i]):
        max_n = max(numbers[i])
        max_location = [i + 1, numbers[i].index(max_n) + 1]

print(max_n)
print(f"{max_location[0]} {max_location[1]}")
