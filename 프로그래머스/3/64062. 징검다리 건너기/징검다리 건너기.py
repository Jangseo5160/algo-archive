# 징검다리 건너기
# 디딤돌에 숫자, 밟을 때 1씩 줄어듬
# 디딤돌 0이 되면 밟을 수 없음, 그 다음 디딤돌로 건널수있음
# 밟을 수 있는 디딤돌이 여러개면 가장 가까운 디딤돌로만 건널 수 있음
# 디딤돌 최대 칸수 k 주어짐, 최대 몇명까지 징검다리 건널 수 있는지
# 징검다리 건널 수 있는 수는 무제한, stone은 2십만 이하, 원소값은 2억 이하. k는 범위 내. 

# 시간복잡도 => 이분탐색으로 기준을 m명 건널 수 있는지 없는지. 

def solution(stones, k):
    answer = 0
    
    left = 1
    right = max(stones)
    
    while left<=right:
        mid = (left+right)//2
        zero_count = 0
        possible = True
        for s in stones:
            if s < mid:
                zero_count+=1
                
                if zero_count>=k:
                    possible = False
                    break
            else:
                zero_count=0
        if possible:
            answer = mid
            left=mid+1
        else:
            right=mid-1

    return answer