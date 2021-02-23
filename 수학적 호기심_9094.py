import sys


r = sys.stdin.readline

for _ in range(int(r())):
    n, m = map(int, r().split())
    count = 0
    for a in range(1, n):
        for b in range(a + 1, n):
            temp = (a**2 + b**2 + m) / (a*b)
            if temp - int(temp) == 0:
                count += 1
    print(count)
