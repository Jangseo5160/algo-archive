from collections import deque
from multiprocessing.resource_sharer import stop

# 집 -> 산책, 집은 Sr, Sc, 공원은 Er, Ec
# 도로는 0, 도로 아니면 1
'''
각 전사들은 메두사를 향해 최단 경로
전사는 도로, 비도록 구분 안함

'''
'''
# 메두사 이동
도로를 따라 한칸 이동, er, ec까지 최단 경로, 이동칸이 전사라면, 전사는 사라짐
상하좌우 순서대로 최단경로 감
집->공원까지 갈수있는 경로 없을수도 있음

# 메두사시선
상하좌우 하나 선택해서 바라봄
대각방향 채우며 삼각형 모양으로 넒어짐
메두사가 본 전사들은모두 돌로 변해서 이번 턴 못움직이고, 턴 종료되야지 풀림
두명 이상이 같은 위치에 있다면, 둘다 돌로 변함
상하좌우중, 볼수있는 전사가 가장 많은 방향 바라봄
만약 같은 수라면, 상하좌우 우선순위로 방향 결정함.

# 전사들 이동
돌로 변하지 않은 전사들은 메두사 향해서최대 두칸이동
첫번째 이동은 메두사와 거리 줄일 수 있는 방향으로. 상하좌우 우선순위로 방향 선택. 격자 안에서 이동. 메두사 시야 들어오는 곳이면 이동 안됨
두번째 이동은 메두사와 거리 줄일 수 있는 곳인데, 이번엔 좌우상화 우선순위로. 격자 안에서. 메두사 시야에 들어오는 곳이면 이동 안됨

# 전사 공격
메두사와 같은 칸에 도달한 전사는 메두사 공격하고 죽음

# 출력
메두사가 공원 도달할 때까지 매 턴. 모든 전사 이동 거리합. 메두사로 인해 돌이 된 전사 수. 메두사가 공격한 전사 수.
메두사 공원 도착하면 0 출력 후 종료. 도로 존재 안하면 -1

'''


N, M = map(int, input().split())
sr, sc, er, ec = map(int, input().split())
s = list(map(int, input().split()))
soldier = [0] *M
for i in range(M):
    soldier[i] = (s[2*i], s[2*i+1])
board = [[0]*N for _ in range(N)]
for i in range(N):
    board[i] = list(map(int, input().split()))


'''
# 메두사 이동
도로를 따라 한칸 이동, er, ec까지 최단 경로, 이동칸이 전사라면, 전사는 사라짐
상하좌우 순서대로 최단경로 감
집->공원까지 갈수있는 경로 없을수도 있음
'''
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def move_snail(sr, sc):
    #er, ec까지 최단경로로 가능데, 동일한 최단경로라면 상하좌우로 가고, 불가능한 경우도 체크.
    #메두사 이동 위치에 전사있으면 공격받고 사라짐
    #(dist, d, nr, nc) tuple 정렬하기
    dist = [[-1]*N for _ in range(N)]
    q=deque([(er, ec)])
    dist[er][ec] =0
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r+dr[d],c+dc[d]
            if 0<=nr<N and 0<=nc<N and dist[nr][nc]==-1 and board[nr][nc]==0:
                dist[nr][nc] = dist[r][c]+1
                q.append((nr, nc))
    if dist[sr][sc] ==-1:
        return -1, -1, 0
    new_position = set()
    for d in range(4):
        nr = sr+dr[d]
        nc = sc+dc[d]
        if 0<=nr<N and 0<=nc<N and board[nr][nc]==0 and dist[nr][nc]!=-1:
            new_position.add((dist[nr][nc], d))
    _, final_d = min(new_position)
    sr = sr+dr[final_d]
    sc = sc+dc[final_d]
    alive = []
    for idx, (r, c) in enumerate(soldier):
            if (r, c) != (sr, sc):
                alive.append((r, c))


    return sr, sc, alive

'''
# 메두사시선
상하좌우 하나 선택해서 바라봄
대각방향 채우며 삼각형 모양으로 넒어짐
메두사가 본 전사들은모두 돌로 변해서 이번 턴 못움직이고, 턴 종료되야지 풀림
두명 이상이 같은 위치에 있다면, 둘다 돌로 변함
상하좌우중, 볼수있는 전사가 가장 많은 방향 바라봄
만약 같은 수라면, 상하좌우 우선순위로 방향 결정함.
'''
def down(sr, sc, soldier):
    blocked = set()  # block 좌표
    shadow = set()  # 탐색 안할 좌표돌
    region = set()
    # sr, sc
    for r in range(sr+1, N):
        gap = abs(r-sr)
        # 가운데
        if (r, sc) not in shadow:
            region.add((r, sc))
            # 전사 만나면 그 뒤에 섀도우 지역 shadow에 넣어서, 나중에 탐색할 때 shadow면 아예 탐색 안하도록
            if (r, sc) in soldier:
                blocked.add((r, sc))
                for temp_r in range(r+1, N):
                    if 0<=temp_r<N:
                        shadow.add((temp_r, sc))
                    # 전사든 아니든, 일단 그 지역이 shadow가 아니라면 region에 넣음

        # 오른쪽
        for rc in range(sc+1, sc+gap+1):
            if 0<=rc<N:
                if(r, rc) not in shadow:
                    region.add((r, rc))
                    # 전사 만났을 떄
                    if (r, rc) in soldier:
                        blocked.add((r, rc))
                        for temp_r in range(r+1, N):
                            shadow.add((temp_r, rc))
                            temp_gap = abs(temp_r-r)
                            for temp_c in range(rc+1,rc+temp_gap+1):
                                if 0<=temp_c<N:
                                    shadow.add((temp_r, temp_c))
        # 왼쪽
        for lc in range(sc-1, sc-(gap+1), -1):
            if 0<=lc<N:
                if(r, lc) not in shadow:
                    region.add((r, lc))
                    # 전사 만났을 떄
                    if (r, lc) in soldier:
                        blocked.add((r, lc))
                        for temp_r in range(r+1, N):
                            shadow.add((temp_r, lc))
                            temp_gap = abs(temp_r-r)
                            for temp_c in range(lc-1,lc-temp_gap-1, -1):
                                if 0<=temp_c<N:
                                    shadow.add((temp_r, temp_c))
    block_soldier = set()
    for idx, (r, c) in enumerate(soldier):
        if (r, c) in blocked:
            block_soldier.add(idx)
    return region, block_soldier

def up(sr, sc, soldier):
    blocked = set()  # block 좌표
    shadow = set()  # 탐색 안할 좌표돌
    region = set()
    # sr, sc
    for r in range(sr-1, -1, -1):
        gap = abs(r-sr)
        # 가운데
        if (r, sc) not in shadow:
            region.add((r, sc))
            # 전사 만나면 그 뒤에 섀도우 지역 shadow에 넣어서, 나중에 탐색할 때 shadow면 아예 탐색 안하도록
            if (r, sc) in soldier:
                blocked.add((r, sc))
                for temp_r in range(r-1, -1,-1):
                    if 0<=temp_r<N:
                        shadow.add((temp_r, sc))

        # 오른쪽
        for rc in range(sc+1, sc+gap+1):
            if 0<=rc<N:
                if(r, rc) not in shadow:
                    region.add((r, rc))
                    # 전사 만났을 떄
                    if (r, rc) in soldier:
                        blocked.add((r, rc))
                        for temp_r in range(r-1, -1,-1):
                            shadow.add((temp_r, rc))
                            temp_gap = abs(temp_r-r)
                            for temp_c in range(rc+1,rc+temp_gap+1):
                                if 0<=temp_c<N:
                                    shadow.add((temp_r, temp_c))
        # 왼쪽
        for lc in range(sc-1, sc-(gap+1), -1):
            if 0<=lc<N:
                if(r, lc) not in shadow:
                    region.add((r, lc))
                    # 전사 만났을 떄
                    if (r, lc) in soldier:
                        blocked.add((r, lc))
                        for temp_r in range(r-1, -1,-1):
                            shadow.add((temp_r, lc))
                            temp_gap = abs(temp_r-r)
                            for temp_c in range(lc-1,lc-temp_gap-1, -1):
                                if 0<=temp_c<N:
                                    shadow.add((temp_r, temp_c))
    block_soldier = set()
    for idx, (r, c) in enumerate(soldier):
        if (r, c) in blocked:
            block_soldier.add(idx)
    return region, block_soldier

def left(sr, sc, soldier):
    blocked = set()  # block 좌표
    shadow = set()  # 탐색 안할 좌표돌
    region = set()
    # sr, sc
    for c in range(sc-1, -1, -1):
        gap = abs(c-sc)
        # 가운데
        if (sr, c) not in shadow:
            region.add((sr, c))
            # 전사 만나면 그 뒤에 섀도우 지역 shadow에 넣어서, 나중에 탐색할 때 shadow면 아예 탐색 안하도록
            if (sr, c) in soldier:
                blocked.add((sr, c))
                for temp_c in range(c-1, -1,-1):
                    if 0<=temp_c<N:
                        shadow.add((sr, temp_c))
                    # 전사든 아니든, 일단 그 지역이 shadow가 아니라면 region에 넣음

        # 아래오른쪽
        for rr in range(sr+1, sr+gap+1):
            if 0<=rr<N:
                if(rr, c) not in shadow:
                    region.add((rr, c))
                    # 전사 만났을 떄
                    if (rr, c) in soldier:
                        blocked.add((rr, c))
                        for temp_c in range(c-1, -1, -1):
                            shadow.add((rr, temp_c))
                            temp_gap = abs(temp_c-c)
                            for temp_r in range(rr+1,rr+temp_gap+1):
                                if 0<=temp_r<N:
                                    shadow.add((temp_r, temp_c))
        # 위왼쪽
        for lr in range(sr-1, sr-(gap+1), -1):
            if 0<=lr<N:
                if(lr, c) not in shadow:
                    region.add((lr, c))
                    # 전사 만났을 떄
                    if (lr, c) in soldier:
                        blocked.add((lr, c))
                        for temp_c in range(c-1, -1, -1):
                            shadow.add((lr, temp_c))
                            temp_gap = abs(temp_c-c)
                            for temp_r in range(lr-1,lr-temp_gap-1, -1):
                                if 0<=temp_r<N:
                                    shadow.add((temp_r, temp_c))
    block_soldier = set()
    for idx, (r, c) in enumerate(soldier):
        if (r, c) in blocked:
            block_soldier.add(idx)
    return region, block_soldier

def right(sr, sc, soldier):
    blocked = set()  # block 좌표
    shadow = set()  # 탐색 안할 좌표돌
    region = set()
    # sr, sc
    for c in range(sc+1, N):
        gap = abs(c-sc)
        # 가운데
        if (sr, c) not in shadow:
            region.add((sr, c))
            # 전사 만나면 그 뒤에 섀도우 지역 shadow에 넣어서, 나중에 탐색할 때 shadow면 아예 탐색 안하도록
            if (sr, c) in soldier:
                blocked.add((sr, c))
                for temp_c in range(c+1, N):
                    if 0<=temp_c<N:
                        shadow.add((sr, temp_c))

        # 아래오른쪽
        for rr in range(sr+1, sr+gap+1):
            if 0<=rr<N:
                if(rr, c) not in shadow:
                    region.add((rr, c))
                    # 전사 만났을 떄
                    if (rr, c) in soldier:
                        blocked.add((rr, c))
                        for temp_c in range(c+1,N):
                            shadow.add((rr, temp_c))
                            temp_gap = abs(temp_c-c)
                            for temp_r in range(rr+1,rr+temp_gap+1):
                                if 0<=temp_r<N:
                                    shadow.add((temp_r, temp_c))

        # 위왼쪽
        for lr in range(sr-1, sr-(gap+1), -1):
            if 0<=lr<N:
                if(lr, c) not in shadow:
                    region.add((lr, c))
                    # 전사 만났을 떄
                    if (lr, c) in soldier:
                        blocked.add((lr, c))
                        for temp_c in range(c+1, N):
                            shadow.add((lr, temp_c))
                            temp_gap = abs(temp_c-c)
                            for temp_r in range(lr-1,lr-temp_gap-1, -1):
                                if 0<=temp_r<N:
                                    shadow.add((temp_r, temp_c))

    block_soldier = set()
    for idx, (r, c) in enumerate(soldier):
        if (r, c) in blocked:
            block_soldier.add(idx)
    return region, block_soldier

# 메두사시선, 돌이 된 전사수 출력, 돌된전사 누구인지=>이번판 못도니까, *******메두사 시야 들어오는 곳 좌표 집합, 돌된전사 idx
def glaze(sr, sc, soldier):
    region = set()
    stone_soldier = [] # idx
    up_region, up_stone_soldier = up(sr, sc, soldier)
    down_region, down_stone_soldier = down(sr, sc, soldier)
    left_region, left_stone_soldier = left(sr, sc, soldier)
    right_region, right_stone_soldier = right(sr, sc, soldier)

    temp_best = set()
    temp_best.add((-len(up_stone_soldier),0))
    temp_best.add((-len(down_stone_soldier),1))
    temp_best.add((-len(left_stone_soldier),2))
    temp_best.add((-len(right_stone_soldier),3))
    _, d = min(temp_best)
    if d==0:
        region, stone_soldier = up_region, up_stone_soldier
    if d==1:
        region, stone_soldier = down_region, down_stone_soldier
    if d==2:
        region, stone_soldier = left_region, left_stone_soldier
    if d==3:
        region, stone_soldier = right_region, right_stone_soldier

    return region, stone_soldier

# 전사들 이동, 모든 전사 이동거리 출력
def move_soldier(region, soldier):
    dist = 0
    for idx, (r, c) in enumerate(soldier):
        # 돌이면 못움직임
        if idx not in stone_soldier:
            ori_dist = abs(sr-r) + abs(sc-c)
            for d in range(4):
                nr, nc = r+dr[d], c+dc[d]
                new_dist = abs(nr-sr)+abs(nc-sc)
                #범위내, 이동가능칸, *********** 메두사 시야 들어오는 곳으로 이동 못함
                if 0<=nr<N and 0<=nc<N and (nr, nc) not in region:
                    if new_dist<ori_dist:
                        soldier[idx] = (nr, nc)
                        dist+=1
                        break
    for idx, (r, c) in enumerate(soldier):
        if idx not in stone_soldier:
            ori_dist = abs(sr-r) + abs(sc-c)
            #좌우상하
            for d in (2, 3, 0, 1):
                nr, nc = r+dr[d], c+dc[d]
                new_dist = abs(nr-sr)+abs(nc-sc)
                #범위내, 이동가능칸
                if 0<=nr<N and 0<=nc<N and (nr, nc) not in region:
                    if new_dist<ori_dist:
                        soldier[idx] = (nr, nc)
                        dist += 1
                        break
    return dist

# 전사 공격, 메두사를 공격한 전사 수 출력, 공격하고 전사 죽음
def attack(sr, sc):
    attack_count = 0
    alive = []
    for idx, (r, c) in enumerate(soldier):
        if (r, c)==(sr, sc):
            attack_count+=1
        else:
            alive.append((r, c))
    return attack_count, alive


while True:
    sr, sc, soldier = move_snail(sr, sc)
    if (sr, sc) == (er, ec):
        print(0)
        break
    if (sr, sc)==(-1,-1):
        print(-1)
        break


    region, stone_soldier = glaze(sr, sc, soldier)
    dist =move_soldier(region, soldier)
    attack_count, soldier = attack(sr, sc)
    # 전사이동거리, 돌된전사, 메두사공격전사
    print(dist, len(stone_soldier), attack_count)
