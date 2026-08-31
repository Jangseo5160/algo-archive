def solution(n, k):
    answer = 0
    new_num = ""
    
    while n>0:
        ch = n%k
        new_num = str(ch) + new_num
        n//=k
    numbers = new_num.split('0')
    
    for num in numbers:
        if num == "":
            continue
        num = int(num)
        is_prime = True
        if num ==1:
            is_prime = False
        else:
            for i in range(2, int(num ** 0.5) +1):
                if num%i ==0:
                    is_prime = False
        if is_prime:
            answer+=1
                    
    return answer