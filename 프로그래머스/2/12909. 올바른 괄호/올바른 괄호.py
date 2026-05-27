def solution(s):
    stk=[]
    for a in s:
        if a == "(":
            stk.append(a)
        elif a==")":
            if stk == []:
                return False
            elif stk[-1]=="(":
                stk.pop()
    if stk == []:
        return True
    else:
        return False