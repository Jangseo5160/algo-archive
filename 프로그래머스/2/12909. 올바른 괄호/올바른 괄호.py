def solution(s):
    answer = True
    stk = []
    for c in s:
        if c == "(":
            stk.append(c)
        elif c == ")":
            if not stk:
                return False
            else:
                stk.pop()
        
    if len(stk) == 0:
        return True
    else:
        return False