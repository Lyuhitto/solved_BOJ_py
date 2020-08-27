c, k, p = map(int, input().split())
collect = 0
for i in range(1, c + 1):
    collect += (k * i + p * i**2)
print(collect)
