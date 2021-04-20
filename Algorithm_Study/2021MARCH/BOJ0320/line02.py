def solution(enter, leave):
    stack = []
    left = 0
    right = 0
    answer = []
    check = [[0] * len(enter) for _ in range(len(enter))]
    while left < len(enter) and right < len(leave) :
        print(enter[left], leave[right],stack)
        if enter[left] != leave[right] :
            stack.append(enter[left]) 
            left += 1 
            
        else : 
            pop_index = None
            for s in range(len(stack)) :
                if enter[left] == stack[s] :
                    pop_index = s
                    continue 
                check[enter[left]-1][stack[s]-1] = 1
                check[stack[s]-1][enter[left]-1] = 1
            if pop_index is not None:
                stack.pop(pop_index)
            left += 1
            right += 1
    for i in range(right , len(leave)) :
        print(leave[i],stack)
        pop_index = None
        for s in range(len(stack)) :
            if leave[i] == stack[s] :
                pop_index = s
                continue 
            check[leave[i]-1][stack[s]-1] = 1
            check[stack[s]-1][leave[i]-1] = 1
        if pop_index is not None:
            stack.pop(pop_index)

    print(check)
    for c in check :
        answer.append(sum(c))

    return answer
enter = [1,4,2,3]	
leave = [2,1,3,4]
print(solution(enter, leave))