def solution(n):
    answer = 0
    base = [1,1,2]
    if n < 3:
        return base[n]
    
    dp = [0]*(n+1)
    for i in range(3):
        dp[i]=base[i]
    
    for i in range(3, n+1):
        dp[i]=dp[i-1]+dp[i-2]
    
    return dp[n] % 1234567