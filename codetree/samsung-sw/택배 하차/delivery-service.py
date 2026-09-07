N, M = map(int, input().split())
board = [[0] * N for _ in range(N)]
boxes = {}
answer = []

def can_fall(r, c, h, w):
    if r+h == N:
        return False
    for j in range(c, c+w):
        if board[r+h][j]!=0:
            return False
    return True

def can_remove_left(k):
    r,c,h,w = boxes[k]
    for i in range(r, r+h):
        for j in range(c):
            if board[i][j] !=0:
                return False
    return True
def can_remove_right(k):
    r,c,h,w = boxes[k]
    for i in range(r, r+h):
        for j in range(c+w, N):
            if board[i][j] !=0:
                return False
    return True

def remove_box(k):
    r,c,h,w = boxes[k]
    for i in range(r, r+h):
        for j in range(c, c+w):
            board[i][j]=0
    del boxes[k]
def gravity():
    order = sorted(boxes.keys(), key = lambda k: boxes[k][0]+boxes[k][2], reverse=True)
    for k in order: # order는 list,k 는 인덱스?
        r,c,h,w = boxes[k]
        for i in range(r, r+h):
            for j in range(c, c+w):
                board[i][j]=0
        
        while can_fall(r, c, h, w):
            r+=1
        boxes[k]=[r,c,h,w]
        for i in range(r, r+h):
            for j in range(c, c+w):
                board[i][j]=k
    

for _ in range(M):
    k, h, w, c = map(int, input().split())
    c-=1

    r=0
    while can_fall(r, c, h, w):
        r+=1
    boxes[k] = [r, c, h, w]
    for i in range(r, r+h):
        for j in range(c, c+w):
            board[i][j]=k

while boxes:
    candidates = []
    for k in boxes:
        if can_remove_left(k):
            candidates.append(k)
    if candidates:
        k=min(candidates)
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
        k=min(candidates)
        remove_box(k)
        answer.append(k)
        gravity()
    if not boxes:
        break
for k in answer:
    print(k)
        
