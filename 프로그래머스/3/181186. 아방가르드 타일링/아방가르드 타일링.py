def solution(n):
    MOD = 1000000007
    answer = 0
    base = [1,1,3,10,23,62,170]
    if n<=6:
        return base[n]
    
    dp = [0]*(n+1)
    for i in range(7):
        dp[i]=base[i]
    
#     def recursive(idx, pattern_idx):
#         if idx<0:
#             return 0
#         pattern = [2,2,4]
#         return (dp[idx]*pattern[pattern_idx] + recursive(idx-1, (pattern_idx+1)%3))
            
    
    for i in range(7,n+1):
        
        dp[i]=(dp[i-1] + dp[i-2]*2 + dp[i-3]*6 + dp[i-4] - dp[i-6]) % MOD
    
    
    return dp[n]