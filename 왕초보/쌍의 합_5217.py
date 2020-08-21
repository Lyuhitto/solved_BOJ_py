for i in range(int(input())):
    n = int(input())
    n_list = []
    if n > 12:
        raise ValueError("Invalid value!")
    for n1 in range(1, (n // 2 + 1)):
        n2 = n - n1
        if n1 != n2:
            n_list.append(f'{n1} {n2}')
    print(f"Pairs for {n}: {', '.join(n_list)}")
