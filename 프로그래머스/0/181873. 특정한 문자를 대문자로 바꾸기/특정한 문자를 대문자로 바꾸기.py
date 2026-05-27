def solution(my_string, alp):
    answer = ''
    for char in my_string:
        if char == alp:
            answer+=alp.upper()
        else:
            answer+=char
    return answer