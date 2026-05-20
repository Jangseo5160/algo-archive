def solution(arr):
    answer = []
    for i in arr:
        if answer == [] or i != answer[-1]:
            answer.append(i)
            # print(answer)
        else:
            continue
    return answer