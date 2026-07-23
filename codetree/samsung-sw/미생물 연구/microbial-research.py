import sys
from collections import deque

# 입력 받기
N, Q = map(int, input().split())

# 자료형
grid = [[-1]*(N) for _ in range(N)]
bio = {}


def print_grid(grid):
    for i in range(N):
        print(*grid[i], sep = '\t')


def adding(i):
    sj, si, ej, ei = map(int, input().split())
    bio[i] = [si, sj, ei, ej]
    for r in range(si, ei):
        for c in range(sj, ej):
            grid[r][c] = i

def bfs(r, c, v, grid):
    q = deque([(r, c)])
    v[r][c] = True
    section =[grid[r][c], [r, c]]

    while q:
        cr, cc = q.popleft()
        for (dr, dc) in ((-1,0), (1,0), (0,-1), (0,1)):
            nr, nc = cr+dr, cc+dc
            # 범위 안, 키가 같, 방문 안함
            if 0<=nr<N and 0<=nc<N and v[nr][nc] is False and grid[nr][nc] == grid[r][c]:
                q.append([nr, nc])
                v[nr][nc] = True
                section.append(([nr, nc]))
    return section

def inspecting():
    v = [[False]*N for _ in range(N)]
    section_list = []

    # grid 변경되었으니, bfs 돌리면서 bio 별로 좌표 리스트 추가해주고, 만약 쪼개지면 아예 없애주는거
    for r in range(N):
        for c in range(N):   
            if grid[r][c]>0 and v[r][c] is False:
                
                section = bfs(r, c, v, grid)
                section_list.append(section)
    rem_set= set()

    for arr in section_list:
        for brr in section_list:
            if arr != brr and arr[0]==brr[0]:
                rem_set.add(arr[0])
    ############# counter 사용 ########################
    # key_counts = Counter([arr[0] for arr in section_list])

    glist = [can for can in section_list if can[0] not in rem_set]

    for arr in section_list:
        if arr[0] in rem_set:
            for r, c in arr[1:]:
                grid[r][c]= -1

    return glist


    # print_grid(grid)
    # print(bio)

def move(glist):
    new_list = []
# 원점좌표
    for arr in glist:
        min_r, min_c = float("inf"), float("inf")
        key = arr[0]
        for r, c  in arr[1:]:
            if r< min_r:
                min_r = r
            if c <min_c:
                min_c = c
        for i  in range(1, len(arr)):
            arr[i][0]-=min_r
            arr[i][1]-=min_c
        new_list.append(arr)
        
# 영역, 먼저투입(키 작은) 순서대로 배치
    new_list.sort(key=lambda x: (-len(x[1:]), x[0]))

    final_list = []
# 차례대로 이동, 모든 영역이 범위 내, 그리드이 0보다 크지 않으면 
    new_grid = [[0]*N for _ in range(N)]
    
    for arr in new_list:
        is_placed = False
        key=arr[0]
        for sc in range(N):
            if is_placed: break
            for sr in range(N):
                can_placed = True
                for r, c in arr[1:]:
                    nr = r+sr
                    nc = c+sc
                    if not(0<=nr<N and 0<=nc<N and new_grid[nr][nc] == 0):
                        can_placed=False
                
                if can_placed:
                    for r, c in arr[1:]:
                        new_grid[r+sr][c+sc] = key
                    for i in range(1, len(arr)):
                        arr[i][0] +=sr
                        arr[i][1] +=sc

                    final_list.append(arr)
                    is_placed= True
                    break
    return new_grid ,final_list

    

def score(new_grid, final_list):
    area_dict ={}
    for arr in final_list:
        area_dict[arr[0]] = len(arr)-1
    pairs = set()
    for r in range(N):
        for c in range(N):
            if new_grid[r][c]>0:
                curr_id = new_grid[r][c]
                if r+1<N:
                    if new_grid[r+1][c] >0 and new_grid[r+1][c]!=curr_id:
                        pairs.add((min(new_grid[r+1][c], curr_id), max(new_grid[r+1][c], curr_id)))
                
                if c+1<N:
                    if new_grid[r][c+1] >0 and new_grid[r][c+1]!=curr_id:
                        pairs.add((min(new_grid[r][c+1], curr_id), max(new_grid[r][c+1], curr_id)))
                
    total_score = 0
    for id1, id2 in pairs:
        total_score+=area_dict[id1] * area_dict[id2]
    return total_score




for i in range(1,Q+1):
    # 미생물 투입, 둘 이상 나눠지면 해당 미생물은 사라짐
    adding(i)
    glist = inspecting()

    # 이동, 영역 넓은 > 먼저 투입 순서로 이동, 배양 용기 안벗어나고, 다른 미생물과 안겹치고 x 좌표 최소 > y좌표 최소, 불가능한 미생물은 삭제
    grid, final_list = move(glist)

    # 결과 기록, 맞닿으면 각 영역 곱만큼 성과
    sc = score(grid, final_list)

    print(sc)