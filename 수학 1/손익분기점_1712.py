import sys


def get_break_even_point(fixed_cost, variable_cost, income: int):
    if variable_cost >= income:
        print(-1)
    else:
        print(int(fixed_cost/(income-variable_cost))+1)


a, b, c = map(int, sys.stdin.readline().strip().split())
get_break_even_point(a, b, c)
