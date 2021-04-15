
def solution(absolutes, signs):
    ans = 0 
    
    for i in range(len(absolutes)):
        if signs[i] :
            ans += absolutes[i]
        else :
            ans -= absolutes[i]


    return ans

print(solution([4,7,12]	,[true,false,true]))