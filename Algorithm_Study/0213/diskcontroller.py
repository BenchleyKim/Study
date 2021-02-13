import heapq


jobs = [[0, 3], [1, 9], [2, 6]]	


def solution(jobs) :
    data = []
    worktime = 0
    current_time = 0
    for job in jobs :
        if len(data) >= 1 :
            heapq.heappush(data, (job[1],job))
        else : 
            currentjob = job
            worktime = current_time - currentjob[0] + currentjob[1]
            print(worktime)


print(solution(jobs))