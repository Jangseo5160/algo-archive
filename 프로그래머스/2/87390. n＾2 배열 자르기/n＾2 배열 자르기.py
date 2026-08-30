def solution(n, left, right):
    # answer = []
    # grid = [[0] * n for _ in range(n)]
    # onearr = []
    # for i in range(n):
    #     for j in range(n):
    #         grid[i][j]=(i+1)
    #         grid[j][i]=(i+1)
    # for arr in grid:
    #     for a in arr:
    #         onearr.append(a)
    # answer = onearr[left:right+1]
    
    answer = []
    for idx in range(left, right+1):
        row = idx // n
        col = idx % n
        num =max(row, col) +1
        answer.append(num)
    
    return answer