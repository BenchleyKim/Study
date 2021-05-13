


def bit(n) :
    B = list(bin(n))
    count = 0 
    last = 0
    print(B)
    for i in range(len(B)-1,1,-1):
        print(i)
        if B[i] == '0' :
            count = 1 
            break
    if count :
        return n+1
    else :
        # for i in range(min(2,len(B)-2)) :
        B[2] = '0'
        B.insert( 2,'1')
    print(B)
    print()
    B = ''.join(B)
    return int(B,2)
    


def solution(numbers):
    answer = []
    for num in numbers :
        ans = bit(num)
        answer.append(ans)
    return answer



print(solution([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]))