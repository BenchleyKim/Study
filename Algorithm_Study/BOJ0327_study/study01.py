def solution(w,h) :
    answer = 1
    def Euclidean(a, b):
        while b != 0:
            r = a % b
            a = b
            b = r
        
        return a
    gcd = Euclidean(w,h)
    sw = w // gcd 
    sh = h // gcd 
    garbage_paper = (sw + sh - 1) * gcd
    return w*h - garbage_paper

print(solution(8,12))