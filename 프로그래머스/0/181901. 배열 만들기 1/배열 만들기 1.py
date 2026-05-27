def solution(n, k):
    answer = []
    mul=1
    while mul*k <=n:
        answer.append(mul*k)
        mul+=1
    return answer