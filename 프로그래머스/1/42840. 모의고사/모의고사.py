def solution(answers):
    answer = []
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result=[0,0,0]


    for i in range(len(answers)):
        if a1[i%5] == answers[i]:
            result[0]+=1
        if a2[i%8] == answers[i]:
            result[1]+=1
        if a3[i%10] == answers[i]:
            result[2]+=1
            
    max_score = max(result)
    
    for a in range(3):
        if result[a] == max_score:
            answer.append(a+1)
            
    return answer
    