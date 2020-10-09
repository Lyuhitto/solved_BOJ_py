from sys import stdin
'''
해시 구조(줄여서 해시-hash)란?
파이썬에서 딕셔너리에 해당한다
key값을 이름표 삼아 데이터를 저장하는 구조
'''


def get_list() -> list:
    number = int(input())
    number_list = list(map(int, stdin.readline().split()))
    if len(number_list) != number:
        raise ValueError('Invalid value')
    return number_list


n_list = get_list()
m_list = get_list()

hash_map = {}
for n in n_list:
    if n in hash_map:
        hash_map[n] += 1
    else:
        hash_map[n] = 1

print(" ".join(str(hash_map[m]) if m in hash_map else '0' for m in m_list))
