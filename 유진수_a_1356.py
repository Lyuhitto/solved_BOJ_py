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
    result = 1
    for i in arr:
        result *= i
    return result


print(ujin(input()))
