# k칸 앞으로: 건전지 사용량 -k, 현재 위치 *2
# 점프로 이동하는 것 최소화


def solution(n):
    ans = 0
    while n>0:
        if n%2==1:
            n-=1
            ans+=1
        n//=2
    
    return ans