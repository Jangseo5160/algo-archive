def solution(name):
    answer = 0
    cnt=0
    n=len(name)
    
    up_down = sum((min(ord(c) - ord('A'), 26-(ord(c) - ord('A'))) for c in name))
    left_right = n-1  
    
    for i in range(n):
        next_i = i+1
        while next_i < n and name[next_i] == 'A':
            next_i +=1
        
        go_right_back = i+i+(n-next_i)
        go_left_back = i + (n-next_i) + (n-next_i)

        left_right = min(left_right, go_right_back, go_left_back)
    
    return up_down + left_right

# ord() => 아스키값 변환 후 사용
# JAAAANN
# AJAZ