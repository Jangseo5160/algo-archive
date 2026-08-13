def solution(n, money):
    answer = 0
    dp = [0] * (n+1)
    dp[0]=1
    
    for num in money:
        for i in range(num, n+1):
            dp[i] = dp[i] + dp[i-num]
        
    return dp[n] % 1000000007