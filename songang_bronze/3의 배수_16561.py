def get_3n(n):
    if n < 9:
        return 0
    num = 1
    count = 2
    for i in range(9, n, 3):
        num += count
        count += 1
    return num


print(get_3n(int(input())))
