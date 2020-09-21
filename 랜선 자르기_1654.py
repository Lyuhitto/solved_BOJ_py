import sys


def cut_lan(k: int, n: int, lan_list: list) -> int:
    low_len = 1
    high_len = max(lan_list)
    while low_len <= high_len:
        cnt = 0
        mid_len = (low_len + high_len) // 2
        for lan in lan_list:
            cnt += lan // mid_len
        if cnt >= n:
            low_len = mid_len + 1
        else:
            high_len = mid_len - 1
    return high_len


def get_lan(k: int) -> list:
    lst = []
    for _ in range(k):
        lst.append(int(sys.stdin.readline()))
    return lst


k, n = map(int, sys.stdin.readline().split())
o_lan = get_lan(k)
print(cut_lan(k, n, o_lan))
