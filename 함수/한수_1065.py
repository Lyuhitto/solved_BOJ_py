"""
한수란? : 각 자리수가 등차수열을 이룰때
2자리 이하의 수는 모두 등차수열을 이루므로 99까지는 모두 한수
3자리 이상의 수는 각각의 자리수를 분리해서 그 숫자들이 등차수열을
이루는지 확인해야함
"""


def get_arithmetic_number(n: int) -> int:
    artimmetic_numbers = 0
    if 1 <= n <= 99:
        return n
    elif 99 < n <= 1000:
        for i in range(100, n + 1):
            n_list = list(map(int, str(i)))
            if n_list[0] - n_list[1] == n_list[1] - n_list[2]:
                artimmetic_numbers += 1
        return 99 + artimmetic_numbers
    else:
        raise ValueError("Out of range.")


n = int(input())
print(get_arithmetic_number(n))
