import sys


# 2차원 배열로 풀기
r = sys.stdin.readline
n, k = map(int, r().split())  # n = 물건의 개수, k = 배낭의 무게
item = [[0, 0]]
for _ in range(n):
    item.append(list(map(int, r().split())))

bag = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= item[i][0]:
            bag[i][j] = max(bag[i-1][j], bag[i-1][j-item[i][0]] + item[i][1])
        else:
            bag[i][j] = bag[i-1][j]

print(bag[n][k])


# 1차원 배열로 풀기
n, k = map(int, r().split())
item = [list(map(int, r().split())) for _ in range(n)]
bag = [0 for _ in range(k + 1)]

for i in range(n):
    for j in range(k, 1, -1):
        if j >= item[i][0]:
            bag[j] = max(bag[j], bag[j-item[i][0]] + item[i][1])
#        print(bag)

print(bag[k])
