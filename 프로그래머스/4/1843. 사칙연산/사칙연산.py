def solution(arr):
    answer = -1
    n = len(arr)//2 +1
    INF = int(1e9)
    mindp = [[INF] * n for _ in range(n)]
    maxdp = [[-INF] * n for _ in range(n)]
    for i in range(n):
        mindp[i][i] = int(arr[i*2])
        maxdp[i][i] = int(arr[i*2])
    for length in range(1, n):
        for start in range(n-length):
            end = start + length
            for k in range(start, end):
                if arr[k*2+1] == '+':
                    mindp[start][end] = min(mindp[start][end], mindp[start][k] + mindp[k+1][end])
                    maxdp[start][end] = max(maxdp[start][end], maxdp[start][k] + maxdp[k+1][end])
                elif arr[k*2+1] == '-':
                    mindp[start][end] = min(mindp[start][end], mindp[start][k] - maxdp[k+1][end])
                    maxdp[start][end] = max(maxdp[start][end], maxdp[start][k] - mindp[k+1][end])
    
    return maxdp[0][n-1]