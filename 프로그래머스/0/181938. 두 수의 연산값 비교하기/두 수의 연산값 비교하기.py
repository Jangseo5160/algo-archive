def solution(a, b):
    answer = 0
    ab=int(str(a)+str(b))
    twoab=2*a*b
    return max(ab, twoab)