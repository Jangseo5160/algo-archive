from collections import Counter
def solution(str1, str2):
    answer = 0
    str1=str1.lower()
    str2=str2.lower()
    
    A1 = []
    A2 = []
    for i in range(len(str1)-1):
        ch = str1[i:i+2]
        if ch.isalpha():
            A1.append(ch)
    
    for i in range(len(str2)-1):
        ch = str2[i:i+2]
        if ch.isalpha():
            A2.append(ch)
    # print(A1, A2)
    A1 = Counter(A1)
    A2 = Counter(A2)
    
    inter= A1&A2 # min
    union= A1|A2 # max
    
    inter = sum(inter.values())
    union = sum(union.values())
    # print(union)
    if union == 0:
        return 65536
    
    return int(inter/union * 65536)
