import sys


while 1:
    start, w_or_d, amount = map(str, sys.stdin.readline().strip().split())
    start = int(start)
    amount = int(amount)
    if start == 0 and amount == 0 and w_or_d == 'W':
        break
    elif w_or_d == 'W':
        if (start - amount) < -200:
            print("Not allowed")
            continue
        print(start - amount)
    elif w_or_d == 'D':
        print(start + amount)
