def solution(numbers):
    answer = []
    for number in numbers:
        if number%2==0:
            answer.append(number+1)
        else:
            binary = '0'+bin(number)[2:]
            
            idx = binary.rfind('0')
            
            binary = (binary[:idx] + '10'+binary[idx+2:])
            answer.append(int(binary, 2))
    
    return answer