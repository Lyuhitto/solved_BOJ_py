"""
직각삼각형
c ** 2 = (a ** 2 + b ** 2) ** 0.5 
   /|
c / | a
 /  |
 ----
  b
"""


while 1:
    n = sorted(list(map(int, input().split())))
    if sum(n) == 0:
        break
    print('right' if n[2] == (n[0] ** 2 + n[1] ** 2) ** 0.5 else 'wrong')
