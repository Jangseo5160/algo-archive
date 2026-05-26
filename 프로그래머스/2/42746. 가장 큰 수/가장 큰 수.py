def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    
    numbers.sort(key = lambda x : x*3, reverse=True)
    for i in numbers:
        answer+=i
    
    return str(int(answer))

# n^2 가능한 모든 문자열 순서로 만들기
# str -> int -> 최댓값 -> str 반환