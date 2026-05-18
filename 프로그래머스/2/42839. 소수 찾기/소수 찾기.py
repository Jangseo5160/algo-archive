from itertools import permutations

def if_prime(a):

    if a < 2:
        return False
    for i in range(2, a):
        if a%i ==0:
            return False
    return True
    
def solution(numbers):
    # 같은 숫자 반복되어있으면 중복 처리해야됨. set은 중복 허용안하는 자료형
    unique_nums = set() 
    
    for i in range(1, len(numbers)+1): # 숫자 길이 정하기
        for p in permutations(numbers, i): # 정해진 숫자 길이로 튜플 조합 만들기
            unique_nums.add(int("".join(p))) # 튜블에서 공백 제거하고 숫자로 변환, 이때 0은 자동으로 제거됨
    print(unique_nums)
    
    prime_count = sum(1 for num in unique_nums if if_prime(num))
    
    return prime_count