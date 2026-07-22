import sys
from collections import deque

N, K, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
cleaner = [[] for _ in range(K)]
for i in range(K):
    r, c = map(int, input().split())
    r=r-1; c=c-1
    cleaner[i] = [r, c]


def move_cleaner():
    global grid

    for i in range(K):
        r, c = cleaner[i]
        v=[[-1]*N for _ in range(N)]

        q=deque([(r,c)])
        v[r][c]=0
        min_dist = float('inf')
        can = []
        cleaner_set = set(tuple(pos) for pos in cleaner)
        while q:
            cr, cc = q.popleft()

            if v[cr][cc]>min_dist:
                break

            if grid[cr][cc]>0:
                if v[cr][cc]<=min_dist:
                    min_dist = v[cr][cc]
                    can.append([v[cr][cc], cr, cc])
            
            for dr, dc in ((-1, 0), (1, 0), (0,-1),(0,1)):
                nr, nc = cr+dr, cc+dc
                if 0<=nr<N and 0<=nc<N and grid[nr][nc]>=0 and v[nr][nc]==-1 and (nr, nc) not in cleaner_set:
                    q.append((nr, nc))
                    v[nr][nc] = v[cr][cc]+1
        if can:
            can.sort()
            dist, new_r, new_c = can[0]
            cleaner[i] = [new_r, new_c]


# move_cleaner()
# print(grid)
# print(cleaner)

def cleaning():
    global grid

    for r, c in cleaner:
        order = [[[r+1, c], [r-1, c], [r, c+1], [r,c]]
            ,[[r+1, c], [r, c-1], [r, c+1], [r,c]]
            ,[[r+1, c], [r-1, c], [r, c-1], [r,c]]
            ,[[r-1, c], [r, c-1], [r, c+1], [r,c]]
            ]
        final = []
        for d in range(4):
            total=0
            for i in range(4):
                nr, nc = order[d][i]
                if 0<=nr<N and 0<=nc<N and grid[nr][nc] >0:
                    if grid[nr][nc] >=20:
                        total+=20
                    else:
                        total +=grid[nr][nc]
                    # print(total)
            final.append((-total,d))
        # print(r,c, "\n", final)
        if final:
            
            final.sort()
            # print(r,c, "\n", final)
            _, dir = final[0]
            # print(dir)
            for j in range(4):
                temp_r, temp_c = order[dir][j]
                # print("test", r, c, temp_r, temp_c)
                if 0<=temp_r<N and 0<=temp_c<N and grid[temp_r][temp_c] >0:
                    # print("success")
                    # print("pass", temp_r, temp_c)
                    # print("ccc")
                    if grid[temp_r][temp_c]>=20:

                        grid[temp_r][temp_c]-=20
                    else:
                        grid[temp_r][temp_c]=0

# for row in grid: 
#     print(row) 
# print("\n") 
# cleaning()
# for row in grid: 
#     print(row)    
# print("\n") 

# for row in cleaner:
#     print(row)

def dirty():
    global grid
    for r in range(N):
        for c in range(N):
            if grid[r][c]>0:
                grid[r][c]+=5
# dirty()
# print(grid)
def spread():
    global grid

    new_grid = [row[:] for row in grid]
    for r in range(N):
        for c in range(N):
            if grid[r][c]==0:
                total = 0
                for dr, dc in ((-1, 0), (1, 0), (0,-1),(0,1)):
                    nr, nc = r+dr, c+dc
                    if 0<=nr<N and 0<=nc<N and grid[nr][nc]>0:
                        total+=grid[nr][nc]
                new_grid[r][c] = total//10
    grid = new_grid

# spread()
# print(grid)

def score():
    total =0
    for r in range(N):
        for c in range(N):
            if grid[r][c]>0:
                total+=grid[r][c]
    print(total)



for _ in range(L):
    move_cleaner()
    # for row in grid: 
    #     print(row) 
    # for c in cleaner: 
    #     print(c) 
    cleaning()
    # for row in grid: 
    #     print(row) 
    # for c in cleaner: 
    # #     print(c) 
    dirty()
    spread()
    # # for row in grid: 
    # #     print(row) 
    # # for c in cleaner: 
    # #     print(c) 
    score()

