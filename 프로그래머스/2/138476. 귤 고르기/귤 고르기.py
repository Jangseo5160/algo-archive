from collections import Counter
def solution(k, tangerine):
    answer=0
    cnts = Counter(tangerine)
    
    cnts = sorted(cnts.values(), reverse=True)
    for c in cnts:
        k-=c
        answer+=1
        
        if k<=0:
            return answer