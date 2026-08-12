import heapq

def solution(n, roads, sources, destination):
    answer = []
    
    graph = [[]*2 for _ in range(n+1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    INF = int(1e9)
    dist = [INF] * (n+1)
    
    heap = [(0, destination)]
    dist[destination] = 0
    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        if cur_dist > dist[cur_node]:
            continue
        for next_node in graph[cur_node]:                    
            new_dist = cur_dist + 1
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))
    for s in sources:
        if dist[s]==INF:
            answer.append(-1)
        else:
            answer.append(dist[s])
    return answer