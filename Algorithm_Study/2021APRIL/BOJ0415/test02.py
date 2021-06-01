def solution(s):
    answer = 0
    s = list(s)
    for i in range(len(s)):
        stack = []
        s.append(s.pop(0))
        flag= True
        for j in range(len(s)) :
            if s[j] in ['(','{','['] :
                stack.append(s[j])
            else :
                if len(stack) == 0 :
                    flag = False
                    break
                if s[j] == ')' and stack[-1] == '(' :
                    stack.pop()
                    continue
                elif s[j] == ']' and stack[-1] == '[' :
                    stack.pop()
                    continue
                elif s[j] == '}' and stack[-1] == '{' :
                    stack.pop()
                    continue
                else :
                    flag = False
                    break
        if stack :
            flag = False
        if flag :
            answer += 1

        

    return answer

print(solution("}{"))

print(solution("[](){}"))
print(solution("}]()[{"	))
print(solution("[)(]"))
print(solution("}}}"))
	

	
