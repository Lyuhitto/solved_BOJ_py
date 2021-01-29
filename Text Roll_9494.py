# 이진탐색이라곤 하는데, 굳이 그거 안써도 풀리더라
import sys


r = sys.stdin.readline

while 1:
    n = int(input())
    if n == 0:
        break

    temp = []
    for _ in range(n):
        temp.append(r().strip())

    index = 0

    for line in temp:
        is_blank = False
        # 만약 index >= len(line)이면 동작하지 않는다
        for char in range(index, len(line)):
            if line[char] == " ":
                is_blank = True
                index = char
                break
        if not is_blank:
            if index < len(line):
                index += len(line[index:])

    print(index + 1)  # index는 0부터 시작하므로 1을 더한다
