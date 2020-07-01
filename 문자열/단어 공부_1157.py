def most_used_alphabet(word):
    upper_word = word.upper()
    set_word = set(upper_word)
    max_num = 0
    num = 0
    duplicate = 0
    result = ""
    for alphabet in set_word:
        num = upper_word.count(alphabet)
        if num > max_num:
            max_num = num
            duplicate = 0
            result = alphabet
        elif num == max_num:
            duplicate += 1
    if duplicate != 0:
        print("?")
    else:
        print(result)


example = input()
most_used_alphabet(example)
