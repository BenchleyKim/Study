def solution(lottery):
    answer = -1
    user = {}
    for user_id, flag in lottery :
        if user_id not in user :
            user[user_id] = [1, flag]
            continue
        if user[user_id][1] == 0 :
            if flag == 0 :
                user[user_id][0] += 1
            else :
                user[user_id][0] += 1
                user[user_id][1] = 1
            continue
    total_sum = 0
    user_cnt =  0
    for key in user.keys() :
        if user[key][1] == 1 :
            user_cnt += 1
            total_sum += user[key][0]
    if user_cnt == 0 :
        return 0
    answer = total_sum // user_cnt

    return answer