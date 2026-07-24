import sys
from collections import deque
from collections import Counter

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
    bio[i] = [si, sj, ei, ej] # row 먼저, col 두번째로 배치
    for r in range(si, ei):
        for c in range(sj, ej):
            grid[r][c] = i

# 구역별로 section에 [key, [r,c], [r,c] .. ] 하는 bfs
def bfs(r, c, v, grid):
    # bfs에 튜플을 넣을지, 리스트를 넣을지
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

# 쪼개진지 검사하는게 필요, bfs는 따른 함수로 빼두기
def inspecting(): 
    v = [[False]*N for _ in range(N)]
    section_list = []

    # grid 변경되었으니, bfs 돌리면서 bio 별로 좌표 리스트 추가해주고, 만약 쪼개지면 아예 없애주는거
    for r in range(N):
        for c in range(N):   
            if grid[r][c]>0 and v[r][c] is False:
                
                section = bfs(r, c, v, grid)
                section_list.append(section)

    

    # for arr in section_list:
    #     for brr in section_list:
    #         # arr이 brr이랑 다르고, 키가 같을때
    #         if arr != brr and arr[0]==brr[0]:
    #             rem_set.add(arr[0])

    rem_set= set()
    cnt = Counter(arr[0] for arr in section_list)
    rem_set = {key for key, c in cnt.items() if c>1}

    glist = [arr for arr in section_list if arr[0] not in rem_set]

    for arr in section_list:
        if arr[0] in rem_set:
            for r, c in arr[1:]:
                grid[r][c]= -1

    return glist

def move(glist):
    new_list = []
# 원점좌표
    for arr in glist:
        min_r = min(r for r, c in arr[1:])
        min_c = min(c for r, c in arr[1:])
        for i  in range(1, len(arr)):
            arr[i][0]-=min_r
            arr[i][1]-=min_c
        new_list.append(arr)
        
# 영역, 먼저투입(키 작은) 순서대로 배치
    new_list.sort(key=lambda x: (-len(x[1:]), x[0]))

# 차례대로 이동, 모든 영역이 범위 내, 그리드이 0보다 크지 않으면 
    new_grid = [[0]*N for _ in range(N)]
    final_list = []

    for arr in new_list:
        is_placed = False
        key=arr[0]
        shape = arr[1:]
        sr, sc = find_position(shape, new_grid)
        if sr is not None:
            for r, c in shape:
                new_grid[r+sr][c+sc] = key
            final_list.append(arr)
    return new_grid ,final_list

def find_position(shape, new_grid):
    # 순서 바꿔서, 문제에서 col 작은거 > row 작은거 순으로 배치
    # 탐색 순서가 정렬 순서랑 같다!
    for sc in range(N):
        for sr in range(N):
            # 모든 좌표가 유효한지 검사할 때
            if all(0<=r+sr<N and 0<=c+sc<N and new_grid[r+sr][c+sc] == 0 for r, c in shape):
                return sr, sc
    return None, None
    


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
    

############################3

# from collections import deque, defaultdict
# N, Q = map(int, input().split())
# # 미생물 저장할 배열
# A = [[0] * N for _ in range(N)]
# def insert(num, r1, c1, r2, c2):
#     for r in range(r1, r2):
#         for c in range(c1, c2):
#             A[r][c] = num
# dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
# def in_range(r, c):
#     return 0 <= r < N and 0 <= c < N
# # BFS
# def BFS(r, c):
#     # 상대적인 위치
#     res = []
#     q = deque()
#     num = A[r][c]
#     q.append((r, c))
#     #visited 대신 0으로 바꿔주는 거로 함
#     A[r][c] = 0
#     res.append((0, 0))
#     while q:
#         now_r, now_c = q.popleft()
#         for dx, dy in dxy:
#             nx, ny = now_r + dx, now_c + dy
#             if in_range(nx, ny) and A[nx][ny] == num:
#                 q.append((nx, ny))
#                 A[nx][ny] = 0
#                 res.append((nx - r, ny - c))
#     return num, res
# # 모든 칸을 순회하면서, 만약 미생물이 있으면 BFS를 돌아서 상대적 위치를 모두 알아낸다.
# def get_groups():
#     # 돌았으면 번호 0으로 바꿔주기
#     res = []
#     num_cnt = defaultdict(int)
#     # 각 번호의 개수를 새야 함
#     for i in range(N):
#         for j in range(N):
#             if A[i][j] != 0:
#                 num, groups = BFS(i, j)
#                 res.append((num, groups))
#                 num_cnt[num] += 1
                
#     # 2개 이상있는 번호는 제외하고, 반환
#     return [(num, group) for num, group in res if num_cnt[num] == 1]
# def get_possible_position(group):
#     for i in range(N):
#         for j in range(N):
#             flag = True
#             for dx, dy in group:
#                 nx, ny = i+dx, j+dy
#                 if not (in_range(nx, ny) and A[nx][ny] == 0):
#                     flag = False
#                     break
#             if flag:
#                 return i, j
#     return None, None
# def move():
#     groups = get_groups()
#     groups.sort(key=lambda x: (-len(x[1]), x[0]))
#     for num, group in groups:
#         r, c = get_possible_position(group)
#         if r is not None:
#             for dx, dy in group:
#                 A[r+dx][c+dy] = num
#     return groups
# def get_score(group_cnt):
#     num_pairs = set()
#     for r1 in range(N):
#         for c1 in range(N):
#             for r2, c2 in [(r1+1, c1), (r1, c1+1)]:
#                 if in_range(r2, c2) and A[r1][c1] != A[r2][c2] and A[r1][c1] != 0 and A[r2][c2] != 0:
#                     n1 = A[r1][c1]
#                     n2 = A[r2][c2]
#                     # 중복 제거
#                     num_pairs.add((min(n1, n2), max(n1, n2)))
#     answer = 0
#     for n1, n2 in num_pairs:
#         answer += group_cnt[n1] * group_cnt[n2]
#     return answer
# # 미생물 투입. turn: 미생물 번호
# for turn in range(1, Q+1):
#     r1, c1, r2, c2 = map(int, input().split())
#     insert(turn, r1, c1, r2, c2)
#     groups = move()
#     group_cnt = {
#         num : len(group)
#         for num, group in groups
#     }
#     # for a in A:
#     #     print(*a)
#     # print()
#     print(get_score(group_cnt))


