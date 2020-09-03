def cmd(n: int) -> str:
    pat = input()
    for _ in range(n-1):
        file = input()
        for i in range(len(pat)):
            if pat[i] != file[i] and pat[i] != '?':
                pat = pat[:i]+'?'+pat[i+1:]
    return pat


print(cmd(int(input())))
