'''
공격자 선정
공격력 낮은, 가장 최근 공격(last 큰거), 행열합 큰거, 열큰거

공격
가장 높은 포탑 선정
공격력 높음, 가장오래된, 행열 합작은, 열작은

레이저 공격
부서진포탑 못지나감. 범위 밖은 반대편으로 돌아감
최단 경로로 공격. 경로있는애들은 공격력 절반, 공격 대상은 공격력만큼. 우하좌상 순서대로

만약 최단경로 없으면 포탄공격
공격자 절반만큼 8개 피해. 해당자는 전체 공격
마찬가지로 범위 밖은 반대편 격자로 이동
공격자는 해당 없음

0 이하는 포탑 부서짐

공격과 무관한 포탑은 공격력 +1
'''

N, M, K = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(N)]
last = [[-1]*M for _ in range(N)]

def attacker():
    can = set()
    for r in range(N):
        for c in range(M):
            if board[r][c]!=0:
                can.add((board[r][c], -last[r][c], -(r+c), -c))
    score, _, neg_rc, neg_c = min(can)
    ar = -neg_rc+neg_c
    ac = -neg_c
    return ar, ac

def victim():
    can = set()
    for r in range(N):
        for c in range(M):
            if board[r][c]!=0:
                can.add((board[r][c], -last[r][c], -(r+c), -c))
    score, _, neg_rc, neg_c = max(can)
    vr = -neg_rc+neg_c
    vc = -neg_c
    return vr, vc

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def laser(ar,ac,vr,vc):
    relate = set()
    q=deque([(vr, vc)])
    dist = [[-1]*M for _ in range(N)]
    dist[vr][vc] = 0
    while q:
        cr, cc = q.popleft()
        for d in range(4):
            nr = cr+dr[d]
            nc = cc+dc[d]
            if board[nr%N][nc%M]!=0 and dist[nr%N][nc%M] ==-1:
                dist[nr % N][nc % M] = dist[cr][cc] +1
                q.append((nr%N, nc%M))

    tr, tc = ar, ac
    relate.add((ar, ac))
    visited = [[False] * M for _ in range(N)]
    visited[ar][ac] = True

    while True:
        if dist[ar][ac]==-1:
            return -1, relate

        for d in (3,1,2,0):
            nr, nc = tr+dr[d], tc+dc[d]
            nr%=N
            nc%=M
            if board[nr][nc]!=0 and dist[nr][nc]== dist[tr][tc]-1 and visited[nr][nc] is False:
                relate.add((nr, nc))
                visited[nr][nc] = True
                tr, tc = nr, nc
                if (tr, tc) == (vr, vc):
                    return 1, relate
                break

def check():
    for r in range(N):
        for c in range(M):
            if board[r][c]<=0:
                board[r][c]=0

def bomb(ar,ac,vr,vc):
    relate = set()
    relate.add((ar, ac))
    relate.add((vr, vc))
    for (rr, cc) in ((-1,-1), (-1, 0), (-1,1), (1,-1), (1, 0), (1,1), (0,-1), (0,1)):
        nr, nc = vr+rr, vc+cc
        nr %= N
        nc %= M
        if board[nr][nc]!=0:
            relate.add((nr, nc))
    return relate

def up(relate):
    for r in range(N):
        for c in range(M):
            if board[r][c] ==0:
                continue
            if (r, c) in relate:
                continue
            board[r][c]+=1



for i in range(K):
    ar, ac = attacker()
    vr, vc = victim()

    if (ar, ac) == (vr, vc):
        break

    board[ar][ac] += (N+M)
    last[ar][ac] = i

    a, relate = laser(ar,ac,vr,vc)

    if a!=-1:
        for (r,c) in relate:
            if board[r][c]==0:
                continue
            if (r, c) == (ar, ac):
                continue
            elif (r, c) == (vr, vc):
                board[vr][vc] -=board[ar][ac]
            else:
                board[r][c] -= board[ar][ac]//2

    if a==-1:
        relate = bomb(ar,ac,vr,vc)
        for (r,c) in relate:
            if board[r][c]==0:
                continue
            if (r, c) == (ar, ac):
                continue
            elif (r, c) == (vr, vc):
                board[vr][vc] -=board[ar][ac]
            else:
                board[r][c] -= board[ar][ac]//2

    check()
    up(relate)
fr, fc = victim()
print(board[fr][fc])