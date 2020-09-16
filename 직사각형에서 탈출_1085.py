import sys


std_input = sys.stdin.readline().strip().split()


"""
n = [x, y, w, h]
result = [|(0-x)|, (w-x), |(0-y)|, (h-y)]
"""


def escape_from_square(n: list) -> int:
    result = []
    for i in range(2):
        result.append(abs(0 - n[i]))
        result.append(n[i+2]-n[i])
    return min(result)


n_list = list(map(int, std_input))
print(escape_from_square(n_list))
