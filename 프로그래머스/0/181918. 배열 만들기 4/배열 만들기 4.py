def solution(arr):
    stk = []
    i=0
    while i < len(arr):
        if stk == []:
            stk.append(arr[i])
            i+=1            
        elif stk[-1]<arr[i]:
            stk.append(arr[i])
            i+=1
        else:
            stk=stk[0:len(stk)-1]
            # stk.pop()
            # stk.remove(stk[-1])
    return stk