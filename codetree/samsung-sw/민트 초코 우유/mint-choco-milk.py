import sys
from collections import deque

N, T = list(map(int, input().split()))
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

for i in range(N):
    belief[i] = list(map(int, input().split()))

def morning(bl):
    for i in range(N):
        for j in range(N):
            bl[i][j]+=1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

convert = { 1: 0, 2:0, 4:0, 6:1, 5:1, 3:1, 7:2}

def grouping(bl, fl):
    visited=[[0]*N for _ in range(N)]
    q = deque()
    G = []
    leader_list = []
    group_list = []

    for r in range(N):
        for c in range(N):

            if visited[r][c] ==1:
                continue

            group = []
            q.append((r, c))
            visited[r][c] =1
            f = fl[r][c]
            group.append((convert[f],-bl[r][c], r, c))

            while q:
                cr, cc = q.popleft()
                
                for d in range(4):
                    nr, nc = cr + dr[d], cc + dc[d]

                    if not (0<=nr<N and 0<=nc<N):
                        continue

                    if visited[nr][nc] == 1:
                        continue     

                    if fl[nr][nc] == f:     
                        q.append((nr, nc))
                        visited[nr][nc]=1
                        group.append((convert[fl[nr][nc]], -bl[nr][nc], nr, nc))

            G.append(group)
            
    for a in range(len(G)):
        group_list = G[a]
        group_list.sort()
        (fl_num, neg_leader_scr, leader_r, leader_c )= group_list[0]
        bl[leader_r][leader_c]+=(len(group_list)-1)
        leader_list.append((fl_num, -bl[leader_r][leader_c], leader_r, leader_c))

        for b in range(1, len(group_list)):
            (_, _, mem_r, mem_c) = group_list[b]
            bl[mem_r][mem_c] -=1

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
        d = B%4

        while x>0:
            yr, yc = yr +dr[d], yc + dc[d]
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
            if fl[i][j]==7:
                cn1+=bl[i][j]

            if fl[i][j]==3:
                cn2+=bl[i][j]

            if fl[i][j]==5:
                cn3+=bl[i][j]

            if fl[i][j]==6:
                cn4+=bl[i][j]

            if fl[i][j]==4:
                cn5+=bl[i][j]

            if fl[i][j]==2:
                cn6+=bl[i][j]

            if fl[i][j]==1:
                cn7+=bl[i][j]
    print(cn1, cn2, cn3, cn4, cn5, cn6, cn7)

bl = belief
fl = food

for _ in range(T):
    morning(bl)
    # print("mortnie", bl)
    bl, llist = grouping(bl, fl)
    # print("grpu", bl, llist)
    bl, fl = spread(bl, fl, llist)
    # print("spre", bl, fl, llist)
    score(bl, fl)
