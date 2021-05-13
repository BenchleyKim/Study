
def bit(n) :
    
    i = n

    flag = True
    while True :
        i += 1
        K = bin(n ^ i)
        cnt = 0
        flag = True

        for k in K :
            if k == '1' : 
                cnt += 1
            if cnt > 2 :
                flag = False
                break
        if flag :
            break
    return i

    


def solution(numbers):
    answer = []
    for num in numbers :
        ans = bit(num)
        answer.append(ans)
    return answer



print(solution([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]))
