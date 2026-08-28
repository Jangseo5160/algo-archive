# 1, -1, 10, -10,,, 다음 층 = 현재 층 + 버튼 값
# 만약 다음층이 계산했을 때 0보다 작으면 안움직임
# 버튼 한번당 마법돌 한개 사용
# 마법돌 최소 구하기
# storey 1억
def solution(storey):
    answer = 0
    while storey>0:
        c = storey%10
        # print(c)
        storey = storey//10
        if c ==0:
            continue
        elif c==5 and storey%10 >=5:
            answer+=5
            storey+=1
        elif 0<c<=5:
            answer+=c
        elif 6<=c<=9:
            answer+= (10-c)
            storey+=1
    return answer