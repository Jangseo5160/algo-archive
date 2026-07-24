from collections import *

def solution(participant, completion):
    answer = ''
    # c = Counter(e for e in completion)
    # p = Counter(e for e in participant)
    # result = (p- c)
    # # print(result)
    # answer = list(result.keys())[0]
    # # print(answer)
    dic = {}
    for e in participant:
        dic[e]= dic.get(e, 0)+1
    
    for a in completion:
        dic[a]-=1
    
    for name in dic:
        if dic[name]>0:
            return name
    
