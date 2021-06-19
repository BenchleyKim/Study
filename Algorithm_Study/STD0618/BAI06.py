import heapq

def solution(nums ) :
    answer =  -1
    heap  =[]
    heapq.heappush(heap, (-(0 + nums[0]), 1 ))
    while heap :
        idx , cnt = heapq.heappop(heap)
        idx = -idx
        if idx == len(nums) - 1 :
            return cnt 
        if nums[idx] == 0 :
            continue
        if nums[idx] + idx < len(nums) :
            heapq.heappush(heap, (-(idx + nums[idx]), cnt+1 ))
        if idx  - nums[idx ]>= 0 :
            heapq.heappush(heap, (-(idx - nums[idx]), cnt+1 ))

    return answer


nums = [4,1,2,3,1,0,5] 
print(solution(nums))