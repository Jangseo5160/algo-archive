import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    cnt = 0
    while True:
        if scoville[0] >=K: 
            return cnt
        if len(scoville) ==1 and scoville[0]<K:
            return -1
        
        new_score = heapq.heappop(scoville)
        new_score += heapq.heappop(scoville) *2
        # print(new_score)
        # print(scoville)
        heapq.heappush(scoville, new_score)
        cnt+=1
    return -1