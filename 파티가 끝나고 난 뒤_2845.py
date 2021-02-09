import sys


r = sys.stdin.readline


l, p = map(int, r().split())
n_list = list(map(int, r().split()))
result = list(str(i - (l*p)) for i in n_list)
print(" ".join(result))
