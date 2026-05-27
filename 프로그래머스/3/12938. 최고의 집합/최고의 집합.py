def solution(n, s):
    answer = []
    sol = s//n
    rem = s%n
    answer = [sol] *(n-rem)
    # answer.append(sol) * (n-rem)
    if s<n:
        return [-1]
    for i in range(rem):
        answer.append(sol+1)
    return answer