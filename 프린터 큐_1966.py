from sys import stdin


for _ in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    que = list(map(int, stdin.readline().split()))
    for idx, val in enumerate(que):
        if idx == m:
            que[idx] = [val, True]
        else:
            que[idx] = [val, False]

    order = 0
    while True:
        if que[0][0] == max(que)[0]:
            order += 1
            if que[0][1] is True:
                print(order)
                break
            else:
                que.pop(0)
        else:
            que.append(que.pop(0))
