import time


def decomposition(n):
    min_n = 10 if n < 29 else n - len(str(n)) * 9
    for i in range(min_n, n):
        result = i + sum([int(x) for x in str(i)])
        if result == n:
            return i
    return 0


start = time.time()
print(decomposition(int(input())))
print(f"time : {time.time()-start}")
