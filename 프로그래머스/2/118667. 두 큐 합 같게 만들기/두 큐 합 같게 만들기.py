# 그리디 + 큐
from collections import deque
def solution(queue1, queue2):
    answer = -2
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    if (sum1 + sum2) %2 ==1:
        return -1
    cnt=0
    n=len(queue1)
    while cnt<4*n:
        if sum1 == sum2:
            return cnt
        
        elif sum1>sum2:
            value = q1.popleft()
            q2.append(value)
            sum1-=value
            sum2+=value
            
        elif sum1<sum2:
            value = q2.popleft()
            q1.append(value)
            sum2-=value
            sum1+=value
            
        cnt+=1
    
    return -1