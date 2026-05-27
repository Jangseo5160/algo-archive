def solution(strArr):
    answer = []
    for a in strArr:
        if "ad" not in a:
            answer.append(a)
    return answer