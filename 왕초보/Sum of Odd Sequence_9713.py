for i in range(int(input())):
    n = int(input())
    result = 0
    for j in range(1, n+1):
        if j % 2 == 1:
            result += j
    print(result)
