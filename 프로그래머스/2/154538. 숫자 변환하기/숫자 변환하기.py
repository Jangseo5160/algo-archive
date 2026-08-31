from collections import deque

def solution(x, y, n):
    answer = 0
    q = deque()
    q.append((x, 0))
    min_val = float('inf')
    visited=set()
    visited.add(x)
    
    while q:
        val, cnt = q.popleft()
        
        if val == y:
            return cnt
        
        for next_val in (val+n,val*2, val*3):
            if next_val not in visited and next_val <=y:
                visited.add(next_val)
                q.append((next_val, cnt+1))
        
    return -1