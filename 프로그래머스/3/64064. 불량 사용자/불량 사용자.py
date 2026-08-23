# 조합탐색 => 백트래킹 / DFS

def match(user, ban):
    if len(user) != len(ban):
        return False
    else:
        for i in range(len(ban)):
            if ban[i]=="*":
                continue
            elif user[i] != ban[i]:
                return False
    return True

def solution(user_id, banned_id):
    result = set()
    
    def dfs(idx, used, selected):
        if idx == len(banned_id):
            result.add(frozenset(selected))
            return
        for user in user_id:
            if user in used:
                continue
            if match(user, banned_id[idx]):
                used.add(user)
                selected.append(user)
                dfs(idx+1, used, selected)
                used.remove(user)
                selected.pop()
                
    dfs(0,set(), [])
    return len(result)