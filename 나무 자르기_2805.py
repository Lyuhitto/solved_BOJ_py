import sys


n, m = map(int, sys.stdin.readline().split())
tree_list = list(map(int, sys.stdin.readline().split()))
cut_min = 1
cut_max = max(tree_list)

while cut_min <= cut_max:
    get_tree = 0
    cut_mid = (cut_min + cut_max) // 2
    for tree in tree_list:
        if tree > cut_mid:
            get_tree += (tree - cut_mid)
    if get_tree >= m:
        cut_min = cut_mid + 1
    else:
        cut_max = cut_mid - 1

print(cut_max)
