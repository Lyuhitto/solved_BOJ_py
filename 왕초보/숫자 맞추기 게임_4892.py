i = 1
while 1:
    n0 = int(input())
    if n0 == 0:
        break
    n1 = 3*n0
    even_or_odd = ''
    if n1 % 2 == 0:
        even_or_odd = 'even'
    elif n1 % 2 == 1:
        even_or_odd = 'odd'
    n2 = (n1+1)/2
    n3 = 3*n2
    n4 = n3/9
    print(f"{i}. {even_or_odd} {int(n4)}")
    i += 1
