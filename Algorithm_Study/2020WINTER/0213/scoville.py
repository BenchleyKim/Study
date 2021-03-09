from queue import PriorityQueue
import heapq


scoville = [1, 2, 3, 9, 10, 12]
K = 7
def solution(scoville, K):
    data = []
    for s in scoville :
        heapq.heappush(data,s)
    l = 0 
    answer = 0
    while len(data) > 0  :
        f = heapq.heappop(data)
        if f >= K : 
            return answer
        if len(data) < 1: 
            return -1
        s = heapq.heappop(data)
        l = f+s*2
        answer += 1
        heapq.heappush(data,l)
    return -1

print(solution(scoville,K))
