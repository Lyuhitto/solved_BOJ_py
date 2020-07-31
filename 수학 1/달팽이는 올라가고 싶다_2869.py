def snail_can_go_up(A, B, V):
    if not(B < A or A <= V):
        raise ValueError("These are not B<A and A<=V")
    day = (V-B)/(A-B)
    return int(day) if day == int(day) else int(day) + 1


a, b, v = map(int, input().split())
print(snail_can_go_up(a, b, v))
