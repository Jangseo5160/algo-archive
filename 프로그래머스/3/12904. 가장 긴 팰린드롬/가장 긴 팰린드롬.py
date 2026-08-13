def solution(s):
    answer = 0
    n=len(s)
    for mid in range(n):
        l=mid
        r=mid
        while 0<=l<n and 0<=r<n and s[l]==s[r]:
            answer = max(answer, r-l+1)
            l-=1
            r+=1
            
        l=mid
        r=mid+1
        while 0<=l<n and 0<=r<n and s[l]==s[r]:
            answer = max(answer, r-l+1)
            l-=1
            r+=1
    return answer