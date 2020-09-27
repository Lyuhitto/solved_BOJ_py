"""
큐의 원리(FIFO, 선입선출)로 한쪽 끝에서 넣고 다른 한쪽에서 빼는
연산을 이용함
"""


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
