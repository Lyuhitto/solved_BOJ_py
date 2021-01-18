n = int(input())
if (((n//3) + (n % 3)) % 2) == 1:
    print("SK")
else:
    print("CY")

# 몫+나머지가 홀수면 SK, 짝수면 CY가 된다
# 짧게 줄이면 int(input())%2 and 'SK' or 'CY'
