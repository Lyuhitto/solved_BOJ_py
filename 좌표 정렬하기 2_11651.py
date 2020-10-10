n = [list(map(int, input().split())) for _ in range(int(input()))]
for val in sorted(n, key=lambda x: (x[1], x[0])):
    print(val[0], val[1])
