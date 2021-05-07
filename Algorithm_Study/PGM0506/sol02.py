
import re 

def solution(user_id, banned_id):
    answer = 0
    # check = [0] * len(user_id)
    # cases = [0] * len(banned_id)
    for j in range(len(banned_id)) :
        bid = banned_id[j]
        pattern = bid.replace("*", ".")
        p = re.compile(pattern)
        for i in range(len(user_id)) :
            # if check[i] :
            #     continue
            uid = user_id[i]
            res = p.match(uid)
            if res :
                if res.end() - res.start() == len(uid) :
                    print(res)
                    # check[i] = 1
                    # cases[j] += 1
    # print(cases)                    
    
    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],	["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],	["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],	["fr*d*", "*rodo", "******", "******"]))
