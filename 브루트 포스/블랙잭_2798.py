import sys


def black_jack():
    n, m = map(int, input().split())
    jack = list(map(int, sys.stdin.readline().strip().split()))
    if len(jack) != n:
        raise ValueError(f"Your list length is not {n}")
    result = 0
    tmp = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                tmp = jack[i] + jack[j] + jack[k]
                if tmp > m:
                    continue
                if abs(m - result) > abs(m - tmp):
                    result = tmp
    print(result)


black_jack()

'''
카드가 3장이므로 for문도 3개가 필요하다.
'''
