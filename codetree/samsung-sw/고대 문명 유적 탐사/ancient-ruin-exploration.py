'''
5x5 격자에서 7가지의 유물 조각 (1~7)

1. 탐사 진행
    candidate_rotation()
    - 회전 중심 좌표 (1,1 ~ 3,3)별로 90도 180도 270도 중 하나의 각도만큼 회전 했을때의 1차 획득 가치 도출 
        - 이때 최대 가치 -> 회전 각도 -> 열이 가장 작은 구간 -> 행이 가장 작은 구간 대로 우선순위 
    
    go_rotation()
    - 앞서 뽑은 후보에 대해 회전 진행 

2. 유물 획득
    get_treasure()
    - 방문하지 않은 칸에 대해 상하좌우로 인접한 같은 종류의 유물 조각이 3개 이상일 경우 가치 카운트 
    - 총 가치 리턴하고 각 좌표들도 임시 격자에다가 false로 표시해두기

    put_treasure()
    - 조각이 사라진 위치에 새로운 조각 넣기 
    - 열 번호 작은 순 -> 행 번호 큰 순 

    + 유물 연쇄 힉득 (유물이 없을 때까지 반복)
        
3. 탐사 반복
    - 총 K번 턴에 걸쳐 진행 
    - 각 턴마다 획득한 유물의 가치의 총합 출력 
    - 1차 유물 획득에서 아무것도 없었다면 K번 못채워도 종료 

'''
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5


# 1. 유물 획득 및 가치 계산 함수
def get_treasure(current_grid):
    total_value = 0
    is_treasure = [[False] * 5 for _ in range(5)]
    visited = [[False] * 5 for _ in range(5)]
    
    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                queue = deque([(i, j)])
                visited[i][j] = True
                group = [(i, j)] # 연결된 좌표들을 담을 리스트
                
                while queue:
                    cx, cy = queue.popleft()
                    
                    for d in range(4):
                        nx = cx + dx[d]
                        ny = cy + dy[d]
                        
                        if in_range(nx, ny) and not visited[nx][ny] and current_grid[cx][cy] == current_grid[nx][ny]:
                            queue.append((nx, ny))
                            visited[nx][ny] = True
                            group.append((nx, ny))
                
                # 3개 이상 연결되었다면 가치 추가 및 삭제 표시
                if len(group) >= 3:
                    total_value += len(group)
                    for gx, gy in group:
                        is_treasure[gx][gy] = True
                        
    return total_value, is_treasure


# 2. 3x3 부분 격자 회전 함수
def rotate_grid(original_grid, r, c, angle):
    # 2차원 배열 깊은 복사 (deepcopy보다 빠름)
    new_grid = [row[:] for row in original_grid]
    
    for _ in range(angle):
        tmp_grid = [row[:] for row in new_grid]
        for i in range(3):
            for j in range(3):
                # 90도 시계방향 회전 공식
                new_grid[r-1+i][c-1+j] = tmp_grid[r+1-j][c-1+i]
                
    return new_grid


# 3. 최적의 회전 후보 찾기 함수
def candidate_rotation():
    max_value = -1
    best_grid = None
    
    # 우선순위: 1.회전각도(작은순) -> 2.열(작은순) -> 3.행(작은순)
    for angle in range(1, 4):
        for c in range(1, 4):
            for r in range(1, 4):
                rotated = rotate_grid(grid, r, c, angle)
                val, _ = get_treasure(rotated)
                
                if val > max_value:
                    max_value = val
                    best_grid = rotated
                    
    return max_value, best_grid


# 4. 빈 곳에 새로운 유물 조각 채우기 함수
def put_treasure(current_grid, is_treasure):
    # 열 번호가 작은 순 -> 행 번호가 큰 순
    for c in range(5):
        for r in range(4, -1, -1):
            if is_treasure[r][c]:
                # 큐가 비어있지 않을 때만 채움 (안전장치)
                if wait_treasure:
                    current_grid[r][c] = wait_treasure.popleft()


K, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(5)]
wait_treasure = deque(list(map(int, input().split())))

# 메인 시뮬레이션
for k in range(K):
    # 1단계: 탐사 진행 (최적의 회전 찾기)
    turn_val, next_grid = candidate_rotation()
    
    # 1차 획득에서 아무것도 얻지 못했다면 즉시 종료
    if turn_val == 0:
        break
        
    grid = next_grid # 최적의 격자로 업데이트
    turn_total_value = 0
    
    # 2단계 & 3단계: 유물 획득 및 연쇄 작용
    while True:
        # 현재 격자에서 획득할 유물 찾기
        val, is_treasure = get_treasure(grid)
        
        # 더 이상 터질 유물이 없으면 연쇄 종료
        if val == 0:
            break
            
        turn_total_value += val
        
        # 유물이 사라진 자리에 새로 채워넣기
        put_treasure(grid, is_treasure)
        
    # 각 턴마다 획득한 총 가치 출력 (보통 공백 기준으로 출력합니다)
    print(turn_total_value, end=" ")
