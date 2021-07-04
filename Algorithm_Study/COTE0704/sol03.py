import copy 
import heapq

def cal_E(arr) :
    base_list = list(range(1, len(arr)+1))
    e = 0 
    for i in range(len(arr)) :
        e += abs(arr[i] - base_list[i])
    return e 

def solution(arr, k):
    answer = -1
    c_e = cal_E(arr)
    # while c_e != 0 :
    heap = [(c_e, 0, arr)]
    heap = []
    heapq.heappush(heap, ( 0 , c_e, arr))
    while heap :
        cnt , c_e ,  arr = heapq.heappop(heap)
        if c_e == 0 :
            answer = cnt
            break
        for i in range(len(arr)) :
            for j in range(i+1, min(len(arr), i + k + 1)) :
                arr[i], arr[j] = arr[j], arr[i]
                n_e = cal_E(arr)
                if n_e <= c_e :
                    heapq.heappush(heap, [cnt + 1, n_e , copy.deepcopy(arr)])
                arr[i], arr[j] = arr[j], arr[i]
    return answer