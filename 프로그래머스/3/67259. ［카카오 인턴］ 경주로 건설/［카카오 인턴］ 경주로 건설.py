# bfs로 접근했지만, 모든 간선이 양수이기 때문에 다익스트라임
# 

from collections import deque
def solution(board):
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
        
    INF = float('inf')
    cost = [[[INF]*4 for _ in range(len(board))] for _ in range(len(board))]
    
    q = deque() # r, c, 방향, 비용
    q.append((0,0,-1,0))
        
    while q:
        r, c, prev_dir, cur_cost = q.pop()
        
        for i in range(4):
            nr = r+ dr[i]
            nc = c+dc[i]
            new_dir = i
            if 0<=nr<len(board) and 0<=nc<len(board) and board[nr][nc]==0:
                if prev_dir == -1:
                    new_cost = cur_cost+100
                
                elif new_dir//2 == prev_dir//2:
                    new_cost = cur_cost+100
                else:
                    new_cost = cur_cost+600
                
                if new_cost<cost[nr][nc][new_dir]:
                    cost[nr][nc][new_dir] = new_cost
                    q.append((nr, nc, new_dir, new_cost))
                
    answer = 0
    return min(cost[len(board)-1][len(board)-1])