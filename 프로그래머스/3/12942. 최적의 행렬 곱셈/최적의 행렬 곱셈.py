def solution(matrix_sizes):
    answer = 0
    n = len(matrix_sizes)
    dp = [[0]*n for _ in range(n)]
    
    # 행렬 2개 곱하는 경우
    for i in range(n-1):
        dp[i][i+1] = matrix_sizes[i][0] * matrix_sizes[i][1] * matrix_sizes[i+1][1]
    
    
    # 구간 길이
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length -1 
            
            dp[i][j] = float('inf')
            
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + matrix_sizes[i][0]* matrix_sizes[k][1]*matrix_sizes[j][1]
                
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n-1]