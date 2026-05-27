def solution(num_list):
    answer = 0
    return max(sum(num_list[::2]), sum(num_list[1::2]))