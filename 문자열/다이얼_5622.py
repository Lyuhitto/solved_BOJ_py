def calc_dial(number: str):
    dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    result = 0
    for n in number:
        for index, value in enumerate(dial):
            if n in value:
                result += (index + 3)
    print(result)


number = input()
calc_dial(number)
