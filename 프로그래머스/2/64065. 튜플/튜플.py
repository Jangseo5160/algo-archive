def solution(s):
    answer = []
    s=s[2:-2]
    group = s.split("},{")
    group = [list(map(int, g.split(","))) for g in group]
    group.sort(key=len)
    used = set()
    for g in group:
        for num in g:
            if num not in used:
                answer.append(num)
                used.add(num)
    return answer