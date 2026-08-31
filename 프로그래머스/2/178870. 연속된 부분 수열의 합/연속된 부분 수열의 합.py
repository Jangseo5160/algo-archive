# 투포인터, end를 기준으로 start를 조정하면서 진행
def solution(sequence, k):
    answer = [0, len(sequence)-1]
    value = 0
    start, end = 0,0 
    min_length = len(sequence)
    
    for end in range(len(sequence)):
        value += sequence[end]
        while value>k:
            value-= sequence[start]
            start+=1
        if value==k:
            length = end-start+1
            
            if min_length > length:
                min_length = length
                answer = [start, end]
            
    return answer