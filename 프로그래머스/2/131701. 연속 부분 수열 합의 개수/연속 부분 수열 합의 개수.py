# 원형 배열 => 2배 이어붙여서 1차원 배열로
# 투포인터로 접근했는데, 쉬운건 length로 접근하는 것
# 투포인터는 특정 조건 찾을 때, length는 가능한 모든 경우의 수 찾기
def solution(elements):
    answer = 0
    n=len(elements)
    elements+=elements
    
    total = set()
    
    for start in range(n):
        current_sum = 0
        for length in range(n):
            current_sum += elements[start+length]
            total.add(current_sum)
    
    return len(total)