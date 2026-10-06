'''
d: 1,2,3,4 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
모든 바다 탐험
1단계 인접탐험: 한칸 이동
형재 바라보는 방향 -> 좌회전 후 직진, 우회전후 직진, 180도 후 직진
인접한 칸 방문 가능 못할 때까지 반복
바라본 방향 갱신
# 1단계
하나씩 탐색 후 r, c, d 리턴
-1, -1, -1 리턴하면 2단계
아직 visited 안한 좌표 알아야함
2단계에서는 bfs로

2단계
가장 가까운 바다 이동
인접 칸중에 갈수있는 곳 없으면 => 방문 안한 바다 현재 위치에서 가장 가까운 칸 찾아 이동
암초는 못지나, 이미 방문바다 지나.
가장 가까운칸 여러개면 행번호 작은거, 열번호 작은거 칸으로 이동
최단거리 이동. 인접칸으로 이동. 좌하우상 순서로 이동
마지막 방향이 이동방향으로 갱신

i번째 줄에 i번째 방문하는 칸 행번호, 열번호 출력
'''
from collections import deque
from operator import truediv

N, r, c, d = map(int, input().split())
d-=1
r-=1
c-=1
board=[[]*N for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(N):
    board[i] = list(map(int, input().split()))
cnt = 0
for ri in range(N):
    for ci in range(N):
        if board[ri][ci] == 1:
            cnt+=1
visited = [[False]*N for _ in range(N)]
visited[r][c] = True

def move_one(r, c, d):
    td = [[0,2,3,1], [1,3,2,0], [2,1,0,3], [3,0,1,2]]
    now_d = td[d]
    for i in now_d:
        nr, nc = r+dr[i], c+dc[i]
        if 0<=nr<N and 0<=nc<N and board[nr][nc]!=1 and visited[nr][nc] is False:
            visited[nr][nc]= True
            global cnt
            cnt+=1
            return nr, nc, i
    else:
        return -1,-1,-1

def jump(r, c, d):
    dist= [[-1]*N for _ in range(N)]
    sr, sc = r, c
    q = deque([(r, c)])
    dist[r][c] = 0
    destination = set()
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r+dr[d]
            nc = c+dc[d]
            if 0<=nr<N and 0<=nc<N and board[nr][nc]!=1 and dist[nr][nc]==-1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
                if visited[nr][nc] is False:
                    destination.add((dist[nr][nc], nr, nc))
    if len(destination)!=0:
        fdi, fr, fc = min(destination)
        visited[fr][fc]=True
        global cnt
        cnt+=1

        q= deque([(fr, fc)])
        again  = [[-1]*N for _ in range(N)]
        again[fr][fc] = 0

        while q:
            cr, cc = q.popleft()
            for nd in range(4):
                nr = cr+dr[nd]
                nc = cc+dc[nd]
                if 0 <= nr < N and 0 <= nc < N and board[nr][nc] != 1 and again[nr][nc] == -1:
                    again[nr][nc] = again[cr][cc]+1
                    q.append((nr, nc))
        cr, cc = sr, sc
        while (fr, fc) !=(cr, cc):
            for nd in (2,1,3,0):
                nr = cr+dr[nd]
                nc = cc+dc[nd]
                if 0<=nr<N and 0<=nc<N and again[nr][nc] != -1 and again[nr][nc] == again[cr][cc]-1:
                    cr, cc=nr, nc
                    last_d=nd
                    break
        return fr, fc, last_d
    else: return -1, -1,-1

cur_r, cur_c, cur_d= r, c,d
while cnt<N*N:
    print(cur_r+1, cur_c+1)
    new_r, new_c, new_d = move_one(cur_r, cur_c, cur_d)
    if (new_r, new_c, new_d) == (-1, -1, -1):
        if cnt<N*N:
            new_r, new_c, new_d = jump(cur_r, cur_c, cur_d)
            if (new_r, new_c, new_d) == (-1, -1, -1):
                break
        else: break
    cur_r, cur_c, cur_d = new_r, new_c, new_d
