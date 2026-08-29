def solution(board):
    
    r= len(board)
    c = len(board[0])
    
    max_size = 0
    
    for ri in range(r):
        for ci in range(c):
            if board[ri][ci] == 1 and ri>0 and ci>0:
                board[ri][ci] = min(board[ri-1][ci], board[ri][ci-1], board[ri-1][ci-1])+1
                
            max_size = max(max_size, board[ri][ci])
    return max_size*max_size