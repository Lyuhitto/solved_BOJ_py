a, b = map(str, input().split())
a = int(a, 2)
b = int(b, 2)
'''
bin(숫자)을 하면 '0b이진수'의 형태이므로
문자열의 앞을 잘라야한다
'''
print(bin(a + b)[2:])
