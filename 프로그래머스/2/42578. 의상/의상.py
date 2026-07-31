def solution(clothes):
    answer = 0
    hash_map={}
    for cloth in clothes:
        # print(cloth[0], cloth[1])
        hash_map[cloth[1]] = []
    for cloth in clothes:
        hash_map[cloth[1]].append(cloth[0])
    print(hash_map)
    total = 1
    for kind in hash_map:
        total *= (len(hash_map[kind])+1)
    answer = total -1
    return answer