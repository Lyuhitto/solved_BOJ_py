from sys import stdin, stdout


'''
binary search(이진탐색)을 이용해도 되지만,
그저 존재 유무만 알고 싶으므로 in을 사용함
'''


def get_num_list(number: int) -> list:
    number_list = list(map(int, stdin.readline().strip().split()))
    if len(number_list) != number:
        raise ValueError
    return number_list


n_list = set(get_num_list(int(stdin.readline())))
m_list = get_num_list(int(stdin.readline()))

for val in m_list:
    stdout.write('1\n') if val in n_list else stdout.write('0\n')
