from sys import stdin


que = []
for _ in range(int(input())):
    cmd = list(map(str, stdin.readline().split()))
    if cmd[0] == 'push':
        que.append(cmd[1])
    elif cmd[0] == 'pop':
        print(que.pop(0) if que else -1)
    elif cmd[0] == 'size':
        print(len(que))
    elif cmd[0] == 'empty':
        print(0 if que else 1)
    elif cmd[0] == 'front':
        print(que[0] if que else -1)
    elif cmd[0] == 'back':
        print(que[-1] if que else -1)
    else:
        pass
