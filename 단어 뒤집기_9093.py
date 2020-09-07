import sys


'''
스택을 활용한 문제 풀이
'''


def reverse_word(sentence: str) -> str:
    result = ''
    stack = []
    for w in sentence:
        if w == ' ' or w == '\n':
            while stack:
                result += stack.pop()
            result += ' '
        else:
            stack.append(w)
    return result


for i in range(int(input())):
    print(reverse_word(sys.stdin.readline()))
