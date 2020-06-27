import string


def word_location(word):
    alphabet = list(string.ascii_lowercase)
    alphabet_location = [-1 for i in range(len(alphabet))]
    set_word = list(set(word))
    for w in set_word:
        location = word.index(w)
        alphabet_location[alphabet.index(w)] = location
    for l in alphabet_location:
        print(l, end=" ")

a = input()
word_location(a)
