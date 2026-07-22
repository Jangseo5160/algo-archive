from collections import deque
    
    
def solution(n, results):
    answer = 0
    win = [[] for _ in range(n+1)]
    loose = [[] for _ in range(n+1)]
    
    for a, b in results:
        win[a].append(b)
        loose[b].append(a)
        
    def bfs(graph, i):
        v = [0] * (n+1)
        cnt =0
        q=deque([i])
        v[i]=1

        while q:
            now = q.popleft()
            for next_node in graph[now]:
                if v[next_node]==0:
                    q.append(next_node)
                    cnt+=1
                    v[next_node] = 1
        return cnt
    
    for i in range(1, n+1):
        win_cnt = bfs(win, i)
        loose_cnt = bfs(loose, i)
        
        if win_cnt+loose_cnt == n-1:
            answer+=1
        
    return answer