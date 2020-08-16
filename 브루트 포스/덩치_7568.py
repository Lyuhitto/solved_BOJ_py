people = [list(map(int, input().split())) for row in range(int(input()))]
solve = ""
for i in people:
    rank = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    solve += str(rank)+' '
print(solve)

'''
단순하게 자기 자신보다 큰 만큼 rank를 늘린다
'''
