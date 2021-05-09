import heapq

def solution(t, rank):
    answer = []
    # 손님이 도착한 시간과 인덱스 
    trr = [(j,i) for i,j in enumerate(t)]
    trr = sorted(trr, reverse=True)
    mx_time = trr[0][0]
    print(trr)
    heap = []
    for node in trr :
        t, i = node
        heapq.heappush(heap, (t, rank[i],i))
    while heap :
        t,r,i = heapq.heappop(heap)
        answer.append(i)
            
    return answer


print(solution([0,1,3,0],	[0,1,2,3]))
print(solution([7,6,8,1],	[0,1,2,3]))