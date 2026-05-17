def solution(numbers, target):
    answer = 0
    def dfs(index, current_sum):
        # base case
        if index == len(numbers):
            return 1 if current_sum == target else 0
        
        # recursive case: + and - case
        return dfs(index+1, current_sum+numbers[index]) + dfs(index+1, current_sum - numbers[index])
        
    return dfs(0,0)