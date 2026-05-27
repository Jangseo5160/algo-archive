def solution(number, k):
    answer = ''
    stk=[]
    for num in number:
        while k>0 and stk and stk[-1]<num:
            stk.pop()
            k-=1
        stk.append(num)
        
    if k>0:
        stk=stk[:-k]
        
    return ''.join(stk)

