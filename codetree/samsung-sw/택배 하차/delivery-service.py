import sys

# 입력받기
N, M = map(int, input().split())
grid = [[0]*N for _ in range(N)]
# key: [r, c], [r,c] 좌표들
box = {}

def find_position(grid, box, k):
    best_si = None
    for si in range(N):
        # for sj in range(N):
            # 모든 좌표가 범위내, 격자값이 0,
        if all(0<=si+r<N and grid[si+r][c]==0 for r, c in box[k]):
            best_si = si
        else:
            break
    return best_si, 0

def adding():
    k, h, w, c = map(int, input().split())
    box[k]=[]
    r=-1
    c-=1

    for i in range(h):
        for j in range(c, c+w):
            box[k].append([i, j])

    si, sj = find_position(grid, box, k)
    if si is None:
        return

    for idx in range(len(box[k])):
        r, c = box[k][idx]
        box[k][idx]=[si+r, sj+c]
        grid[si+r][sj+c]= k

def l_remove():
    candi=[]
    # box에 있는 박스들, 모든 좌표를 r=0으로 되도록 만들었을 때 놓을 수 있으면 후보에 넣기
    for key in box:
        # m_r = min(r for r , c in box[key])
        m_c = min(c for r, c, in box[key])
            # 모든 좌표들이 범위내, 그리드 0,
        can_remove=True
        for r, c in box[key]:

            if any(grid[r][col]!=0 for col in range(m_c)):
                can_remove=False
                break
        if can_remove:
            candi.append(key)
    if not candi:
        return None

        # 후보 중 key 값이 가장 작은애가 remove 대상
    candi.sort()
    lk = candi[0]
    for r, c in box[lk]:
        grid[r][c]=0
    del box[lk]
    return lk





def gravity():
    # 아래에서부터 순서 정하기
    # for r in range(N, 0, -1):
    #     if grid[r]>0 and :
    #         order

    # 아래에서부터 순서 정하기
    sorted_keys = sorted(box.keys(), key= lambda k: max(r for r, c in box[k]), reverse=True)

    # 위치찾고, 그리드 초기화, 추가, 딕트 갱신, 만약 변함없으면 그만
    for k in sorted_keys:
        for r, c in box[k]:
            grid[r][c]=0
        while True:
            can_drop = True
            for r, c in box[k]:
                if r + 1 >= N or grid[r + 1][c] != 0:
                    can_drop = False
                    break
            if not can_drop:
                break
            for idx in range(len(box[k])):
                box[k][idx][0] += 1
        for r, c in box[k]:
            grid[r][c]= k

def r_remove():
    candi=[]
    # box에 있는 박스들, 모든 좌표를 r=0으로 되도록 만들었을 때 놓을 수 있으면 후보에 넣기
    for key in box:
        # m_r = min(r for r , c in box[key])
        max_c = max(c for r, c, in box[key])
            # 모든 좌표들이 범위내, 그리드 0,
        can_remove=True
        for r, c in box[key]:
            if any(grid[r][col]!=0 for col in range(max_c+1, N)):
                can_remove=False
                break
        if can_remove:
            candi.append(key)
    if not candi:
        return None

        # 후보 중 key 값이 가장 작은애가 remove 대상
    candi.sort()
    rk = candi[0]
    for r, c in box[rk]:
        grid[r][c]=0
    del box[rk]
    return rk



for _ in range(M):
    adding()

while len(box)>0:
    lk = l_remove()
    if lk is not None:
        gravity()
        print(lk)
    if len(box) == 0:
            break
    rk = r_remove()
    if rk is not None:

        gravity()
        print(rk)