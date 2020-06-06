import sys

n = int(input())
subjects = list(map(int, sys.stdin.readline().strip().split()))

print(sum(subjects) / max(subjects) * 100 / n)
