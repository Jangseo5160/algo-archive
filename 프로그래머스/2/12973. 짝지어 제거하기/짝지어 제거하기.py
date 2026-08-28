

def solution(s):
    stk = []
    
    for cur in s:
        if len(stk)==0:
            stk.append(cur)
        elif stk[-1] == cur:
            stk.pop()
        else:
            stk.append(cur)
    if len(stk)==0:
        return 1
    else:
        return 0
