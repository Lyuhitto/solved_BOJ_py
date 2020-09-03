'''
첫번째수를 패턴으로 정하고,
다른 숫자들과 비교해서
일치하지 않으면 '?'로 바꾼다
'''
def cmd(n: int) -> str:
    pat = input()
    for _ in range(n-1):
        file = input()
        for i in range(len(pat)):
            if pat[i] != file[i] and pat[i] != '?':
                pat = pat[:i]+'?'+pat[i+1:]
    return pat


print(cmd(int(input())))
