def solution(name):
    answer = 0
    l = len(name)    
    arr = []
        
    for i in range(l) :
        n = name[i]
        mn = min((ord(n)-ord('A')),26-(ord(n)-ord('A')))
        arr.append(mn)
    rcnt = l
    for i in range(1,l) :
        rcnt -= 1
        if arr[i] == 0 :
            break
    lcnt = l
    for i in range(l-1,0) :
        lcnt -= 1
        if arr[i] == 0 :
            break
    if rcnt > lcnt : 
        answer = sum(arr)+l-lcnt 
    else :
        answer = sum(arr)+l-rcnt

    return answer

print(solution("JEROEN"))
print(solution("JAN"))