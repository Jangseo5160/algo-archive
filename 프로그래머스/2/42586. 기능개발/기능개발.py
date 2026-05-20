import math

def solution(progresses, speeds):
    answer = []
    day=[]
        
    for i in range(len(progresses)):
        day.append(math.ceil((100-progresses[i])/speeds[i]))
            
    stk=[]
    answer=[]
    
    for i in day:
        if stk and stk[0] < i:
            answer.append(len(stk))
            stk.clear()
            
        stk.append(i)
            
    if stk:
        answer.append(len(stk))
        
    return answer