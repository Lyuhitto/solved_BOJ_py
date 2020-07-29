def find(n):
    end = 1
    plus = 0
    while 1:
        if n <= (end + plus):
            mother = n - plus
            son = end + 1 - mother
            if (end % 2) == 0:
                return f"{mother}/{son}"
            else:
                return f"{son}/{mother}"
        else:
            plus += end
            end += 1


number = int(input())
print(find(number))
