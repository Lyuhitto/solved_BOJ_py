'''
스택에 '(' 만 넣는다

"NO"가 되는 경우:
    1. 모든 문자열을 검사했는데 스택이 비어있지 않을 경우
    2. ')'를 만나 pop을 해야하는데 스택이 비어있는 경우
'''


def check_VPS(ps: str) -> str:
    ps_stack = []
    for w in ps:
        if w == '(':
            ps_stack.append(w)
        else:
            if not ps_stack:
                return "NO"
            ps_stack.pop()
    if ps_stack:
        return "NO"
    return "YES"


for _ in range(int(input())):
    ps = input()
    print(check_VPS(ps))
