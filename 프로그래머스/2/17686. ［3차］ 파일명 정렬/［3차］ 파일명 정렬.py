def solution(files):
    answer = []
    tail=""
    canlist = []
    
    for file in files:
        head=""
        number=""
        i=0
        while i<len(file) and not file[i].isdigit():
            head+=file[i]
            i+=1
        while i<len(file) and file[i].isdigit() and len(number)<=5:
            number+=file[i]
            i+=1
        canlist.append((head.lower(), int(number), file))
    canlist.sort(key=lambda x: (x[0], x[1]))
    
    
    return [file for _, _, file in canlist]