import heapq

def solution(t, rank):
    answer = []
    # 손님이 도착한 시간과 인덱스 
    trr = [(j,i) for i,j in enumerate(t)]
    trr = sorted(trr, reverse=True)
    print(trr)
    heap = []
    start_time = 0
    if trr :
        start_time = trr[-1][0]
    while trr :
        if trr[-1][0] > start_time :
            break
        t, i = trr.pop()
        heapq.heappush(heap, (rank[i],t,i))
    while heap :
        print(heap)
        p,t, i = heapq.heappop(heap)
        
        answer.append(i)
        if not heap :
            if trr :
                start_time = trr[-1][0]
            else :
                break
        else : start_time += 1
        while trr :
            if trr[-1][0] > start_time :
                break
            ct, ci = trr.pop()
            heapq.heappush(heap, (rank[ci],ct,ci))
    
    return answer


print(solution([0,1,3,0],	[0,1,2,3]))
print(solution([7,6,8,1],	[0,1,2,3]))