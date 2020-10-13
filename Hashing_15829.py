'''
해시 함수란 임의의 길이의 입력을 받아
고정된 길이의 출력을 내보내는 함수이다
ord()는 입력된 문자를 숫자로 변환시킨다
이때 문자는 무조건 소문자이므로 96을 뺀다
'''


L = int(input())
line = input()
result = 0

for i in range(L):
    result += (ord(line[i]) - 96) * (31 ** i)

print(result % 1234567891)
