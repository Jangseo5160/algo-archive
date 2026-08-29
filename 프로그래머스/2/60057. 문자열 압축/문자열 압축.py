def solution(s):
    answer = len(s)
    
    for chunk in range(1, len(s)//2+1):
        prev = s[0:chunk]
        count=1
        compressed = ''
        
        for i in range(chunk,len(s), chunk):
            cur = s[i:i+chunk]
            if prev == cur:
                count+=1
            else:
                if count>1:
                    compressed += str(count)+prev
                else:
                    compressed += prev
                
                prev= cur
                count = 1
        if count>1:
            compressed += str(count)+prev
        else:
            compressed += prev

        answer = min(answer, len(compressed))
    
    return answer