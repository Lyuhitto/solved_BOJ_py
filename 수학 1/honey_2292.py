def honey(n):
    n1 = n - 1
    room = 1
    i = 1
    while n1 > 0:
        n1 -= i * 6
        i += 1
        room += 1
    return room


number = int(input())
print(honey(number))
