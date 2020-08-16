import sys

three = list(map(int, sys.stdin.readline().strip().split()))
for i in sorted(three):
    print(i, end=" ")
