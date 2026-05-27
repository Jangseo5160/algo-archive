def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    
    parent = list(range(n))
    
    def find(a):
        if parent[a]!=a:
            parent[a] = find(parent[a])
        return parent[a]
    
    def union(a,b):
        a, b = find(a), find(b)
        if a==b:
            return False
        parent[b]=a
        return True
    
    for a, b, cost in costs:
        if union(a,b):
            answer+=cost
    return answer

# MTS(prim, kruskal), 경로(dijkstra) 중 kruskal 사용하는 문제