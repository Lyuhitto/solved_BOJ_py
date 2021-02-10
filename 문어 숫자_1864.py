import sys


r = sys.stdin.readline


octopus_numbers = {
    "-": 0, "\\": 1, "(": 2,
    "@": 3, "?": 4, ">": 5,
    "&": 6, "%": 7, "/": -1
    }

while 1:
    number = list(r().strip())
    if "#" in number:
        break
    result = 0
    number_len = len(number) - 1
    for n in number:
        result += 8 ** number_len * octopus_numbers[n]
        number_len -= 1
    print(result)
