N, M = map(int, input().split())
boxes = {} # k -> [r, c, w, h]
board = [[0]*(N) for _ in range(N)]
answer = []

def can_fall(r, c, w, h):
    if r+h == N:
        return False
    for j in range(c, c+w):
        if board[r+h][j] !=0:
            return False
    return True

# 택배 투입
for _ in range(M):
    k, h, w, c = map(int, input().split())
    c-=1

    # 떨어질 위치 찾기
    r=0
    while can_fall(r, c, w, h):
        r+=1

    boxes[k] = [r ,c, w, h]
    for i in range(r, r+h):
        for j in range(c, c+w):
            board[i][j] = k

def can_remove_left(k):
    r, c, w, h = boxes[k]
    for i in range(r, r+h):
        for j in range(c):
            if board[i][j]!=0:
                return False
    return True
def can_remove_right(k):
    r, c, w, h = boxes[k]
    for i in range(r, r+h):
        for j in range(c+w, N):
            if board[i][j]!=0:
                return False
    return True

def remove_box(k):
    r,c,w,h = boxes[k]
    for i in range(r, r+h):
        for j in range(c, c+w):
            board[i][j] = 0
    del boxes[k]

def gravity():
    order= sorted(boxes.keys(), key = lambda k: boxes[k][0] + boxes[k][3], reverse=True)
    for k in order:
        r, c, w, h = boxes[k]
        for i in range(r, r+h):
            for j in range(c, c+w):
                board[i][j]=0
        while can_fall(r,c,w,h):
            r+=1
        boxes[k] = [r,c,w,h]
        for i in range(r, r+h):
            for j in range(c, c+w):
                board[i][j]=k

while boxes:
    candidates = []
    for k in boxes:
        if can_remove_left(k):
            candidates.append(k)
    if candidates:
        k = min(candidates)
        remove_box(k)
        answer.append(k)
        gravity()
    if not boxes:
        break
    candidates = []
    for k in boxes:
        if can_remove_right(k):
            candidates.append(k)
    if candidates:
        k = min(candidates)
        remove_box(k)
        answer.append(k)
        gravity()
    if not boxes:
        break

for k in answer:
    print(k)


# 택배하차 - 좌측
# 왼쪽 뚫려있는것, k작은것, 중력

# 택배하차 - 우측
# 오른쪽 뚫려있는것, k작은것, 중력