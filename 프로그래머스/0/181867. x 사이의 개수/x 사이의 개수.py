def solution(myString):
    answer = []
    count = myString.split("x")
    print(count)
    for i in count:
        answer.append(len(i))
    return answer