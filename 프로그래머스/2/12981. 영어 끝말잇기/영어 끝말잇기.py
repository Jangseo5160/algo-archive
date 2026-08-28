import math
def solution(n, words):
    answer = []
    used = set()
    cnt=0
    
    
    for i in range(len(words)):
        if i ==0:
            used.add(words[i])
            continue
        elif words[i].strip()[0] != words[i-1].strip()[-1] or words[i] in used:
            return [i%n +1, i//n+1]
        used.add(words[i])
    return [0,0]