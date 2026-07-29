from collections import deque
import sys
input = sys.stdin.readline

# 방향: 동, 서, 남, 북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

EAST = 0
WEST = 1
SOUTH = 2
NORTH = 3
TOP = 4

EMPTY = 0
WALL = 1
TIME_MACHINE = 2
CUBE = 3
EXIT = 4

INF = 10 ** 18


N, M, F = map(int, input().split())
area = []
for _ in range(N):
    temp = list(map(int, input().split()))
    area.append(temp)

# 동 서 남 북 위
time_faces = []
for _ in range(5):
    temp = []
    for m in range(M):
        temp.append(list(map(int, input().split())))
    time_faces.append(temp)
anomalies = []

for _ in range(F):
    r, c, d, v = map(int, input().split())
    anomalies.append([r, c, d, v])


def rotate_left(arr):
    size = len(arr)
    new_arr = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            new_arr[size - 1 - j][i] = arr[i][j]
    return new_arr

def rotate_right(arr):
    size = len(arr)
    new_arr = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            new_arr[j][size - 1 - i] = arr[i][j]

    return new_arr

def rotate_180(arr):
    size = len(arr)
    new_arr = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            new_arr[size - 1 - i][size - 1 - j] = arr[i][j]
    return new_arr

def paste(flat, piece, sy, sx):
    # print(piece)
    size = len(piece)
    for i in range(size):
        for j in range(size):
            flat[sy + i][sx + j] = piece[i][j]

# 전개도 만들기
flat = [[-1] * (3 * M) for _ in range(3 * M)]
east = rotate_left(time_faces[EAST])
west = rotate_right(time_faces[WEST])
north = rotate_180(time_faces[NORTH])
south = time_faces[SOUTH]
top = time_faces[TOP]

paste(flat, west, M, 0)
paste(flat, east, M, 2 * M)
paste(flat, north, 0, M)
paste(flat, south, 2 * M, M)
paste(flat, top, M, M)

# print(flat)

def check_side(r, c):
    if M <= r < 2 * M and 2 * M <= c < 3 * M:
        return EAST
    if M <= r < 2 * M and 0 <= c < M:
        return WEST
    if 2 * M <= r < 3 * M and M <= c < 2 * M:
        return SOUTH
    if 0 <= r < M and M <= c < 2 * M:
        return NORTH
    if M <= r < 2 * M and M <= c < 2 * M:
        return TOP
    return -1

# 중요 
def move_side(r, c):
    side = check_side(r, c)
    if side == EAST:
        if r == M:
            return 3 * M - c - 1, 2 * M - 1
        if r == 2 * M - 1:
            return c, 2 * M - 1
    elif side == WEST:
        if r == M:
            return c, M
        if r == 2 * M - 1:
            return 3 * M - c - 1, M
    elif side == SOUTH:
        if c == 2 * M - 1:
            return c, r
        if c == M:
            return 2 * M - 1, 3 * M - r - 1
    elif side == NORTH:
        if c == 2 * M - 1:
            return M, 3 * M - r - 1
        if c == M:
            return M, r
    return -1, -1

def bfs_time_wall():
    dist = [[INF] * (3 * M) for _ in range(3 * M)]
    q = deque()

    sy, sx = -1, -1

    for i in range(3 * M):
        for j in range(3 * M):
            if flat[i][j] == TIME_MACHINE:
                sy, sx = i, j
    dist[sy][sx] = 0
    q.append([sy, sx])

    while q:
        cy, cx = q.popleft()
        for d in range(4):
            ny = cy + dr[d]
            nx = cx + dc[d]
            if not (0 <= ny < 3 * M and 0 <= nx < 3 * M):
                continue
            if flat[ny][nx] == -1:
                ny, nx = move_side(cy, cx)
                if ny == -1:
                    continue
            if flat[ny][nx] == WALL:
                continue
            if dist[ny][nx] > dist[cy][cx] + 1:
                dist[ny][nx] = dist[cy][cx] + 1
                q.append([ny, nx])

    return dist

bfs_wall = bfs_time_wall()
#print(bfs_wall)

cube_r, cube_c = -1, -1

for i in range(N):
    for j in range(N):
        if area[i][j] == CUBE:
            cube_r, cube_c = i, j
            break
    if cube_r != -1:
        break

floor_exit_r, floor_exit_c = -1, -1
wall_exit_r, wall_exit_c = -1, -1

for k in range(M):
    fr, fc = cube_r - 1, cube_c + k
    wr, wc = 0, M + k

    if 0 <= fr < N and 0 <= fc < N:
        if area[fr][fc] in (EMPTY, EXIT):
            floor_exit_r, floor_exit_c = fr, fc
            wall_exit_r, wall_exit_c = wr, wc
    fr, fc = cube_r + M, cube_c + k
    wr, wc = 3 * M - 1, M + k
    if 0 <= fr < N and 0 <= fc < N:
        if area[fr][fc] in (EMPTY, EXIT):
            floor_exit_r, floor_exit_c = fr, fc
            wall_exit_r, wall_exit_c = wr, wc
    fr, fc = cube_r + k, cube_c - 1
    wr, wc = M + k, 0

    if 0 <= fr < N and 0 <= fc < N:
        if area[fr][fc] in (EMPTY, EXIT):
            floor_exit_r, floor_exit_c = fr, fc
            wall_exit_r, wall_exit_c = wr, wc
    fr, fc = cube_r + k, cube_c + M
    wr, wc = M + k, 3 * M - 1
    if 0 <= fr < N and 0 <= fc < N:
        if area[fr][fc] in (EMPTY, EXIT):
            floor_exit_r, floor_exit_c = fr, fc
            wall_exit_r, wall_exit_c = wr, wc


time = bfs_wall[wall_exit_r][wall_exit_c]

if time == INF:
    print(-1)
    sys.exit()

floor_start_time = time + 1
blocked_time = [[INF] * N for _ in range(N)]

for r, c, d, v in anomalies:
    t = 0

    # 시작 위치도 막힌다고 처리
    if blocked_time[r][c] > t:
        blocked_time[r][c] = t

    while True:
        t += v
        r += dr[d]
        c += dc[d]

        if not (0 <= r < N and 0 <= c < N):
            break

        # 이상현상은 빈 공간으로만 확산 가능하다고 보면 됨
        if area[r][c] != EMPTY:
            break

        if blocked_time[r][c] > t:
            blocked_time[r][c] = t


def bfs_floor():
    # 바닥으로 내려온 시작 칸이 이미 이상현상에 막혔으면 실패
    if floor_start_time >= blocked_time[floor_exit_r][floor_exit_c]:
        return -1

    dist = [[INF] * N for _ in range(N)]
    q = deque()

    dist[floor_exit_r][floor_exit_c] = floor_start_time
    q.append([floor_exit_r, floor_exit_c])

    # 시작 칸이 바로 최종 출구인 경우
    if area[floor_exit_r][floor_exit_c] == EXIT:
        return floor_start_time

    while q:
        cy, cx = q.popleft()

        for d in range(4):
            ny = cy + dr[d]
            nx = cx + dc[d]

            if not (0 <= ny < N and 0 <= nx < N):
                continue

            # 바닥에서는 EMPTY 또는 EXIT만 이동 가능
            if area[ny][nx] not in (EMPTY, EXIT):
                continue

            nt = dist[cy][cx] + 1

            # 이상현상이 같은 시간 또는 더 먼저 도착한 칸이면 못 감
            if nt >= blocked_time[ny][nx]:
                continue

            if dist[ny][nx] <= nt:
                continue

            dist[ny][nx] = nt

            if area[ny][nx] == EXIT:
                return nt

            q.append([ny, nx])

    return -1
answer = bfs_floor()
print(answer)
