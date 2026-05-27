def solution(binomial):
    answer = 0
    part = binomial.split()
    a=int(part[0])
    op=part[1]
    b=int(part[2])
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b