def solution(tickets):
    answer = []
    tickets.sort()
    visited = [False] * len(tickets)
    
    def dfs(current_airport, path):
        # base 조건
        if len(path) == len(tickets)+1:
            return path
        
        for i, ticket in enumerate(tickets):
            if not visited[i] and ticket[0] == current_airport:
                visited[i]= True
                
                result = dfs(ticket[1], path + [ticket[1]])
                
                if result:
                    return result
                
                visited[i]= False
                
        return 0
    
    return dfs("ICN", ["ICN"])