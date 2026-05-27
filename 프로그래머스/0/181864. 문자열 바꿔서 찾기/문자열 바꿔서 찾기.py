def solution(myString, pat):
    answer = 0
    return int("".join(["A" if i =="B" else "B" for i in pat]) in myString)
