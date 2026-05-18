def solution(brown, yellow):
    answer = []
    area =brown + yellow
    for height in range(1, area//2+1):
        if area%height==0:
            width=area//height
            if (width-2) * (height-2) == yellow:
                return [width, height]