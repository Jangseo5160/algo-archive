from collections import deque

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = set([begin])
    while queue:
        current_word, cnt=queue.popleft()
        
        if current_word == target:
            return cnt
        
        for word in words:
            if word not in visited:
                diff_cnt=0
                for c1, c2 in zip(current_word, word):
                    if c1 != c2:
                        diff_cnt+=1
                if diff_cnt == 1:
                    visited.add(word)
                    queue.append((word, cnt+1))
    
    
    return 0