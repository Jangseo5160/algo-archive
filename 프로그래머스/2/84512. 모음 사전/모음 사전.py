def solution(word):
    answer = 0
    cnt=-1
    alpha = ["A","E","I","O","U"]
    
    def dfs(curr_word):
        nonlocal answer, cnt
        
        cnt+=1
        
        if curr_word ==word:
            answer= cnt
            return
        if len(curr_word)==5:
            return
        for a in alpha:
            if answer==0:
                dfs(curr_word+a)
        
    dfs("")
    return answer