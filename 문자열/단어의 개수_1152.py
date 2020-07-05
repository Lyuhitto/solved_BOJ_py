import sys


def word_counter(sentence):
    word_list = sentence.split()
    print(len(word_list))


a = sys.stdin.readline()
word_counter(a)