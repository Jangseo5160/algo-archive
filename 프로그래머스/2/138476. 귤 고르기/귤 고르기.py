def solution(k, tangerine):
    answer = 0
    tangerine.sort()
    total = {}
    for key in tangerine:
        total[key] = total.get(key,0) +1
    
    total = sorted(total.items(), key=lambda x: x[1], reverse = True)
    
    for i in range(len(total)):
        if k<=0:
            return answer
        else:
            k-=total[i][1]
            answer+=1
    
    return answer