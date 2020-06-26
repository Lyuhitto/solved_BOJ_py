import sys


def get_line():
    n = int(input())
    line = list(map(int, sys.stdin.readline(n)))
    return line


def sum_numbers(line):
    result = sum(line)
    return result


a = get_line()
print(sum_numbers(a))
