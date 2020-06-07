import sys

n = int(input())

for i in range(n):
    quiz_list = list(sys.stdin.readline().strip())
    score = 0
    result = 0
    for j in quiz_list:
        if j == "O":
            score += 1
            result += score
        elif j == "X":
            score = 0
        else:
            raise TypeError("This is not O or X")
    print(result)
    result = 0
