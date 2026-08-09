import heapq
def solution(n, works):
    answer = 0
    if sum(works)<=n:
        return 0
    maxheap = [-w for w in works]
    heapq.heapify(maxheap)
    for i in range(n):
        a = heapq.heappop(maxheap)
        a+=1
        heapq.heappush(maxheap,a)
    for c in maxheap:
        answer += c*c 
    return answer