# 신봉음식 Fij
# T, C, M
# 신앙심 Bij
# T일동안 아침,점심,저녁
# 아침: 모든 학생 신앙심 Bij +=1
from collections import deque
food = {'T': 100, 'C':10, 'M':1, 'CM': 11, 'TM':101, 'TC': 110, 'TCM': 111}

def breakfast(belif_board):
    for i in range(N):
        for j in range(N):
            belif_board[i][j]+=1

# 점심: 신봉음식같은 그룹에서 대표자 선정, Bij 큰>i 가장 작은 > c가장 작은
# 대표자+= 자신 제외 그룹멤버수, 그룹멤버 신앙심-=1

dr = [-1, 1, 0,0]
dc = [0, 0, -1,1]

def lunch(belif_board):
    visited=[[False]*N for _ in range(N)]
    leader = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                k = food_board[i][j]
                q=deque([(i,j)])
                visited[i][j]=True
                member = []
                member.append((-belif_board[i][j], i, j))
                while q:
                    r, c = q.popleft()
                    for d in range(4):
                        nr, nc = r+dr[d], c+dc[d]
                        if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and food_board[nr][nc]==k:
                            visited[nr][nc]=True
                            q.append((nr, nc))
                            member.append((-belif_board[nr][nc], nr, nc))
                _, leader_r, leader_c = min(member)
                leader.append((leader_r, leader_c))
                for _, r, c in member:
                    if (r, c) == (leader_r, leader_c):
                        belif_board[r][c]+=(len(member)-1)
                    else:
                        belif_board[r][c]-=1
    return leader


# 저녁: 대표자들이 신앙 전파, 단일>이중>삼중, 같은 그룹내 대표자 신앙심 큰>행번호 작은>열번호 작은
# 전파자(대표자) 신앙심 B = 1, x=B-1, x만큼 전파하는데 사용, B%4 = 0,1,2,3 => 위, 아래, 왼쪽 오른쪽
# 격자밖 or x<=0 => 전파 종료, 전파 대상이 신봉음식이 전파자와 같으면 다음으로 진행, 다를 때만 전파
# 전파 대상 신봉음식이 전파자와 다를때, 전파대상 신앙심 y
# x>y : 강한전파, 전파대상 신봉음식 = 전파자 신봉음식, x-=(y+1), y+=1, x<=0 => 종료
# x<=y : 약한 전파, 전파대상 신봉음식 + 전파자 신봉음식, x=0, y+=x, 전파 종료

def dinner(food_board,belif_board ):
    leader = lunch(belif_board)
    one_list = []
    two_list = []
    three_list = []
    blocked = set()
    for r,c in leader:
        # food 단일
        if food_board[r][c] == 100 or food_board[r][c] == 10 or food_board[r][c] == 1:
            one_list.append((-belif_board[r][c], r, c))
        # food 이중
        elif food_board[r][c] == 11 or food_board[r][c] == 101 or food_board[r][c] == 110:
            two_list.append((-belif_board[r][c], r, c))
        # food 삼중
        elif food_board[r][c] == 111:
            three_list.append((-belif_board[r][c], r, c))
    if one_list:
        one_list.sort()
    if two_list:
        two_list.sort()
    if three_list:
        three_list.sort()
    total_list = []
    total_list = one_list+two_list+three_list
    for neg_B, r, c in total_list:
        if (r, c) not in blocked:
            x=-neg_B-1
            belif_board[r][c] = 1
            d = (-neg_B)%4
            stop = False
            nr=r
            nc=c
            while True:
                nr, nc = nr+dr[d], nc+dc[d]
                if nr<0 or nr>=N or nc<0 or nc>=N or x<=0:
                    stop=True
                    break
                if food_board[nr][nc] != food_board[r][c]:
                    y=belif_board[nr][nc]
                    if x>y:
                        food_board[nr][nc] = food_board[r][c]
                        x -= (y + 1)
                        y += 1
                        belif_board[nr][nc] = y
                        blocked.add((nr, nc))
                        if x<=0:
                            stop = True
                    elif x<=y:
                        food_board[nr][nc] |= food_board[r][c]
                        y += x
                        x = 0
                        belif_board[nr][nc] = y
                        blocked.add((nr, nc))
                        stop = True
                if stop:
                    break


# 각 저녁 끝나면 신봉음식 순서대로 신앙심 출력
def score(food_board, belif_board):
    score = [0]*7
    for i in range(N):
        for j in range(N):
            if food_board[i][j] == 111:
                score[0]+=belif_board[i][j]
            if food_board[i][j] == 110:
                score[1]+=belif_board[i][j]
            if food_board[i][j] == 101:
                score[2]+=belif_board[i][j]
            if food_board[i][j] == 11:
                score[3]+=belif_board[i][j]
            if food_board[i][j] == 1:
                score[4]+=belif_board[i][j]
            if food_board[i][j] == 10:
                score[5]+=belif_board[i][j]
            if food_board[i][j] == 100:
                score[6]+=belif_board[i][j]
    return score

N, T = map(int, input().split())
food_board = [[0]*N for _ in range(N)]
belif_board = [[0]*N for _ in range(N)]


for i in range(N):
    temp = list(map(str, input().strip()))
    for j in range(N):
        food_board[i][j] = food[temp[j]]

for i in range(N):
    belif_board[i] = list(map(int, input().split()))

for _ in range(T):
    breakfast(belif_board)
    # lunch(belif_board)
    dinner(food_board, belif_board)
    scores = score(food_board, belif_board)
    print(*scores)

