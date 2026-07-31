def solution(phone_book):
    hash_map = {}
    for num in phone_book:
        hash_map[num] = 1
    for num in phone_book:
        temp = ""
        for n in num:
            temp+=n
            if temp in hash_map and temp != num:
                return False
    return True