def solution(a, b, c):
    # set([a,b,c])처럼 list로 감싸서 추출
    # check=len(set([a,b,c]))
    # if check ==1: => 원소 1개
    # if check ==2: => 원소 2개
    # if check ==3: => 원소 3개
    if a!=b and b!=c and a!=c:
        return a+b+c
    elif a==b==c:
        return 27*(a**6)
    else: 
        return (a+b+c)*(a**2+b**2+c**2)