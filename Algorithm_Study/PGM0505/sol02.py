from itertools import permutations

def solution(expression):
    cal = list("+-*")
    all_case = list(permutations(cal,3))
    mx = 0
    for case in all_case :
        prior = {c:i for i,c in enumerate(case)}
        postfix = []
        stack = []
        num = ""
        for e in expression :
            if e in cal :
                postfix.append(int(num))
                num = ""
                while stack :
                    if prior[stack[-1]] >= prior[e] :
                        postfix.append(stack.pop())
                    else :
                        break            
                stack.append(e)
                continue
            num += e
        postfix.append(int(num))
        while stack :
            postfix.append(stack.pop())
        stack = []
        for p in postfix :
            if p in cal :
                B = stack.pop()
                A = stack.pop()
                if p == '-' :
                    stack.append(A-B)
                    continue
                if p == '+' :
                    stack.append(A+B)
                    continue
                if p == '*' :
                    stack.append(A*B)
                    continue
            else : 
                stack.append(p)
        mx = max(mx, abs(stack[-1]))

    return mx

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
print(solution("200-300-500-600*40+500+500"))

# 1248000