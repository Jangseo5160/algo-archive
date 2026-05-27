def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    camera=-30001
    count=0
    for start, end in routes:
        if camera < start:
            count+=1
            camera=end
    return count

-20 -15
-18 -13
-14 -5
-5  -3