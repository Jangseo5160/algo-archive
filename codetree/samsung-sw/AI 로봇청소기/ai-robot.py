'''
청소기 이동: 가장 가까운 이동거리인 먼지있는 격자로 이동.
물건, 청소기 있으면 안됨. 범위 내 이동
이동거리 짧은거>행번호 작은거> 열번호 작은거

청소: 지금 바라보고 있는 방향 기준으로 오른쪽, 아래쪽, 왼쪽, 위쪽 청소
4가지 격자에서 청소할 수 있는 먼지량 가장 큰거 선정
먼지량 큰거 > 우/하/좌/상 순서
최대 먼지 청소량 20 => board에 남는거 max(p-20, 0), 청소량 : min(20, p)
청소기 순서대로 진행

먼지 축적: 모든 먼지있는 곳 +5

먼지 확산: 주변 4방향 먼지량 합 //10 만큼 확산
동시 확산
'''
from collections import deque
N, K, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
robot = [[0]*2 for _ in range(K)]
for i in range(K):
    r, c = map(int, input().split())
    robot[i] = [r-1, c-1]

def move():
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    temp = set()
    for [r, c] in robot:
        temp.add((r, c))

    for i in range(K):
        sr, sc = robot[i]
        if board[sr][sc]>0:
            continue
        q=deque([(sr, sc)])
        dist = [[-1]*N for _ in range(N)]
        dist[sr][sc] = 0
        pos = set() # 먼지있는 곳 이동거리, 행, 열

        while q:
            cr, cc = q.popleft()
            for d in range(4):
                nr, nc = cr+dr[d], cc+dc[d]
                if 0<=nr<N and 0<=nc<N and board[nr][nc]!=-1 and dist[nr][nc]==-1 and (nr, nc) not in temp:
                    q.append((nr, nc))
                    dist[nr][nc] = dist[cr][cc] +1
                    if board[nr][nc] >0:
                        pos.add((dist[nr][nc], nr, nc))
        if pos:
            _, er, ec = min(pos)
            robot[i] = [er, ec]
            temp.remove((sr, sc))
            temp.add((er, ec))

def cases(r, c):
    group = set()
    shape = [[(-1, 0), (0,0), (1,0), (0,1)], [(0,-1), (0,0), (0,1),(1,0)], [(0,-1),(0,0), (1,0), (-1,0)], [(0,-1),(0,0),(0,1),(-1,0)]]
    for d in range(4):
        total = 0
        for (ddr, ddc) in shape[d]:
            nr, nc = r+ddr, c+ddc
            if 0<=nr<N and 0<=nc<N and board[nr][nc]>0:
                #########청소기 있는 곳 청소 가능한지? 일단 가능하다고 하고 진행
                total += min(board[nr][nc], 20)
        group.add((total, -d))
    return group


def clean():
    # 우/하/좌/상
    for ori_r, ori_c in robot:
        group = cases(ori_r, ori_c)
        _, neg_fd = max(group)
        fd = -neg_fd

        shape = [[(-1, 0), (0, 0), (1, 0), (0, 1)], [(0, -1), (0, 0), (0, 1), (1, 0)],
                 [(0, -1), (0, 0), (1, 0), (-1, 0)], [(0, -1), (0, 0), (0, 1), (-1, 0)]]

        for (ddr, ddc) in shape[fd]:
            nnr, nnc = ori_r + ddr, ori_c + ddc
            if 0 <= nnr < N and 0 <= nnc < N and board[nnr][nnc] > 0:
                board[nnr][nnc] = max((0, board[nnr][nnc]-20))

def plus():
    for r in range(N):
        for c in range(N):
            if board[r][c]>0:
                board[r][c]+=5

def spread():
    global board
    new = [row[:] for row in board]
    shape = [(-1,0), (1,0), (0,-1), (0,1)]
    for r in range(N):
        for c in range(N):
            if board[r][c]==0:
                total=0
                for (dddr, dddc) in shape:
                    nr, nc = r+dddr, c+dddc
                    if 0<=nr<N and 0<=nc<N and board[nr][nc]>0:
                        total += board[nr][nc]
                new[r][c] += total//10
    board = new

for _ in range(L):
    score=0
    move()
    clean()
    plus()
    spread()
    for r in range(N):
        for c in range(N):
            if board[r][c]>0:
                score+=board[r][c]
    if score==0:
        print(score)
        break
    print(score)