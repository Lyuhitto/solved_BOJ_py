"""
이항 계수란 N개가 있을 때 k개를 고를 경우의 수다
수식으로 나타낸다면 n! / k!(n-k)!
"""
'''
def factorial(n):
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans
'''


from math import factorial as f


n, k = map(int, input().split())
print(0 if k < 0 or k > n else int(f(n) / (f(k)*f(n-k))))
