import sys


def distribute(n1, n2):
    a = n1 % 10
    if a == 1 or a == 5 or a == 6:
        return a
    elif a == 0:
        return 10
    elif a == 2:
        temp = [2, 4, 8, 6]
        return temp[n2 % 4 - 1]
    elif a == 3:
        temp = [3, 9, 7, 1]
        return temp[n2 % 4 - 1]
    elif a == 4:
        return 4 if n2 % 2 == 1 else 6
    elif a == 7:
        temp = [7, 9, 3, 1]
        return temp[n2 % 4 - 1]
    elif a == 8:
        temp = [8, 4, 2, 6]
        return temp[n2 % 4 - 1]
    elif a == 9:
        return 9 if n2 % 2 == 1 else 1


r = sys.stdin.readline

for _ in range(int(r())):
    a, b = map(int, r().split())
    print(distribute(a, b))
