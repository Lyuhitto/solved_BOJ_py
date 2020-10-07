"""
최대공약수 Greatest Common Divisor (r = a % b)
GCD(a, b) = GCD(b, r)의 재귀함수로 나타낼 수 있다

최소공배수 Least Common Multiple (g = GCD(a, b))
LCM l = g * (a / g) * b(b / g)
"""


def get_gcd(a: int, b: int) -> int:
    return a if b == 0 else get_gcd(b, a % b)


def get_lcm(a: int, b: int, g: int) -> int:
    return g * (a // g) * (b // g)


a, b = map(int, input().split())
gcd = get_gcd(a, b)
lcm = get_lcm(a, b, gcd)
print(f"{gcd}\n{lcm}")
