def solution(s):
    answer = 1
    n = len(s)
    for start in range(n):
        for end in range(n-1, start+answer-1, -1):
            if s[start] != s[end]:
                continue
                
            i, j = start, end
            while i<j and s[i] == s[j]:
                i+=1
                j-=1
                
            if i>=j:
                answer = end-start+1
                break
    return answer