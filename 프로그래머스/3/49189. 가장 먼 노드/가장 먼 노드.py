from collections import deque

def solution(n, edge):
    
    graph = [[] for _ in range(n+1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    dist = [-1] * (n+1)
    
    q=deque([1])
    dist[1] = 0

    while q:
        curr = q.popleft()
        
        for neighbor in graph[curr]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[curr]+1
                q.append(neighbor)
    
    max_dist = max(dist)
    return dist.count(max_dist)
    
    
        
    
    
    
    
    answer = 0
    return answer