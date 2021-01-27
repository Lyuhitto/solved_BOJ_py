import sys


r = sys.stdin.readline


rect = [[0] * 100 for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, r().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            rect[i][j] = 1

result = 0
for row in rect:
    result += sum(row)
print(result)
