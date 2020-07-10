def suger_delivery(delivery: int):
    if delivery % 5 == 0:
        return delivery//5
    five = delivery // 5
    three = 0
    suger = delivery % 5
    while five >= 0:
        if suger % 3 == 0:
            three = suger//3
            suger %= 3
            break
        five -= 1
        suger += 5
    return suger == 0 and (five+three) or -1


delivery = int(input())
print(suger_delivery(delivery))
