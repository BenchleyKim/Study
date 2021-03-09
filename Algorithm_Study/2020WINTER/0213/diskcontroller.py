import heapq


jobs = [[0,2],[1,1],[4,3],[8,2],[9,5]]
jobs = [[0, 3], [1, 9], [2, 6]]

# 2 + 2 + 3 + 2 + 6 / 5 = 3 
def solution(jobs) :
    i = 0
    data = []
    heapq.heappush(data , jobs[i])
    i += 1
    result= []
    endtime = jobs[0][0]
    while True :
        if len(data) == 0 : 
            current_work = jobs[i]
            i += 1
        else : current_work = heapq.heappop(data) 
        endtime += current_work[1]
        result.append(endtime - current_work[0])
        print( result, data)
        if i == len(jobs) -1 :
            return result
        while  i <= len(jobs)-1  & jobs[i][0] <= endtime :
            heapq.heappush(data, jobs[i])
            i += 1
            # print(i, data)
            
    return result



print(solution(jobs))