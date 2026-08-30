def solution(s):
    answer = 0
    i=0
    while i<len(s):
        if i!=0:
            ch = s[0]
            s = s[1:] + ch
        
        stk = []
        possible = True
        for c in s:
            if c == "}":
                if stk and stk[-1] == "{":
                    stk.pop()
                else:
                    possible = False
                    break
            elif c == ")":
                if stk and stk[-1] == "(":
                    stk.pop()
                else:
                    possible = False
                    break
            elif c == "]":
                if stk and stk[-1] == "[":
                    stk.pop()
                else:
                    possible = False
                    break
            elif c == "{" or c == "(" or c == "[":
                stk+=c
        if possible and len(stk)==0:
            answer+=1
        i+=1
    return answer