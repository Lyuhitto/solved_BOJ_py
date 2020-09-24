from sys import stdin


n = int(input())
member_list = [stdin.readline().strip().split() for _ in range(n)]
member_list.sort(key=lambda x: int((x[0])))
for i in range(n):
    print(f"{member_list[i][0]} {member_list[i][1]}")
