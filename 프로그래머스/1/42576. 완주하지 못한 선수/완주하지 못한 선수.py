from collections import *

def solution(participant, completion):
    answer = ''
    c = Counter(e for e in completion)
    p = Counter(e for e in participant)
    result = (p- c)
    # print(result)
    answer = list(result.keys())[0]
    # print(answer)
    return answer