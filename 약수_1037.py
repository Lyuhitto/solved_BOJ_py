"""
TODO:노션에 적기
"""
import sys


r = sys.stdin.readline


n = int(r())
n_list = sorted(list(map(int, r().split())))
print(n_list[0] * n_list[-1])
