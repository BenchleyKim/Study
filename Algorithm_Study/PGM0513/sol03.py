
import re 

p = re.compile('110')
def insertcase(s) :
    if len(s) <= 3 :
        return s
    stack = []
    count = 0
    arr = []
    for i in s :
        stack.append(i) 
        if len(stack) >= 3 :
            if stack[-1] == '0' :
                if stack[-2] == '1' :
                    if stack[-3] == '1' :
                        stack.pop()
                        stack.pop()
                        stack.pop()
                        count += 1

    de = ''
    if count :
        de = '110' * count
    if len(stack) < 3 :
        for st in stack :
            if st == '0' :
                arr = ''.join(stack) + de
                print(arr)
                return arr
        arr = de + ''.join(stack)
        return arr
    else :
        arr = ''
        for i in range(len(stack)-2) :

            if stack[i] == '1' :
                if stack[i+1] == '1' :
                    if stack[i+2] == '1' :
                        arr = ''.join(stack[:i]) + de + ''.join(stack[i:])
                        return arr
        arr = ''.join(stack) + de
        return arr

def solution(S):
    answer = []
    for s in S : 
        ans = insertcase(s)
        answer.append(ans)


    return answer



print(solution(["1110","1101", "0110","1100","100111100","0111111010","110110110","1111111000","01","1"]))
