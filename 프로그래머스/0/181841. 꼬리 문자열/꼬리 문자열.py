def solution(str_list, ex):
    answer = ''
    for a in str_list:
        if ex not in a:
            answer+=a
    return answer