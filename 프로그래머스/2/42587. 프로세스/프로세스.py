from collections import deque
def solution(priorities, location):
    q=deque()
    for i in range(len(priorities)):
        q.append((priorities[i], i))
        
    cnt=0
    while q:
        p, idx = q.popleft()
        if any(pri > p for pri, _ in q):
            q.append((p, idx))
        else:
            cnt+=1
            if idx == location:
                return cnt
    