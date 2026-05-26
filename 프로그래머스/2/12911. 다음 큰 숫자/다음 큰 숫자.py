def solution(n):
    answer = 0
    cnt = bin(n).count('1')
    
    next_n = n+1
    while(bin(next_n).count('1') != cnt):
        next_n+=1
    return next_n