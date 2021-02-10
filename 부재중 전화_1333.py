n, l, d = map(int, input().split())
time = 0
answer = d
get_call = False
"""
모든 시간은 0초 부터 시작하는데, 이때 많이 헷갈린다
예를들어 l이 15초라면 노래는 0-14초, 20-34초동안 들리게되고
정답은 35가 된다
"""
for _ in range(n):
    if time <= answer < time + l:
        while answer < time + l:
            answer += d
    if l + time <= answer < time + l + 5:
        get_call = True
        break
    time += l + 5

if not get_call:
    while answer - 5 < time:
        answer += d
print(answer)
