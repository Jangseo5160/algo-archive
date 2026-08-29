def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        main = ""
        for s in tree:
            if s in skill:
                main+=s
        if skill.startswith(main):
            answer+=1
    return answer