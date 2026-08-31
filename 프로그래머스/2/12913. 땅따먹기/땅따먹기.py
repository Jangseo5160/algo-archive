def solution(land):
    answer = 0
    base = [0,1,2,3]
    dp = [[0]*4 for _ in range(len(land))]
    
    dp[0] = land[0]
    
    for r in range(1, len(land)):
        land[r][0] += max(land[r-1][1], land[r-1][2], land[r-1][3])
        land[r][1] += max(land[r-1][0], land[r-1][2], land[r-1][3])
        land[r][2] += max(land[r-1][0], land[r-1][1], land[r-1][3])
        land[r][3] += max(land[r-1][0], land[r-1][1], land[r-1][2])
    
        
    return max(land[-1])