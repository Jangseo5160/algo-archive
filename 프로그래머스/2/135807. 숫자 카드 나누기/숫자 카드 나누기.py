def solution(arrayA, arrayB):
    answer = 0
    def gcd(a,b):
        while b:
            a, b = b, a%b
        return a
    
    arrayA.sort()
    arrayB.sort()
    
    gcdA = arrayA[0]
    gcdB = arrayB[0]

    for num in arrayA[1:]:
        gcdA = gcd(gcdA, num)
    
    for num in arrayB[1:]:
        gcdB = gcd(gcdB, num)
        
    possible = True
    
    for num in arrayB:
        if num % gcdA==0:
            possible = False
            break
    
    if possible:
        answer = max(answer, gcdA)
        
        
    possible = True
    
    for num in arrayA:
        if num % gcdB==0:
            possible = False
            break
    if possible:        
        answer = max(answer, gcdB)
            
    return answer