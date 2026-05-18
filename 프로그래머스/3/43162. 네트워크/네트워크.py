def solution(n, computers):
    answer = 0
    visited = [False] * n
    # dfs, 방문하지 않은 노드들을 만날 때 마다 dfs 호출. 연결된 노드들을 모두 방문처리 한다.
    def dfs(com_idx): # 현재 탐색 중인 컴퓨터 인덱스를 매개변수로 삼음.
        visited[com_idx] = True
        
        for neighbor in range(n):
            # 연결되어있고, 아직 방문하지 않은 컴퓨터면 방문하기
            if computers[com_idx][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)
            
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer+=1
        
    
    return answer