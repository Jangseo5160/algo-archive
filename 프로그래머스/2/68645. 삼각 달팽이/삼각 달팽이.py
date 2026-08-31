def solution(n):
    answer = []
    
    side = n
    d=0
    direction = [(1,0),(0,1),(-1,-1)]
    triangle = [[0]*(i+1) for i in range(n)]
    num=1
    r=-1
    c=0
    while side>0:
        dr, dc = direction[d]
        for _ in range(side):
            r+=dr
            c+=dc
            triangle[r][c] = num
            num+=1
        side-=1
        d=(d+1)%3
    for row in triangle:
        answer.extend(row)
    return answer