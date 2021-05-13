
def solution(left, right):
    answer = 0
            
    for i in range(left, right+1) :
        if int(i**(1/2)) == i**(1/2) :
            answer -= i
        else :
            answer += i
    
    return answer

print(solution(13,	17))
print(solution(13,	16))
print(solution(1,	9))

print(solution(24,	27))
print(solution(25,	27))
