def solution(answers):
    par_1 = [1,2,3,4,5] * 2_000
    par_2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1_250
    par_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1_000
    pars = [0,0,0]
    for i in range(len(answers)) :
        if answers[i] == par_1[i] :
            pars[0] += 1
        if answers[i] == par_2[i] : 
            pars[1] += 1
        if answers[i] == par_3[i] : 
            pars[2] += 1
    mx_base = max(pars)
    answer = []
    for i in range(3) :
        if pars[i] ==mx_base :
            answer.append(i+1)
            
            
    
    return answer