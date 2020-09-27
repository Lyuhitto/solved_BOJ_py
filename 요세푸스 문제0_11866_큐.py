"""
큐의 원리(FIFO, 선입선출)로 한쪽 끝에서 넣고 다른 한쪽에서 빼는
연산을 이용함
"""


def josephus_problem(people: int, passes: int) -> list:
    people_list = [(_ + 1) for _ in range(people)]
    result = []
    while people_list:
        for i in range(passes - 1):
            people_list.append(people_list.pop(0))
        result.append(str(people_list.pop(0)))
    return result


n, m = map(int, input().split())
josephus_list = josephus_problem(n, m)
print("<", ", ".join(josephus_list), ">", sep="")
