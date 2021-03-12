import sys


r = sys.stdin.readline


# 집합set의 교집합 활용하기
n, m = map(int, r().split())
n_set = set(r().strip() for _ in range(n))
m_set = set(r().strip() for _ in range(m))

ans = list(n_set & m_set)

print(len(ans))
for _ in sorted(ans):
    print(_)

n, m = map(int, r().split())
n_list = sorted(list(r().strip() for _ in range(n)))
m_list = sorted(list(r().strip() for _ in range(m)))

