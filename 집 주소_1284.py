import sys


r = sys.stdin.readline


while 1:
    n = str(r().strip())
    if n == '0' or not n.isdigit():
        break
    n_list = list(n)
    result = 1
    for number in n_list:
        if number == '1':
            result += 3
        elif number == '0':
            result += 5
        else:
            result += 4
    print(result)
