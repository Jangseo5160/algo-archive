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

def add_cells(k):
    r1, c1, r2, c2=cells[k]
    for i in range(r1, r2):
        for j in range(c1, c2):
            board[j][i] = k
    # r1, c1, r2, c2

def remove_seperate(board):
    visited=[[False]*N for _ in range(N)]
    candidate = []
    for i in range(N):
        for j in range(N):
            if board[i][j]!=-1 and not visited[i][j]:
                key = board[i][j]
                candidate.append(key)
                q=deque([(i, j)])
                visited[i][j]=True
                while q:
                    r, c = q.popleft()
                    for d in range(4):
                        nr, nc = r+dr[d], c+dc[d]
                        if 0<=nr<N and 0<=nc<N and board[nr][nc]==key and not visited[nr][nc]:
                            q.append((nr, nc))
                            visited[nr][nc]=True
    can_list = Counter(candidate)
    remove_dict = {k for k, cnt in can_list.items() if cnt>1}
    if remove_dict:
        for i in range(N):
            for j in range(N):
                if board[i][j] in remove_dict:
                    board[i][j]=-1

def move_order():
    order_list = []
    positions={}

    for i in range(N):
        for j in range(N):
            if board[i][j]!=-1:
                key = board[i][j]
                if key not in positions:
                    positions[key]=[]
                positions[key].append((i, j))
    order_list=sorted(positions, key=lambda k: (-len(positions[k]), k))
    return order_list, positions

def move_cells():
    order_list, positions = move_order()
    new_board=[[-1]*N for _ in range(N)]
    for key in order_list:
        min_r = min(r for r, c in positions[key])
        min_c = min(c for r, c in positions[key])
        shape = [(r-min_r, c-min_c) for r, c in positions[key]]
        r_size = max(r for r, c in shape)+1
        c_size = max(c for r, c in shape)+1
        is_placed = False
        for i in range(N-c_size+1):
            for j in range(N-r_size+1):
                can_place = True
                for (r, c) in shape:
                    if new_board[j+r][i+c]!=-1:
                        can_place = False
                        break
                if can_place:
                    for (r, c)in shape:
                        new_board[j+r][i+c] = key
                    is_placed = True
                    break
            if is_placed:
                break
    return new_board

def score():
    area = [0]*Q
    pair = set()
    for r in range(N):
        for c in range(N):
            key = board[r][c]
            if key!=-1:
                area[key]+=1
                for d in range(4):
                    nr, nc = r+dr[d], c+dc[d]
                    if 0<=nr<N and 0<=nc<N and board[nr][nc]!=-1 and board[nr][nc]!=key:
                        pair.add((min(key,board[nr][nc]), max(key, board[nr][nc])))
    score = 0
    for a, b in pair:
        score += area[a] * area[b]
    return score

for k in range(Q):
    add_cells(k)
    remove_seperate(board)
    board = move_cells()
    print(score())