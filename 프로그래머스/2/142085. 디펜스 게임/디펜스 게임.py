import heapq

def solution(n, k, enemy):
    answer = 0
    heap = []
    for i, e in enumerate(enemy):
        n-=e
        heapq.heappush(heap, -e)
        
        if n<0:
            if k>0:
                val = -heapq.heappop(heap)
                n+=val
                k-=1
            else:
                return i
    return len(enemy)