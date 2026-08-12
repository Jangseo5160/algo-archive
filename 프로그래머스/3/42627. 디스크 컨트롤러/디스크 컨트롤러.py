import heapq

# 요청 시각 순으로 정렬
# 절대 시간까지 도착한 작업들 후보에 추가 => 시간-시각-번호 순으로 정렬
# 가장 짧은 처리 시간 먼저 처리
# 작업 수행 후 절대시각-요청시각 누적합
# 다음 절대시간부터 다시 도착한 작업들 후보에 추가

def solution(jobs):
    joblist = []
    for idx, [req, dur] in enumerate(jobs):
        joblist.append((req,dur,idx))
    joblist.sort()
    
    answer = 0
    heap = [] # 대기열
    i=0
    time = 0
    finished = 0
    
    while finished < len(jobs):
        while i<len(jobs) and joblist[i][0]<=time:
            req, dur, idx = joblist[i]
            heapq.heappush(heap, (dur, req, idx))
            i+=1
        
        if heap:
            work, start, num = heapq.heappop(heap)
            time+=work
            answer += time - start
            finished+=1
            
        else: time+=1
        
    return answer//len(jobs)