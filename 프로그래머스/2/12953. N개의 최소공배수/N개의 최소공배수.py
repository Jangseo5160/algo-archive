def solution(arr):
    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a
    answer = arr[0]
    
    for num in arr[1:]:
        answer = answer*num // gcd(answer, num)
    return answer