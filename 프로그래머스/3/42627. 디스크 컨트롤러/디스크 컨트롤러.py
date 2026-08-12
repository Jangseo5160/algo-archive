import heapq

def solution(jobs):
    joblist = []
    for idx, [req, dur] in enumerate(jobs):
        joblist.append((req,dur, idx))
    joblist.sort()
    
    answer = 0
    n = len(jobs)
    heap = []
    i=0
    time = 0
    finished = 0
    
    while finished < n:
        while i<n and joblist[i][0]<=time:
            req,dur, idx = joblist[i]
            heapq.heappush(heap, (dur, req, idx))
            i+=1
        
        if not heap:
            time = joblist[i][0]
            continue
            
        work, start, num = heapq.heappop(heap)
        time+=work 
        answer += time - start
        finished+=1
        
    return answer//n