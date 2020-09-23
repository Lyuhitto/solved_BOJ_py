def prime(n):
    if n == 1:
        return False
    prime_list = (2, 3, 5, 7, 11)
    if n in prime_list:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = int(input())
n_list = list(map(int, input().split()))
count = 0
for i in n_list:
    if prime(i):
        count += prime(i)
print(count)
