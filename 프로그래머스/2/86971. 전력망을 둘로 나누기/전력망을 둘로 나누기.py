from collections import deque

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for cuta, cutb in wires:
        visited = [False] * (n +1)
        q = deque([1])
        visited[1] = True
        cnt= 1
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                
                if (cur == cuta and nxt == cutb) or (cur == cutb and nxt == cuta):
                    continue
                
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
                    cnt+=1
        other = n-cnt
        answer = min(abs(other-cnt), answer)
    
    return answer