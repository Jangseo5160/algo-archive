# 시간 효율 문제

def solution(numbers):
    answer = [-1] *len(numbers)
    stk = []
    
    for i in range(len(numbers)):
        # numbers[i] 가 result에 들어가는 모든 경우의 수 기준으로 계산
        while stk and numbers[stk[-1]] < numbers[i]:
            idx = stk.pop()
            answer[idx] = numbers[i]
        stk.append(i)
    
    return answer