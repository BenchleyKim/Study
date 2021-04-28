def solution(n):
    answer = ''
    while n > 0 :
        d, m = divmod(n,3)
        if m == 0 :
            if d >= 1: 
                d -= 1
            answer = '4'+answer
        elif m == 1 :
            answer = '1'+answer
        elif m == 2 :
            answer = '2'+answer
        n = d
    return answer
print(solution(1))