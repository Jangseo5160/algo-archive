def solution(sizes):
    answer = 0
    val = -1
    max_val = -1
    min_val = 0
    for r, row in enumerate(sizes):
        for c, val in enumerate(row):
            if val > max_val:
                max_val = val
                min_val = min(row)
                print(max_val, min_val)
                
    for r, row in enumerate(sizes):
        if min(row) > min_val:
            min_val = min(row)
            print(min_val)
            
    answer = max_val * min_val
    return answer