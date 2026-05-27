def solution(s):
    zero_count=0
    convert_count=0
    while s!="1":
        convert_count+=1
        
        num_zero = s.count("0")
        zero_count+=num_zero
        
        new_length = len(s)-num_zero
        
        s=bin(new_length)[2:]
        
    return [convert_count, zero_count]