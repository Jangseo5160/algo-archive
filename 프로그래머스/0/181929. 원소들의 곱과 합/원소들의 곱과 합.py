def solution(num_list):
    multi=1
    for i in num_list:
        multi *= i
    return int(multi<sum(num_list)**2)