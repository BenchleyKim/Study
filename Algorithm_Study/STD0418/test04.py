
def solution(name):
    answer = 0
    l = len(name)    
    arr = []
        
    for i in range(l) :
        n = name[i]
        mn = min((ord(n)-ord('A')),26-(ord(n)-ord('A')))
        arr.append(mn)
    print(arr)
    rcnt = 0
    idx = 0
    for i in range(l) :
        answer += arr[idx]
        arr[idx] = 0
        lcnt = l // 2 +1
        lidx = idx
        while lcnt > 0 :
            lcnt -= 1
            lidx += 1
            if lidx < 0 :
                lidx = l-1
            if arr[lidx] != 0 :
                break
        rcnt = l//2 + 1
        ridx = idx
        while rcnt > 0 :
            rcnt -= 1
            ridx -= 1
            if ridx >= l :
                ridx = 0
            if arr[ridx] != 0 :
                break
        if lcnt < rcnt :
            answer += lcnt
            idx = lidx
        else :
            idx = ridx 
            answer += rcnt

    return answer

print(solution("JEROEN"))
print(solution("JAJAAAJ"))

