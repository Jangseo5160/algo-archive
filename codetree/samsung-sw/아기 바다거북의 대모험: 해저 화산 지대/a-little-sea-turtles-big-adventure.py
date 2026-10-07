"""

M마리 거북
N*N 안식처 N-1, N-1 좌표에 위치
최대 100턴 동안 진행

1단계: 바다거북 이동
ID 작은 순서대로 1번부터 최단경로 탐색
- 이동방해: 산호초 1, 바다거북(살아있는), 화석
- 최단경로 존재 안하면 제자리, 존재하면 우 하 좌 상 순서
- 안식처 도착: N-1, N-1 도착하면 지도에서 제외, 해당 ㅌㄴ을 도착시간으로 기록
- 해저 화산이 있는 칸으로 진입 가능, 앞선 결과는 다음 거북이의 경로 탐색에 반영

2단계: 화산 압력 증가
마그마 압력 10 증가. 모든 화산

3단계: 화산분출 및 연쇄반응
P 이상 압력은 열기 분출
- 열기전파: P만큼 열기 발생. 열기는 상하좌우 뻗음. 이전 칸 열기의 절반
- 산호초, 열기 0 되면 전파 중단
- 한칸에 여러 열기 있으면 합산

연쇄반응: 아직 분출안하는데, 현재 압력 +누적된 열기 >= P이면 즉시 분출
- 외부열기는 압력 수치 자체 증가는 없음
- 새로 분출하는 화산 없을 때까지 연쇄분출 반봅

바다거북 위치: 분출 종료 후 거북이 위치칸의 총 열기 합이 20 이상이면 화석
화석된 거북이는 고정, 장애물로 변함

4단계: 환경 초기화
열기 정보 사라짐. 분출 일으킨 모든 화산(연쇄반응도) 마그마 압력 0됨. 분출안한 화산은 그대로
"""
from collections import deque

N, M, K = map(int, input().split())
board = [[0]*N for _ in range(N)]
for i in range(N):
    board[i] = list(map(int, input().split()))

turtle_pos = [[0]*2 for _ in range(M)]
for i in range(M):
    turtle_pos[i] = list(map(int, input().split()))

volcano = [[0]*4 for _ in range(K)]
for i in range(K):
    volcano[i] = list(map(int, input().split()))
    volcano[i].append(0)

cnt=0
dead_turtle = set() # 죽은 거북 번호 저장
answer = [-1] * M

dr = [-1, 1, 0, 0] ## 상하좌우
dc = [0, 0, -1, 1]

def move():
    # 모든 거북이 움직임
    # 순ㅅ대로 이전 움직임 반영해야됨
    # 죽은 거북은 안움직임
    # 산호초, 죽은 거북, 산거북 보두 장애물 => 죽은거북은 움직이면 안됨
    for i in range(M):
        if i not in dead_turtle:
            sr, sc = turtle_pos[i]
            q=deque([(N-1, N-1)])
            dist = [[-1]*N for _ in range(N)]
            dist[N-1][N-1] = 0
            while q:
                cr, cc = q.popleft()
                for d in range(4):
                    nr, nc = cr+dr[d], cc+dc[d]
                    # 산호, 죽은, 산, 범위
                    if 0<=nr<N and 0<=nc<N and board[nr][nc]==0 and dist[nr][nc]==-1:
                        flag = False
                        for j in range(M):
                            if i==j: continue
                            else:
                                if turtle_pos[j] == [nr, nc]:
                                    flag = True
                                    break
                        if flag is False:
                            dist[nr][nc] = dist[cr][cc] + 1
                            q.append((nr, nc))

            if dist[sr][sc] == -1: # 못가는거니까 걍 넘김
                continue
            else:
                for nd in (3, 1, 2, 0):
                    nr, nc = sr+dr[nd], sc+dc[nd]
                    if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 0:
                        if dist[nr][nc] == dist[sr][sc]-1:
                            turtle_pos[i] = [nr, nc]
                            # 최종 입구 도착하면, cnt 반환할수있음. 걍 dead에 넣어서 관리
                            if (nr, nc) == (N-1, N-1):
                                global cnt
                                answer[i] = cnt
                                dead_turtle.add(i)
                                turtle_pos[i] = [-1, -1]
                            break


def charge():
    for i in range(K):
        volcano[i][3] += 10

def eruption():
    hot = [[0]*N for _ in range(N)]
    erupt = set()
    for i in range(K):
        if volcano[i][3]>= volcano[i][2]:
            erupt.add(i)
            ori_p=volcano[i][2]
            r,c = volcano[i][0], volcano[i][1]
            hot[r][c] += ori_p
            volcano[i][3] = 0
            for d in range(4):
                nr = r
                nc = c
                p = ori_p
                while True:
                    nr = nr+dr[d]
                    nc = nc+dc[d]
                    if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 0 and p > 0:
                        p //= 2
                        hot[nr][nc] += p
                    else: break

    for j in range(K):
        if j not in erupt:
            if volcano[j][3] + hot[volcano[j][0]][volcano[j][1]]>=volcano[j][2]:
                ori_p = volcano[j][2]
                r, c = volcano[j][0], volcano[j][1]
                hot[r][c] += ori_p
                volcano[j][3] = 0
                for d in range(4):
                    p = ori_p
                    nr, nc = r, c
                    while True:
                        nr = nr+dr[d]
                        nc = nc+dc[d]
                        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 0 and p > 0:
                            p //= 2
                            hot[nr][nc] += p
                        else: break
    for t in range(M):
        if t not in dead_turtle:
            tr, tc = turtle_pos[t][0], turtle_pos[t][1]
            if hot[tr][tc]>=20:
                dead_turtle.add(t)
                answer[t] = -1



while(cnt<100):
    cnt+=1

    move()
    charge()
    eruption()

for i in range(M):
    print(answer[i])



