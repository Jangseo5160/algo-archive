def solution(w,h):
    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a
    return (w*h) - (w+h-gcd(w, h))