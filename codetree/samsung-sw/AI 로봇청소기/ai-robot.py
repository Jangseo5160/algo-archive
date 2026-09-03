from collections import deque
import sys

N, K, L = map(int, input().split())
grid = [ list(map(int, input().split())) for _ in range(N)]
cleaner = [[0,0] for _ in range(K)]
for i in range(K):
    r, c = map(int, input().split())
    cleaner[i] = [r-1,c-1]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

# 청소기 이동
# 청소기 좌표, 먼지 현황, 몇번째 청소기인지
# 이동거리 계산, 가장 가까운 격자로 이동
# 청소기의 좌표만 다시 계산해서 바뀌는 건 청소기 좌표뿐
# 이동거리 짧은것 > 같다면 행작은거>열작은거
def move(cleaner, grid, i):
    sr, sc = cleaner[i]
    q=deque([(sr, sc)])
    visited=[[False]*N for _ in range(N)]
    visited[sr][sc] = True
    cleaner_set = set(map(tuple,cleaner))
    candidates = []
    dist = [[-1]*N for _ in range(N)]
    dist[sr][sc]=0
    while q:
        cr, cc = q.popleft()

        if grid[cr][cc]>0:
            candidates.append((dist[cr][cc], cr, cc))

        for d in range(4):
            nr, nc = cr+dr[d], cc+dc[d]
            if 0<=nr<N and 0<=nc<N and visited[nr][nc]==False and grid[nr][nc]!=-1 and (nr, nc) not in cleaner_set:
                q.append((nr, nc))
                visited[nr][nc]=True
                dist[nr][nc]=dist[cr][cc]+1
    if not candidates:
        return
    candidates.sort()
    _, new_r, new_c = candidates[0]
    cleaner[i] = [new_r, new_c]


def clean(cleaner, grid):
    possible = []
    nlist = []
    cleaner_set = set(map(tuple, cleaner))
    for r, c in cleaner:
        # 오른쪽
        for d in range(4):
            total = 0
            if d==0:
                nlist = [(r, c+1),(r-1,c),(r+1,c),(r,c)]
        # 아래쪽
            if d==1:
                nlist = [(r+1, c), (r, c-1), (r, c+1), (r, c)]
        # 왼쪽
            if d==2:
                nlist = [(r, c - 1), (r - 1, c), (r + 1, c), (r, c)]
        # 위쪽
            if d==3:
                nlist = [(r-1, c), (r, c-1), (r , c+1), (r, c)]

            for tempr, tempc in nlist:
                if 0<=tempr<N and 0<=tempc<N and grid[tempr][tempc]>0:
                    total += min(grid[tempr][tempc], 20)
            possible.append((-total, d))

        finald = min(possible)[1]
        # 오른쪽

        if finald == 0:
            nlist = [(r, c + 1), (r - 1, c), (r + 1, c), (r, c)]
        # 아래쪽
        elif finald == 1:
            nlist = [(r + 1, c), (r, c - 1), (r, c + 1), (r, c)]
        # 왼쪽
        elif finald == 2:
            nlist = [(r, c - 1), (r - 1, c), (r + 1, c), (r, c)]
        # 위쪽
        elif finald == 3:
            nlist = [(r - 1, c), (r, c - 1), (r, c + 1), (r, c)]

        for tempr, tempc in nlist:
            if 0 <= tempr < N and 0 <= tempc < N and grid[tempr][tempc] > 0:
                grid[tempr][tempc] = max(0, grid[tempr][tempc]-20)
        possible = []


def accumulate(grid):
    for r in range(N):
        for c in range(N):
            if grid[r][c]>0:
                grid[r][c]+=5

def spread(grid):
    new_grid = [row[:] for row in grid]

    for r  in range(N):
        for c in range(N):
            if grid[r][c]==0:
                total = 0
                for d in range(4):
                    nr, nc = r+dr[d], c+dc[d]
                    if 0<=nr<N and 0<=nc<N and grid[nr][nc]>0:
                        total+=grid[nr][nc]
                new_grid[r][c] = total//10
    return new_grid

def main(grid, cleaner):
    for _ in range(L):
        for i in range(K):
            move(cleaner, grid, i)

        clean(cleaner, grid)
        accumulate(grid)
        grid = spread(grid)

        total = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c]>0:
                    total+=grid[r][c]

        print(total)
main(grid, cleaner)