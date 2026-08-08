def solution(m, n, puddles):
    answer = 0
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    for r in range(1, n+1):
        for c in range(1, m+1):
            
            if [c, r] in puddles:
                continue
                
            if c==1 and r==1:
                dp[1][1] = 1
                continue

            dp[c][r] = dp[c-1][r]+ dp[c][r-1]
    return dp[m][n] % 1000000007