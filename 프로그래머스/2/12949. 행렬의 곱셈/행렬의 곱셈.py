def solution(arr1, arr2):
    answer = []
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = c1, len(arr2[0])
    
    for i in range(r1):
        row=[]
        for w in range(c2):
            cur = 0
            for j in range(c1):
                a = arr1[i][j]
                b = arr2[j][w]
                cur += a*b
            row.append(cur)
        answer.append(row)
    
    return answer