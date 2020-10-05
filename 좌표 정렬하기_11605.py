coordinate = [list(map(int, input().split())) for _ in range(int(input()))]
for val in sorted(coordinate, key=lambda x: (x[0], x[1])):
    print(val[0], val[1])
