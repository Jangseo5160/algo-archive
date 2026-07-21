def solution(k, dungeons):
    answer = -1
    stk = [(k, [], 0)]
    
    while stk:
        curr_k, visited, dist = stk.pop()
        answer = max(answer, dist)
        
        for i in range(len(dungeons)):
            if i not in visited and curr_k >= dungeons[i][0]:
                stk.append((curr_k-dungeons[i][1],visited + [i], dist+1))
    return answer