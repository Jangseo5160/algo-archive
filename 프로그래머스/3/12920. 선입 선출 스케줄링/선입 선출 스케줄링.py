def solution(n, cores):
    answer = 0
    l = 1
    r = max(cores) * n
    
    while l < r:
        mid = (l+r)//2
        total = len(cores) + sum(mid//c for c in cores)
        if total<n:
            l = mid+1
        if total>=n:
            r=mid
    # l은 n번째 작업이 시작되는 최소 시간
    # remain은 l시간 직전까지 완료된 작업 개수
    # l시간 때 시작하는 작업들 중 remain번 째인 것이 우리가 원하는 인덱스
    before = len(cores)
    
    for c in cores:
        before += (l-1)//c
    remain = n - before
    
    # l시간번 째 새로 시작할 수 있는 코어 찾기
    for i, c in enumerate(cores):
        if l % c == 0:
            remain -=1
            
            if remain ==0:
                return i+1
            
    