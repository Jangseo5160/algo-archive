def solution(want, number, discount):
    answer = 0
    
    for i in range(0, len(discount)-9):
        current = {}
        for j in range(i, i+10):
            item = discount[j]
            current[item] = current.get(item, 0) +1
        possible = True
        for idx, w in enumerate(want):
            if current.get(w, 0) != number[idx]:
                possible = False
                break
        if possible:
            answer+=1
    return answer