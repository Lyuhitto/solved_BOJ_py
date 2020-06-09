def get_self_number(n: int) -> int:
    original_set = set(range(1, n + 1))
    generated_set = set()
    for i in range(1, n + 1):
        n_list = list(map(int, str(i)))
        not_self_number = i + sum(n_list)
        generated_set.add(not_self_number)
    self_number_set = original_set - generated_set
    for i in sorted(self_number_set):
        print(i)


get_self_number(10000)
