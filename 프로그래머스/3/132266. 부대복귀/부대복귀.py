from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    q=deque([destination])
    dist=[-1]*(n+1)
    dist[destination]=0
    while q:
        cur = q.popleft()
        for next_node in graph[cur]:
            if dist[next_node]==-1:
                dist[next_node] = dist[cur]+1
                q.append(next_node)
    
    return [dist[s] for s in sources]