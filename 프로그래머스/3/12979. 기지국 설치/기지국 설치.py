import math

def solution(n, stations, w):
    answer = 0
    cover = 2*w+1
    start = 1
    for s in stations:
        left = s-w
        right = s+w
        if start < left:
            answer += math.ceil((left - start)/cover)
            
        start = right + 1
    
    if start <=n:
        answer += math.ceil((n-start+1)/cover)
        
    return answer