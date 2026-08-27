# 모든 보석을 하나 이상 포함하는 가장 짧은 구간
# 시작번호, 끝번호
# 배열 크기 1이상 십만 이하
# 투포인터 문제

def solution(gems):
    total = len(set(gems))
    left=0
    base_left=0
    base_right=len(gems)-1
    count = {}
    
    for right in range(len(gems)):
        gem = gems[right]
        count[gem] = count.get(gem, 0)+1
        
        while len(count) == total:
            if right-left < base_right-base_left:
                base_right=right
                base_left=left
            
            left_gem=gems[left]
            count[left_gem]-=1
            
            if count[left_gem]==0:
                del count[left_gem]
                
            left+=1
            
    return [base_left+1, base_right+1]