from queue import PriorityQueue

scoville = [1, 2, 3, 9, 10, 12]
K = 7
def solution(scoville, K):
    heap = PriorityQueue()
    for s in scoville :
        heap.put(s)
    l = 0 
    answer = 0
    
    while not heap.empty() :
        f = heap.get()
        if f >= K : 
            return answer
        if heap.qsize() <= 1: 
            return -1
        s = heap.get()
        l = f+s*2
        answer += 1
        heap.put(l)
    return -1

print(solution(scoville,K))
