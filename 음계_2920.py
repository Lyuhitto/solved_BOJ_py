import sys


def musical_scales(number: int) -> str:
    diff = number[0] - number[1]
    for idx in range(1, len(number)-1):
        diff_tmp = number[idx] - number[idx + 1]
        if diff != diff_tmp:
            return 'mixed'
    return 'ascending' if diff < 0 else 'descending'


n_list = list(map(int, sys.stdin.readline().strip().split()))
print(musical_scales(n_list))
