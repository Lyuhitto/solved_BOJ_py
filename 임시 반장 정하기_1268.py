import sys


n = int(input())
classes = [sys.stdin.readline().split() for _ in range(n)]
cnt = [0]*n

for n in range(n):
    tmp = [False for _ in range(n)]
    for grade in range(5):
        for s_id in range(n):
            if s_id != n and classes[s_id][grade] == classes[n][grade]:
                tmp[s_id] = True
    cnt[n] = sum(tmp)


print(cnt.index(max(cnt)) + 1)
