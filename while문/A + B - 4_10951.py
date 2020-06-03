import sys

while 1:
    try:
        a, b = map(int, sys.stdin.readline().strip().split())
    except EOFError:
        break
    print(a + b)
