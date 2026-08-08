def solution(N, number):
    answer = 0
    countList = [set() for _ in range(9)]
    countList[1].add(N)
    
    for i in range(2, 9):
        countset = set()
        for j in range(1,i):
            pre = countList[j]
            post = countList[i-j]
            
            for prenum in pre:
                for postnum in post:
                    countset.add(prenum+postnum)
                    countset.add(prenum-postnum)
                    countset.add(postnum-prenum)
                    countset.add(prenum*postnum)
                    if postnum != 0:
                        countset.add(prenum//postnum)
                    if prenum != 0: 
                        countset.add(postnum//prenum)
        countset.add(int(str(N)*i))
        countList[i] = countset
    
    for i in range(1,9):
        if number in countList[i]:
            return i
    
    return -1