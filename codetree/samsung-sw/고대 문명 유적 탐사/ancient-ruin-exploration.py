# import sys
# from collections import *
# K, M = map(int, input().split())
# grid = [[0]*5 for _ in range(5)]

# for i in range(5):
#     grid[i] = list(map(int, input().split()))

# num_list = list(map(int, input().split()))
# num_list.reverse()

# def is_range(r, c):
#     if 0<=r<5 and 0<=c<5:
#         return True
#     return False

# ###################################################################

# # 90도, 180도, 270도 회전
# def rotate(i, sr, sc, tgrid):
#     for i in (1, 2,3):
#         for r in range(3):
#             for c in range(3):
#                 tgrid[sr+c][sc+2-r] = tgrid[sr+r][sc+c]
#     return tgrid


# def bfs(tgrid, r, c, v):
#     q = deque([(r,c)])
#     v[r][c]=0
#     cnt = 0
#     total_cnt = 0
#     glist = set((r, c))

#     while q:
#         cr, cc = q.popleft()
#         k = tgrid[cr][cc]

#         for dr, dc in ((-1,0), (1,0), (0,-1), (0,1)):
#             nr, nc = cr+dr, cc+dc

#             if is_range(nr, nc) and tgrid[nr][nc] == k and v[nr][nc]==-1:
#                 cnt+=1
#                 q.append((nr, nc))
#                 v[nr][nc]=0
#                 glist.add((nr, nc))
#     if cnt>=3:
#         total_cnt+=cnt
#         total_glist.add(glist)

#     return total_cnt, glist

# # 획득가치 계산하기. bfs는 전체 맵에서 3개 이상 연결된 구역의 조각들 카운트
# # 3*3 선택하고 그걸 bfs돌려서 획득가치>각도작은거>열작은거>행작은거 로 구역 픽스

# def explore():
#     fscore, fi, fc, fr = 0, 6, 6, 6
#     v = [[-1]*5 for _ in range(5)]
#     for r in range(3):
#         for c in range(3):
#             for i in range(3):
#                 new_grid = [row[:] for row in grid]
#                 temp_grid = rotate(i, r, c, new_grid)
#                 score, glist = bfs(temp_grid, r, c, v)

#                 if (score, -i, -c, -r)> (fscore, -fi, -fc, -fr):
#                     fscore, fi, fc, fr = score, i, c, r
#                     fglist = glist

#     return fi, fc, fr, fscore, fglist



# # 해당 구역들 열번호 작은순> 행번호 큰순으로 새로운 숫자들 채워넣기. 벽면 숫자 reverse 해서 pop하기
# def get_treasure():
#     total_score = 0
#     fi, fc, fr, fscore, fglist = explore()
#     newglist = []
#     for r, c in fglist:
#         newglist.append([c, -r])
#     newglist.sort()
#     for r, c in newglist:
#         num = num_list.pop()
#         grid[r][c] = num
#     total_score+=fscore

#     while True:
#         v=[[-1]*5 for _ in range(5)]
#         for r in range(5):
#             for c in range(5):
#                 score, glist = bfs(temp_grid, r, c, v)
#                 if score ==0:
#                     break

#                 total_score+=score
#                 newglist = []
#                 for r, c in glist:
#                     newglist.append([c, -r])
#                 newglist.sort()
#                 for r, c in newglist:
#                     num = num_list.pop()
#                     grid[r][c] = num

#     return grid, total_score

# while K:
#     grid, total_score = get_treasure()
#     if total_score>=3:
#         print(total_score)
#     else:
#         break


    
        

# # 그리고 다시 그리드 bfs 검사해서 조각 카운트되면 또 없어지고 새로운 




import sys
from collections import *

K, M = map(int, input().split())
grid = [[0]*5 for _ in range(5)]
for i in range(5):
    grid[i] = list(map(int, input().split()))

num_list = list(map(int, input().split()))
num_list.reverse()

def is_range(r, c):
    if 0<=r<5 and 0<=c<5:
        return True
    return False

###################################################################

# 90도, 180도, 270도 회전 (i=1,2,3). tgrid를 직접 바꾸지 않고 새 grid를 리턴.
def rotate(i, sr, sc, tgrid):
    cur = [[tgrid[sr+r][sc+c] for c in range(3)] for r in range(3)]
    for _ in range(i):
        new = [[0]*3 for _ in range(3)]
        for r in range(3):
            for c in range(3):
                new[r][c] = cur[2-c][r]
        cur = new
    result = [row[:] for row in tgrid]
    for r in range(3):
        for c in range(3):
            result[sr+r][sc+c] = cur[r][c]
    return result

# 보드 전체(5x5)를 훑어서 3개 이상 연결된 모든 덩어리를 찾음
# 리턴: (총 점수, 지워질 좌표 집합)
def bfs(tgrid):
    v = [[-1]*5 for _ in range(5)]
    total_cnt = 0
    total_glist = set()

    for sr in range(5):
        for sc in range(5):
            if v[sr][sc] != -1:
                continue
            q = deque([(sr, sc)])
            v[sr][sc] = 0
            glist = {(sr, sc)}
            k = tgrid[sr][sc]

            while q:
                cr, cc = q.popleft()
                for dr, dc in ((-1,0), (1,0), (0,-1), (0,1)):
                    nr, nc = cr+dr, cc+dc
                    if is_range(nr, nc) and tgrid[nr][nc] == k and v[nr][nc] == -1:
                        v[nr][nc] = 0
                        glist.add((nr, nc))
                        q.append((nr, nc))

            if len(glist) >= 3:
                total_cnt += len(glist)
                total_glist |= glist

    return total_cnt, total_glist

# 획득가치 계산하기. bfs는 회전된 보드 전체에서 3개 이상 연결된 조각들 카운트
# 3*3 선택하고 그걸 bfs돌려서 획득가치>각도작은거>열작은거>행작은거 로 구역 픽스
def explore():
    best = None  # (score, i, sc, sr), temp_grid, fglist

    for sr in range(3):
        for sc in range(3):
            for i in (1, 2, 3):
                temp_grid = rotate(i, sr, sc, grid)
                score, glist = bfs(temp_grid)
                if score == 0:
                    continue
                key = (-score, i, sc, sr)
                if best is None or key < best[0]:
                    best = (key, temp_grid, glist)

    return best  # None이면 어떤 회전을 해도 유물을 못 얻는 것(탐사 종료 신호)

# 지워진 자리들에 열번호 작은순 > 행번호 큰순으로 새 숫자 채워넣기
def fill(g, glist):
    newglist = []
    for r, c in glist:
        newglist.append([c, -r])
    newglist.sort()
    for c, nr in newglist:
        r = -nr
        g[r][c] = num_list.pop()

def get_treasure():
    global grid
    best = explore()
    if best is None:
        return None  # 이번 턴은 유물을 하나도 못 얻음 -> 탐사 종료

    _, temp_grid, fglist = best
    grid = temp_grid          # 선택된 회전을 실제로 적용
    total_score = 0

    glist = fglist
    while True:
        score = len(glist)
        if score == 0:
            break
        total_score += score
        fill(grid, glist)
        score, glist = bfs(grid)  # 채운 뒤 다시 검사 (연쇄)

    return total_score

results = []
for _ in range(K):
    total_score = get_treasure()
    if total_score is None:
        break
    results.append(total_score)

print(' '.join(map(str, results)))