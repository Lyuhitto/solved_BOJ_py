def string_iteration():
    n = int(input())
    i = 0
    while i < n:
        string = input()
        time = int(string[0])
        for word in string[2:]:
            print(word * time, end="")
        print()  
        i += 1

string_iteration()
