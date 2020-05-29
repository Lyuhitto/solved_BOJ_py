import sys

n = int(input())
number_list = list(map(int, sys.stdin.readline().strip().split()))
list_max = max(number_list)
list_min = min(number_list)

print("%d %d" % (list_min, list_max))
