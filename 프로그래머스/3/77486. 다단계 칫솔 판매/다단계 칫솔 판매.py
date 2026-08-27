# 모든 판매원은 이익에서 10%는 추천인, 나머지는 자신
# enroll 이름 순서대로 이익금 총합 출력
# 재귀함수


def solution(enroll, referral, seller, amount):
    parent = {}
    for i in range(len(enroll)):
        parent[enroll[i]] = referral[i]
    total = {}
    for name in enroll:
        total[name]=0
        
    for i in range(len(seller)):
        current = seller[i]
        earning = amount[i]*100
        while current != '-' and earning>0:
            give = earning//10
            mine = earning -give
            total[current] +=mine

            earning = give
            current = parent[current]
    
    answer = [total[name] for name in enroll]
    return answer