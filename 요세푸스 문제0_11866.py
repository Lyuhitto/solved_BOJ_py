def josephus_problem(people: list, passes: int) -> list:
    result = []
    while people:
        for i in range(passes - 1):
            people.append(people.pop(0))
        result.append(str(people.pop(0)))
    return result


n, m = map(int, input().split())
josephus_list = josephus_problem([(i + 1) for i in range(n)], m)
print("<", ", ".join(josephus_list), ">", sep="")
