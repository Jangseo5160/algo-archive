def solution(arr):
    answer = []
    for a in arr:
        answer += [a]*a
    return answer