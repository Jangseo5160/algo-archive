import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville)>1:
        first_min = heapq.heappop(scoville)
        if first_min >= K:
            return answer
        second_min = heapq.heappop(scoville)
        new_score = first_min + second_min*2
        heapq.heappush(scoville, new_score)
        answer+=1
    
    num = scoville.pop()
    if num >=K: return answer
    else: return -1