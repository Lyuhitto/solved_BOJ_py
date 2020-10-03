from collections import Counter


'''
N = 홀수, 입력된 수의 갯수
1. 산술평균: (총합) / N
2. 중앙값
3. 최빈값
4. 범위
'''


def get_list() -> list:
    return sorted([int(input()) for _ in range(int(input()))])


def get_average(number: list) -> int:
    return round(sum(number) / len(number))


def get_middle(number: list) -> int:
    return number[0] if len(number) == 1 else number[len(number) // 2]


def get_most_common(number: list) -> int:
    if len(number) == 1:
        return number[0]
    common = Counter(number).most_common(2)
    return common[1][0] if common[0][1] == common[1][1] else common[0][0]


def get_range(number: list) -> int:
    return max(number) - min(number)


n = get_list()
print(get_average(n))
print(get_middle(n))
print(get_most_common(n))
print(get_range(n))
