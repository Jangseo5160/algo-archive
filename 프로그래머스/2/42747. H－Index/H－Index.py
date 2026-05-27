def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    n=len(citations)
    for i in range(n):
        if citations[i] < i+1:
            return i
    return n

# 7 6 6 6 6
# 1 2 3 4 5

# 1 1 1 1
# 1 2 3 4

# 4 3 2 1
# 1 2 3 4

# 6 5 3 1 0
# 1 2 3 4 5

# 6 5 4 1 0
# 1 2 3 4 5