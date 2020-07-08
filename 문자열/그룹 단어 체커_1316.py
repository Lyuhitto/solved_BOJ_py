n = int(input())
result = 0
for i in range(n):
    word = input()
    result += list(word) == sorted(word, key=word.find)
print(result)
