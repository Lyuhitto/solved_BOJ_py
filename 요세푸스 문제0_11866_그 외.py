"""
큐를 사용하지 않은 간략한 풀이법
이중 반복문 대신 while문 하나만 사용한다
이때 리스트의 첫 시작은 항상 0이므로
반드시 idx += (passes - 1)로 해야 한다
"""


def josephus_problem(people: int, passes: int) -> list:
    people_list = [_ for _ in range(1, people + 1)]
    result = []
    idx = 0
    while people_list:
        idx += (passes - 1)
        if idx > len(people_list):
            idx %= len(people_list)
        result.append(str(people_list.pop(idx)))
    return result


n, m = map(int, input().split())
josephus_list = josephus_problem(n, m)
print("<", ", ".join(josephus_list), ">", sep="")
