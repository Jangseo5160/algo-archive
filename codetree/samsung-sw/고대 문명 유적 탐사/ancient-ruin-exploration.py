'''
고대 문명 유적
5*5 형태
유물 조각 배치
7가지 종류
1~7 표현

1. 탐사 진행
3*3 격자 선택. 격자 회전은 90, 180, 270도 중 하나. 항상 회전 하나는 해야됨
회전 선택 조건: 유물 획득 가치 최대화>회전각도 작은거> 열 작은거, 행 작은거 선택

2. 유물획득
1차: 상하좌우로 인접하게 모임. 3개 이상 연결된 경우 유물 모여서 사라짐. 유물 가치는 모인 조각 개수와 같음
1~7까지 숫자 M개 열번호 작은거부터>행번호 큰순서대로 조각 넣어줌
이 조각은 없어진거.

유물 연쇄 획득: 새로운 조각 넣어주면 3개 이상 연결 가능. 더이상 3개 이상 연결되지 않을때까지 반복

3. 탐사반복
탐사진행~연쇄획득을 1턴으로, 총 K번 진행
각 턴마다 획득한 유물 가치 총합 출력.
K번까지 전에도, 탐사진행했는데 유물 획득가치가 없으면 즉시 종료. 이때 종료되는 턴에 아무값도 출력하지 않음
'''
from collections import deque
from pydoc import visiblename

K, M = map(int, input().split())
board = [[0]*5 for _ in range(5)]

for i in range(5):
    board[i] = list(map(int, input().split()))

wall=deque()
n = list(map(int, input().split()))
for num in n:
    wall.append(num)

answer = []
dr = [-1,1,0,0]
dc = [0,0,-1,1]


def bfs(temp):
    cnt = 0
    visited = [[False]*5 for _ in range(5)]
    pos_set = set()
    for r in range(5):
        for c in range(5):
            if visited[r][c] is False:
                q=deque([(r, c)])
                visited[r][c]=True
                temp_s=1
                pos = set()
                pos.add((r, c))
                while q:
                    cr, cc = q.popleft()
                    for d in range(4):
                        nr=cr+dr[d]
                        nc=cc+dc[d]
                        if 0<=nr<5 and 0<=nc<5 and visited[nr][nc] is False and temp[r][c] == temp[nr][nc]:
                            q.append((nr, nc))
                            visited[nr][nc] = True
                            temp_s+=1
                            pos.add((nr, nc))
                if temp_s>=3:
                    cnt+=temp_s
                    for (pr, pc) in pos:
                        pos_set.add((pr, pc))
    return cnt, pos_set

def rotate90(array, r, c, times):
    new = [row[:] for row in array]
    sub = [array[i][c-1:c+2] for i in range(r-1, r+2)]
    for _ in range(times):
        sub = [list(row) for row in zip(*sub[::-1])]
    for i in range(3):
        for j in range(3):
            new[r-1+i][c-1+j] = sub[i][j]
    return new

def explore(board):
    group = set()
    temp = [row[:] for row in board]
    for d in range(1, 4):
        for r in range(1, 4):
            for c in range(1, 4):
                new = rotate90(board, r, c, d)
                count, _ = bfs(new)
                if count>0:
                    group.add((count, -d, -c, -r))
    if len(group)>0:
        fcnt, neg_fd, neg_fc, neg_fr = max(group)
        r = -neg_fr
        c = -neg_fc
        new = rotate90(board, -neg_fr, -neg_fc, -neg_fd)
        return fcnt, new
    else: return 0, board

def score(board):
    total = 0
    while True:
        cnt, pos_set = bfs(board)
        if cnt==0: break
        total+=cnt
        for (r, c) in pos_set:
            board[r][c] = -1

        for c in range(5):
            for r in range(4, -1, -1):
                if board[r][c] == -1:
                    board[r][c] = wall.popleft()
    return total


for _ in range(K):
    cnt, board = explore(board) # board 상태 변화
    if cnt==0:
        break
    total = score(board) # cnt 올라가고, 그자리 wall에서 채우고, 또 가능한지 확인하고 또 wall 채우고. cnt가 0이라면 그만
    answer.append(total)
print(*answer)

# 4 8 6 3 3 3 12 9 7 14