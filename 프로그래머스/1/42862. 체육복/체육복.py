def solution(n, lost, reserve):
    answer = 0
    
    real_lost = set(lost) - set(reserve)
    real_reserve = set(reserve) - set(lost)
    
    for i in sorted(real_reserve):
        if i-1 in real_lost:
            real_lost.remove(i-1)
        elif i+1 in real_lost:
            real_lost.remove(i+1)
            
        
    return n-len(real_lost)