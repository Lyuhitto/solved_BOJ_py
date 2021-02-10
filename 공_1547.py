import sys


r = sys.stdin.readline


cup = [1, 2, 3]
for _ in range(int(r())):
    x, y = map(int, r().split())
    xi = cup.index(x)
    yi = cup.index(y)

    cup[xi], cup[yi] = cup[yi], cup[xi]

print(cup[0] if cup[0] else -1)
