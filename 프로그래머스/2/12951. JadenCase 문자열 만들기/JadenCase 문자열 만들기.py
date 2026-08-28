def solution(s):
    answer = ''
    for i in range(len(s)):
        if s[i]==" ":
            answer+= " "
                
        elif i==0 or s[i-1] == " ":
            answer+=(s[i].upper())
        else:
            answer+=(s[i].lower())
        
    return answer