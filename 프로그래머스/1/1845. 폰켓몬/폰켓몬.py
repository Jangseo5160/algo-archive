from collections import *
def solution(nums):
    answer = 0
    n = len(nums)//2
    cnt = Counter(num for num in nums)
    # 1:1 2:1, 4:2 n
    # 4 2
    answer = min(n, len(cnt))
    
    return answer