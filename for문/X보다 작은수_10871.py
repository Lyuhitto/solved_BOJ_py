import sys


n, x = map(int, sys.stdin.readline().strip().split())
number = list(map(int, sys.stdin.readline().strip().split()))
result = []

for i in number:
    if i < x:
        assert type(i) is int, '정수 아님'
        result.append(i)
for i in result:
    assert type(i) is int, '정수 아님'
    print(i, end=' ')
