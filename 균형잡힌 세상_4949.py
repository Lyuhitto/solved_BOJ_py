from sys import stdin


while 1:
    line = stdin.readline().rstrip()
    if line == '.':
        break
    que = []
    is_true = True
    for w in line:
        if w in '([':
            que.append(w)
        if w in ')]':
            if que:
                if w == ')' and que[-1] == '(':
                    que.pop()
                elif w == ']' and que[-1] == '[':
                    que.pop()
                else:
                    is_true = False
                    break
            else:
                is_true = False
                break
    print("yes" if not que and is_true else "no")
