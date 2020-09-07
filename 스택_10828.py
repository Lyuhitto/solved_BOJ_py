import sys


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.stack:
            pop_n = self.stack[-1]
            del self.stack[-1]
            return pop_n
        else:
            return -1

    def size(self):
        return len(self.stack)

    def empty(self):
        return 1 if not self.stack else 0

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1


stack = Stack()
for i in range(int(input())):
    cmd = sys.stdin.readline().strip().split()
    if cmd[0] == 'push':
        stack.push(cmd[1])
    elif cmd[0] == 'pop':
        print(stack.pop())
    elif cmd[0] == 'size':
        print(stack.size())
    elif cmd[0] == 'empty':
        print(stack.empty())
    elif cmd[0] == 'top':
        print(stack.top())
    else:
        print('Invalid command')
