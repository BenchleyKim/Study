
import sys
sys.setrecursionlimit(10**7)
def findEmpty(num, check) :
    if not check.get(num) :
        check[num] = num + 1
        return num
    empty = findEmpty(check[num], check)
    check[num] = empty + 1
    return empty

def solution(k, room_number) : 
    check = {}
    answer = []
    for num in room_number :
        num = findEmpty(num, check)
        answer.append(num)
    return answer


print(solution(10,[1,3,4,1,3,1]))