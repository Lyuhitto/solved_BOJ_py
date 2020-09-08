from functools import reduce
'''
print(help(reduce)) 참고
함수형 프로그래밍의 fold라는 개념
reduce(함수, sequence)->값 의 형태
arr = [1,2,3,4]이고 reduce(lambda x, y : x+y, arr)이면
(((1+2)+3)+4)를 수행하는 간단한 함수다
'''


def ujin(n: str) -> str:
    if len(n) <= 1:
        return 'NO'
    for i in range(1, len(n)):
        x = list(map(int, n[:i]))
        y = list(map(int, n[i:]))
        if mul(x) == mul(y):
            return 'YES'
    return 'NO'


def mul(arr: list) -> int:
    return reduce(lambda x, y: x * y, arr)


print(ujin(input()))
