def solution(inp_str):
    answer = []
    check = [0] * 4
    prev_value = inp_str[0]
    overlap_check = {}
    if len(inp_str) < 8 or len(inp_str) > 15 :
        answer.append(1)
    flag = 1
    flag5 = 1
    for i in range(len(inp_str)) :
        if inp_str[i] in overlap_check.keys() :
            overlap_check[inp_str[i]] += 1
            if overlap_check[inp_str[i]] >= 5 :
                if flag5 :
                    answer.append(5)
                    flag5 = 0
        else :
            overlap_check[inp_str[i]] = 1
        
        if inp_str[i].isalpha() :
            if inp_str[i].islower() :
                check[1] = 1
            else :
                check[0] = 1
        elif inp_str[i].isdigit() :
            check[2] = 1
        elif inp_str[i] in "~!@#$%^&*" :
            check[3] = 1
        else :
            if flag  :  
                answer.append(2)
                flag = 0
    if sum(check) < 3 :
        answer.append(3)
    continuous_count = 1
    for i in range(1,len(inp_str)) :
        if inp_str[i] == inp_str[i-1] :
            continuous_count += 1
            if continuous_count >= 4 :
                answer.append(4)
                break
    answer.sort()
    if len(answer) == 0 :
        return [0]
    
    return answer
print(solution(input_value))
print(len(input_value))