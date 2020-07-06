def anwser_of_sangsu(n1, n2: int):
    if n1 == n2:
        raise ValueError("n1 and n2 have the same value")
    n1 = int(str(n1)[::-1])
    n2 = int(str(n2)[::-1])
    if n1 > n2:
        print(n1)
    else:
        print(n2)


n1, n2 = map(int, input().split())
anwser_of_sangsu(n1, n2)
