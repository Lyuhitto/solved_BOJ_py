import sys


r = sys.stdin.readline


# 이분 탐색
n = int(r())
n_list = sorted(list(map(int, r().split())))
m = int(r())
m_list = list(map(int, r().split()))
ans = []

for i in m_list:
    left = 0
    right = n - 1
    is_in = False
    while left <= right:
        mid = (left + right) // 2
        if i == n_list[mid]:
            is_in = True
            break
        elif i < n_list[mid]:
            right = mid - 1
        else:
            left = mid + 1
    ans.append("1" if is_in else "0")

print(" ".join(ans))

# set 사용하기
n = int(r())
n_set = set(map(int, r().split()))
m = int(r())
m_list = list(map(int, r().split()))

for j in m_list:
    print(1 if j in n_set else 0, end=" ")
