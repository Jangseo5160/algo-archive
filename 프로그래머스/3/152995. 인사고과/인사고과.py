def solution(scores):
    target_a, target_b = scores[0][0], scores[0][1]
    n=len(scores)
    scores = [
        [a, b, idx] for idx, [a, b] in enumerate(scores)
    ]
    scores.sort(key= lambda x: (-x[0], -x[1]))
    
    target_sum = target_a + target_b
    
    rank = 1
    max_b = -1
    i=0
    dominated = [False]*n
    
    while i<n:
        j= i
        
        # 앞 점수 같은사람 그룹
        while j<n and scores[i][0] == scores[j][0]:
            j+=1
        
        # 앞 점수 같은사람끼리 비교
        for k in range(i, j):
            a, b, idx = scores[k]
            
            if b < max_b:
                if idx==0:
                    return -1
                continue
                
            if a+b>target_sum:
                rank+=1
                
        # max_b 갱신하기
        for k in range(i, j):
            max_b=max(max_b, scores[k][1])
    
        i=j
    return rank