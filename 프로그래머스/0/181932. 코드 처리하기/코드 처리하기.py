def solution(code):
    answer = ''
    mode = 0
    ret=''
    for i in range(len(code)):
        if code[i]=='1':
            if mode == 1: 
                mode = 0
            else: 
                mode = 1  
        elif i%2==mode:
            ret+=code[i]
    return ret or "EMPTY"