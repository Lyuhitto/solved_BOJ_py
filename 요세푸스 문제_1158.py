n, k = map(int, input().split())
n_list = [i + 1 for i in range(n)]
josep_que = []
num = 0
for i in range(n):
    num += k - 1
    if num >= len(n_list):
        num = num % len(n_list)
    josep_que.append(str(n_list.pop(num)))
print("<", ", ".join(josep_que), ">", sep="")
