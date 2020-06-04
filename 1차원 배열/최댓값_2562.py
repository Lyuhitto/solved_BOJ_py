number_list = []
for i in range(9):
    number_list.append(int(input()))

m = max(number_list)
print(m)
print(number_list.index(m) + 1)
