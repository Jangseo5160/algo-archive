def solution(s):
    numbers=list(map(int, s.split()))
    print(numbers)
    low=min(numbers)
    high=max(numbers)
    return f"{low} {high}"
    # for num in numbers:
    #     int_list+=(int(num))
    # return "".join(min(int_list)+max(int_list))
    # answer = ''
    #low=min(number)
   # high=max(number)
   # answer+=low + high
