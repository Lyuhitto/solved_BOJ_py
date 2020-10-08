from sys import stdin


deq = []
for i in range(int(stdin.readline())):
    cmd = stdin.readline().strip().split()
    if cmd[0] == 'push_front':
        deq.insert(0, cmd[1])
    elif cmd[0] == 'push_back':
        deq.append(cmd[1])
    elif cmd[0] == 'pop_front':
        print(deq.pop(0) if deq else -1)
    elif cmd[0] == 'pop_back':
        print(deq.pop() if deq else -1)
    elif cmd[0] == 'size':
        print(len(deq))
    elif cmd[0] == 'empty':
        print(0 if deq else 1)
    elif cmd[0] == 'front':
        print(deq[0] if deq else -1)
    elif cmd[0] == 'back':
        print(deq[-1] if deq else -1)
    else:
        print('invalid value')
