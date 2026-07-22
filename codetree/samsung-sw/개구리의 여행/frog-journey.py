# import sys
# import heapq

# N = int(input())
# grid = [input() for _ in range(N)] 
# Q = int(input())
# dr = [-1,1,0,0]
# dc = [0,0,-1,1]
# INF = float('inf')

# for _ in range(Q):
#     answer = 0
#     r1,c1,r2,c2=map(int, input().split())
#     r1,c1,r2,c2 = r1-1,c1-1,r2-1,c2-1

#     dist = [[[INF]*6 for _ in range(N)] for _ in range(N)]
#     dist[r1][c1][1] = 0

#     q = [(0, r1, c1, 1)]

#     while q:
#         time, r, c, power = heapq.heappop(q)
#         if time > dist[r][c][power]:
#             continue

#         if power<=4:
#             new_power = power+1
#             new_time = time + new_power**2
#             if new_time < dist[r][c][new_power]:
#                 dist[r][c][new_power] = new_time
#                 heapq.heappush(q, (new_time, r, c, new_power))
    
#         for new_power in range(1, power):
#             new_time = time +1
#             if new_time < dist[r][c][new_power]:
#                 dist[r][c][new_power] = new_time
#                 heapq.heappush(q, (new_time, r, c, new_power))

#         for d in range(4):
#             can_jump = True
#             for step in range(1, power+1):
#                 nr, nc = r+dr[d]*step, c+dc[d]*step
#                 if not (0<=nr<N and 0<=nc<N):
#                     can_jump = False
#                     break
#                 cell = grid[nr][nc]

#                 if step < power:
#                     if cell == "#":
#                         can_jump =False
#                         break
#                 else:
#                     if cell == "S" or cell == "#":
#                         can_jump=False
#                         break

#             if can_jump:
#                 nr, nc = r + dr[d]*power, c+dc[d]*power
#                 new_time = time+1
#                 if new_time < dist[nr][nc][power]:
#                     dist[nr][nc][power] = new_time
#                     heapq.heappush(q, (new_time, nr, nc, power))

#     answer = min(dist[r2][c2][1:6])
#     if answer == INF:
#         answer=-1
#     print(answer)

import sys

def main():
    data = sys.stdin.buffer.read().split(b'\n')
    ptr = 0
    N = int(data[ptr]); ptr += 1
    grid = []
    for _ in range(N):
        grid.append(data[ptr].decode()); ptr += 1
    Q = int(data[ptr]); ptr += 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    INF = float('inf')

    # ---- 그리드는 모든 쿼리에서 동일하므로, "이 칸에서 이 방향으로 이 점프력만큼
    #      점프 가능한가"를 쿼리 시작 전에 딱 한 번만 계산해둔다 ----
    # valid[r][c][d][p] : (r, c)에서 방향 d로 점프력 p(1~5)만큼 점프 가능한지
    valid = [[[[False] * 6 for _ in range(4)] for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for d in range(4):
                ok_path = True  # 지금까지 지나온 경로에 '#'이 없었는지
                for p in range(1, 6):
                    nr, nc = r + dr[d] * p, c + dc[d] * p
                    if not (0 <= nr < N and 0 <= nc < N):
                        break
                    cell = grid[nr][nc]
                    if cell == '#':
                        ok_path = False
                        break
                    valid[r][c][d][p] = ok_path and cell != 'S'

    # ---- 모든 비용(점프 1, 점프력 감소 1, 점프력 증가 4/9/16/25)이 작은 정수라서
    #      heapq 대신 '딜의 알고리즘(버킷 큐)'을 쓰면 log 비용 없이 더 빠르다 ----
    MAXD = 1000  # 실제 걸리는 시간보다 충분히 크게 잡은 안전한 상한

    cache = {}  # (r1, c1) -> 그 출발점에서 계산한 dist 배열 (같은 출발점이면 재사용)

    results = []
    for _ in range(Q):
        r1, c1, r2, c2 = map(int, data[ptr].split()); ptr += 1
        r1 -= 1; c1 -= 1; r2 -= 1; c2 -= 1

        if (r1, c1) in cache:
            # 이미 같은 출발점을 계산해둔 적 있으면 다익스트라를 다시 돌리지 않고 바로 조회
            dist = cache[(r1, c1)]
            ans = min(dist[r2][c2][1:6])
            results.append(ans if ans != INF else -1)
            continue

        dist = [[[INF] * 6 for _ in range(N)] for _ in range(N)]
        dist[r1][c1][1] = 0

        buckets = [[] for _ in range(MAXD)]
        buckets[0].append((r1, c1, 1))

        d = 0
        while d < MAXD:
            bucket = buckets[d]
            if not bucket:
                d += 1
                continue
            while bucket:
                r, c, power = bucket.pop()
                if d > dist[r][c][power]:
                    continue  # 이미 더 짧은 경로로 처리된 상태

                # 1) 점프력 증가
                if power <= 4:
                    np_ = power + 1
                    nt = d + np_ * np_
                    if nt < dist[r][c][np_] and nt < MAXD:
                        dist[r][c][np_] = nt
                        buckets[nt].append((r, c, np_))

                # 2) 점프력 감소 (1 ~ power-1 중 아무 값으로나, 비용 1)
                for np_ in range(1, power):
                    nt = d + 1
                    if nt < dist[r][c][np_]:
                        dist[r][c][np_] = nt
                        buckets[nt].append((r, c, np_))

                # 3) 점프 (미리 계산해둔 valid 표를 그냥 찾아보기만 함)
                vrc = valid[r][c]
                for dd in range(4):
                    if vrc[dd][power]:
                        nr, nc = r + dr[dd] * power, c + dc[dd] * power
                        nt = d + 1
                        if nt < dist[nr][nc][power]:
                            dist[nr][nc][power] = nt
                            buckets[nt].append((nr, nc, power))
            d += 1

        cache[(r1, c1)] = dist  # 이 출발점은 이제 계산 끝났으니 저장해두고 다음에 재사용

        ans = min(dist[r2][c2][1:6])
        results.append(ans if ans != INF else -1)

    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    main()