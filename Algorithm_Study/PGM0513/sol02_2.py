def bit(n) :
    if n % 4 != 3 :
        return n + 1
    B = list(bin(n))
    B[2] = '0'
    B.insert( 2,'1')
    B = ''.join(B)
    return int(B,2)

    


def solution(numbers):
    answer = []
    for num in numbers :
        ans = bit(num)
        answer.append(ans)
    return answer



print(solution([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]))
