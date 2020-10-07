def get_jemin_sum(jemin_list: list) -> int:
    stack = []
    for i in jemin_list:
        if i == 0:
            stack.pop()
        else:
            stack.append(i)
    return sum(stack)


jemin = [int(input()) for _ in range(int(input()))]
print(get_jemin_sum(jemin))
