from collections import deque, Counter
# 미생물 투입
# 덮어씌기, 둘 이상 나눠지면 사라짐

# 배양 용기 이동
# 영역 넓은 무리 > 먼저 투입된거 > 다른 미생물과 겹치지 않게, 범위 벗어나지 않게, x 최소 > y 최소, 둘 수 없는 미생물은 사라짐

# 실험 결과 기록
# 인접한 물리 쌍, A 넓이 * B 넓이

N, Q = map(int, input().split())
cells = {}
board = [[-1]*N for _ in range(N)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]

for k in range(Q):
    r1,c1,r2,c2 = map(int, input().split())
    cells[k] = [r1,c1,r2,c2]

def add_cell(k):
    r1,c1,r2,c2 = cells[k]
    for i in range(r1, r2):
        for j in range(c1, c2):
            board[i][j]=k

def delete_if_seperate(board):
    visited = [[False] * N for _ in range(N)]
    group = []
    for i in range(N):
        for j in range(N):
            if board[i][j] !=-1 and not visited[i][j]:
                key = board[i][j]
                group.append(key)
                q = deque([(i, j)])
                visited[i][j] = True
                while q:
                    r, c = q.popleft()
                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                            if board[nr][nc] == key:
                                visited[nr][nc]=True
                                q.append((nr, nc))

    counts = Counter(group)
    candidate={k for k, cnt in counts.items() if cnt >1}

    # 한개 이상이면 삭제
    # k였던 좌표들 모두 -1로 채우기
    if candidate:
        for i in range(N):
            for j in range(N):
                if board[i][j] in candidate:
                    board[i][j] = -1

# 이동 순서 결정
def order():
    visited=[[-1]*N for _ in range(N)]
    ordered = []
    positions = {}

    for i in range(N):
        for j in range(N):
            key = board[i][j]
            if key!=-1:
                if key not in positions:
                    positions[key] =[]
                positions[key].append((i, j))

    ordered = sorted(positions, key = lambda k: (-len(positions[k]),k))
    return ordered, positions

def move_cell():
    new_board= [[-1]*N for _ in range(N)]
    ordered, positions = order()
    for key in ordered:
        coords = positions[key]
        min_r = min(r for r, c in coords)
        min_c = min(c for r, c in coords)

        shape = [(r-min_r, c-min_c) for r, c in coords]

        r_size = max(r for r, c in shape) +1
        c_size = max(c for r, c in shape) +1
        placed = False
        for r in range(N-r_size+1):
            for c in range(N-c_size+1):
                can_place = True
                for rr, cc in shape:
                    if new_board[r+rr][c+cc] !=-1:
                        can_place=False
                        break
                if can_place:
                    for rr, cc in shape:
                        new_board[r+rr][c+cc] = key
                    placed = True
                    break
            if placed:
                break
    return new_board

def calculate_score():
    area = [0]*Q
    pairs=set()
    for r in range(N):
        for c in range(N):
            key = board[r][c]
            if key!=-1:
                area[key]+=1
                for d in range(4):
                    nr, nc = r+dr[d], c+dc[d]
                    if 0<=nr<N and 0<=nc<N and board[nr][nc]!=-1 and board[nr][nc]!=key:
                        pairs.add((min(key, board[nr][nc]), max(key, board[nr][nc])))
    score= 0
    for a,b in pairs:
        score += area[a]*area[b]
    return score


for k in range(Q):
    add_cell(k)
    delete_if_seperate(board)
    board = move_cell()
    print(calculate_score())


