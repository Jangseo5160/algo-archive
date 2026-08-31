def solution(n, t, m, p):
    answer = ''
    num =0 
    game = ""
    while len(game) < t*m:
        game += convert(num, n)
        num+=1
    
    for i in range(t):
        answer += game[m*i+p-1]
    return answer

def convert(num, n):
    char = "0123456789ABCDEF"
    if num==0:
        return "0"
    result = ""
    while num>0:
        result = char[num%n] + result
        num//=n
    return result