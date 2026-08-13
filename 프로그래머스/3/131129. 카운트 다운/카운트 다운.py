def solution(target):
    answer = []
    INF = int(1e9)
    dp = [[INF, 0] for _ in range(target+1)]
    dp[0] = [0,0]
    dart = []
    
    for num in range(1, 21):
        dart.append((num, 1))
    
    for num in range(1, 21):
        dart.append((num*2, 0))
    
    for num in range(1, 21):
        dart.append((num*3, 0))
    
    dart.append((50, 1))
    
    ######################################
    
    for amount in range(1, target+1):
        for d, s in dart:
            if amount>=d:
                pre_amount = dp[amount-d][0]
                pre_single = dp[amount-d][1]

                new_amount = pre_amount + 1
                new_single = pre_single + s

                if new_amount < dp[amount][0]:
                    dp[amount] = [new_amount, new_single]
                    
                elif new_amount == dp[amount][0]:
                    dp[amount][1] = max(new_single, dp[amount][1])
                
    
    return dp[target]