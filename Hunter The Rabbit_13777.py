# 기초적인 이진 탐색
def rabbit_binary(rabbit):
    low = 1
    high = 50
    temp = []
    while 1:
        guess = (low + high) // 2
        if guess == rabbit:
            temp.append(str(guess))
            return temp
        elif guess > rabbit:
            temp.append(str(guess))
            high = guess - 1
        else:
            temp.append(str(guess))
            low = guess + 1


while 1:
    n = int(input())
    if n == 0 or n < 1 or n > 50:
        break
    process = rabbit_binary(n)
    print(" ".join(process))
