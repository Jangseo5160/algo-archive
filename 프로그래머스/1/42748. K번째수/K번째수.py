def solution(array, commands):
    answer = []
    new_list=[]
    for start, end, th in commands:
        # print(start, end, th)
        new_list=array[start-1:end]
        # print(new_list)
        new_list.sort()
        # print(new_list[th-1])
        answer.append(new_list[th-1])
    return answer