import sys


n1, n2, n3, n4, n5 = map(int, sys.stdin.readline().strip().split())
print((n1**2+n2**2+n3**2+n4**2+n5**2) % 10)
