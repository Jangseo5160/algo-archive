str = input()

# 소문자 판별 : str.islower()
# 대문자 판별 : str.isupper()
# 소문자 -> 대문자 : str.upper()
# 대문자 -> 소문자 : str.lower()
b=""
for a in str:
    if a.islower():
        b=b+a.upper()
    else:
        b=b+a.lower()

print(b)