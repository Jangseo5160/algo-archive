def solution(name):
    answer = 0
    up_down = 0
    
    for c in name:
        up=ord(c) - ord('A')
        down= ord('Z') - ord(c)+1
        up_down += min(up, down)
        # print(up_down)
        
    idx = 0
    left_right = len(name)-1

        
    for i in range(len(name)):
        next_idx = i+1
        while  next_idx<len(name) and name[next_idx] =='A':
            next_idx+=1
                    
        left_back= (len(name)-next_idx)*2 + i
        right_back = i + i + len(name)-next_idx
        print(left_back, right_back, left_right)
        left_right = min(left_back, right_back, left_right)
    
    return up_down + left_right