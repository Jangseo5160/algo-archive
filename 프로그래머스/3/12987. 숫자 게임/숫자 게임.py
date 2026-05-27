def solution(A, B):
    answer = 0
    n=len(A)
    A.sort(reverse=True)
    B.sort(reverse=True)
    j=0
    for i in range(n):
        if A[i] < B[j]:
            j+=1
        
    return j