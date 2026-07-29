import sys
from collections import deque

N, T = map(int, input().split())
food = [[0]*N for _ in range(N)]
belief = [[0]*N for _ in range(N)]

for i in range(N):
    clist = list(input())
    for j in range(N):
        c = clist[j]
        if c == 'T':
            c = 1
        if c=='C':
            c=2
        if c=='M':
            c=4
        food[i][j] = c

belief = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

convert = { 1: 0, 2:0, 4:0, 6:1, 5:1, 3:1, 7:2}

def grouping(bl, fl):
    visited=[[0]*N for _ in range(N)]
    q = deque()
    leader_list = []

    for r in range(N):
        for c in range(N):

            if visited[r][c] ==1:
                continue

            q.append((r, c))
            visited[r][c] =1
            f = fl[r][c]

            fr, fc = r, c
            cnt = 1

            while q:
                cr, cc = q.popleft()
                
                for d in range(4):
                    nr, nc = cr + dr[d], cc + dc[d]  

                    if (0<=nr<N and 0<=nc<N) and visited[nr][nc] !=1 and fl[nr][nc] == f:     
                        q.append((nr, nc))
                        visited[nr][nc]=1
                        cnt+=1

                        if (-bl[nr][nc], nr, nc )<(-bl[fr][fc], fr, fc):
                            fr, fc = nr, nc
            bl[fr][fc] +=cnt
            leader_list.append((convert[fl[fr][fc]], -bl[fr][fc], fr, fc))

    leader_list.sort()
    return bl, leader_list

def spread(bl, fl, leader_list):
    blocked = set()
    
    for i in range(len(leader_list)):
        (fl_num, neg_scr, lr, lc )= leader_list[i]

        if (lr, lc) in blocked:
            continue
        
        B = bl[lr][lc]
        x = B-1
        bl[lr][lc] = 1

        yr, yc = lr, lc

        while x>0:
            yr, yc = yr +dr[B%4], yc + dc[B%4]
            if not (0<=yr<N and 0<=yc<N):
                break

            if fl[yr][yc] == fl[lr][lc]:
                continue

            # 강한전파
            if x > bl[yr][yc]:
                fl[yr][yc] = fl[lr][lc]
                x=x-(bl[yr][yc]+1)
                bl[yr][yc]+=1
                blocked.add((yr, yc))

            #약한전파
            else:
                fl[yr][yc] |= fl[lr][lc]
                bl[yr][yc] +=x
                blocked.add((yr, yc))
                x=0
                
    return bl, fl

def score(bl, fl):
    cn1, cn2, cn3, cn4, cn5, cn6, cn7 = 0, 0, 0, 0, 0, 0, 0
    for i in range(N):
        for j in range(N):
            if fl[i][j]==7: cn1+=bl[i][j]
            if fl[i][j]==3: cn2+=bl[i][j]
            if fl[i][j]==5: cn3+=bl[i][j]
            if fl[i][j]==6: cn4+=bl[i][j]
            if fl[i][j]==4: cn5+=bl[i][j]
            if fl[i][j]==2: cn6+=bl[i][j]
            if fl[i][j]==1: cn7+=bl[i][j]
    print(cn1, cn2, cn3, cn4, cn5, cn6, cn7)

bl = belief
fl = food

for _ in range(T):
    bl, llist = grouping(bl, fl)
    bl, fl = spread(bl, fl, llist)
    score(bl, fl)


