def solution(citations):
    answer = 0
    
    n= len(citations)
    
    citations.sort(reverse=True)
    
    for i in range(n):
        if citations[i] < i+1:
            return i
        
    return n

# 6 5 4 1 0
# i=6, a = 6 -> 5 -> 4