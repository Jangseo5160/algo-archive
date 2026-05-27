def solution(n, lost, reserve):
    answer = 0
    can_reserve = 0
    
    real_lost = set(lost) - set(reserve)
    real_reserve = set(reserve) - set(lost)
    
    for i in sorted(real_lost):
        if i-1 in real_reserve:
            real_reserve.remove(i-1)
            can_reserve+=1
        elif i+1 in real_reserve:
            real_reserve.remove(i+1)
            can_reserve+=1
            
    return n - len(real_lost) + can_reserve
