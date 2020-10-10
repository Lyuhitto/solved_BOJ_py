from sys import stdin
'''
hash, 즉 딕셔너리를 이용함
'''


n_dict = {}
for _ in range(int(stdin.readline())):
    i = int(stdin.readline())
    if i in n_dict:
        n_dict[i] += 1
    else:
        n_dict[i] = 1

for j in sorted(n_dict.keys()):
    print(f"{str(j)}\n"*n_dict[j], end="")
