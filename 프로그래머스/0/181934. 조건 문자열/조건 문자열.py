def solution(ineq, eq, n, m):
    answer = 0
    if n==m:
        if eq=="=":
            return 1
    elif n>m:
        if ineq == ">":
            return 1
    elif n<m:
        if ineq =="<":
            return 1
    return 0