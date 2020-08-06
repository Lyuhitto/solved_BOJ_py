def become_a_president():
    test_case = int(input())
    for case in range(test_case):
        k = int(input())
        n = int(input())
        if not(1 <= k <= 14 and 1 <= n <= 14):
            raise ValueError("Invalid Value")
        apartment = [people for people in range(1, n + 1)]
        for floor in range(k):
            for index in range(1, n):
                apartment[index] += apartment[index-1]
        print(apartment[-1])


become_a_president()
