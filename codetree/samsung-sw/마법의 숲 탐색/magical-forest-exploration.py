'''
1행부터 R행까지
d=0,1,2,3 북동남서

남쪽
서쪽 회전 :출구 반시계방향으로 이동 0-3-2-1
남서쪽 다 안되면 동쪽 회전: 시계방향으로 이동 0-1-2-3

가장 남쪽까지 도달했는데, 몸 일부가 숲 밖이면새롭게 탐색. 최종 위치 답에 포함 안됨

가장 남쪽 도달해서 더이상 이동 안되면 정령 이동.
골렘 내에서 출구 있으면 다른 골렘으로 이동 가능. 갈 수 있는 남쪽 칸까지 가서 종료.
행번호의 합 구하기.
'''
from collections import deque

R, C, K = map(int, input().split())
center = [[-2] for _ in range(K)] # r, c, d
board = [[-1] * C for _ in range(R)]

for i in range(K):
    c, d = map(int, input().split())
    center[i].append(c-1)
    center[i].append(d)

shape = [(-1,0), (1,0), (0,-1), (0,1),(0,0)]

def write(i, r, c, board):
    for (dr, dc) in shape:
        nr, nc = r+dr, c+dc
        board[nr][nc] = i

def can(r, c, d, board):
    for (dr, dc) in shape:
        nr = r+dr
        nc = c+dc
        if not (nr<R and 0<=nc<C):
            return False
        if nr>=0 and board[nr][nc] !=-1:
            return False
    return True

def put_down(i, r,c,d,board):
    while True:
        if can(r+1, c, d, board):
            r+=1
        elif can(r, c-1, d, board) and can(r+1, c-1, d, board):
            r+=1
            c-=1
            d=(d-1)%4
        elif can(r, c+1, d, board) and can(r+1, c+1, d, board):
            r+=1
            c+=1
            d=(d+1)%4
        else:
            break
    if r<=0:
        return -1,-1,-1,[[-1]*C for _ in range(R)]
    write(i, r, c, board)
    return r, c, d, board



def find_gate(r,c,d,gate):
    if d==0:
        gate.add((r-1, c))
    elif d==1:
        gate.add((r,c+1))
    elif d==2:
        gate.add((r+1, c))
    else:
        gate.add((r, c-1))
dr = [-1, 1, 0, 0]
dc = [0,0,-1,1]

def move(r,c,gate, board):
    q=deque([(r, c)])
    visited = [[False] * C for _ in range(R)]
    visited[r][c]=True
    grid = set()
    grid.add((r, c))
    while q:
        cr,cc = q.popleft()
        for d in range(4):
            nr,nc = cr+dr[d], cc+dc[d]
            if 0<=nr<R and 0<=nc<C and not visited[nr][nc] and board[nr][nc] !=-1:
                if board[nr][nc] == board[cr][cc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    grid.add((nr, nc))
                elif board[nr][nc] != board[cr][cc] and (cr, cc) in gate:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    grid.add((nr, nc))

    final_r = max(grid)[0]
    return final_r



total = 0
gate = set()
for i in range(K):
    cr, cc, cd = center[i]
    answer = 0
    nr, nc, nd, board = put_down(i, cr, cc, cd, board)
    find_gate(nr,nc,nd,gate)
    if (-1, -1, -1) == (nr, nc, nd):
        gate = set()
        continue
    else:
        final_row = move(nr, nc, gate, board)
        total += final_row+1
print(total)
    # if out(nr, nc) is True:
    #     board = [[-1] * C for _ in range(R)]
    # else:
    #     final_row = move(nr, nc)
    #     answer+=final_row