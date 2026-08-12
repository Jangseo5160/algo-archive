def solution(n, times):
    answer = 0
    left = 1
    right = max(times)*n
    
    while left<=right:
        mid = (left+right)//2
        cnt = 0
        
        for t in times:
            cnt += mid//t
            
            if cnt >= n:
                break
                
        if cnt>=n:
            right = mid-1
        else:
            left= mid+1
        
    return left