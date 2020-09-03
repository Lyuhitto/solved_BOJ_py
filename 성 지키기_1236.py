n, m = map(int, input().split())
castle = [list(input()) for i in range(n)]
row = 0
col = 0
for i in range(n):
    if 'X' not in castle[i]:
        row += 1
for j in range(m):
    if 'X' not in [castle[i][j] for i in range(n)]:
        col += 1
print(max(row, col))
