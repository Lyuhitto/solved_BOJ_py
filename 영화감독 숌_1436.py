'''
브루트포스 알고리즘 사용
'''
n = int(input())
six = 666
count = 0
while 1:
    if '666' in str(six):
        count += 1
    if count == n:
        print(six)
        break
    six += 1
