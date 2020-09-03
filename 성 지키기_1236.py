'''
가로와 세로에서 X가 없는 경우를 더한 뒤, 둘 중 제일 큰수가 정답이다
'''

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
