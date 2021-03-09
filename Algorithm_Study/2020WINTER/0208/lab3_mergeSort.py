import collections

N = int(input())
arr = []
for _ in range(N) : 
    arr.append(int(input()))

#  arr = list(map(int, input().split()))

def merge(left, right) : 
    i = 0 
    j = 0
    result = []
    while len(left) > i or len(right) > j :
        if len(left) > i and len(right) > j :
            if left[i] <= right[j] :
                result.append(left[i])
                i += 1
            else : 
                result.append(right[j])
                j += 1
            continue
        if len(left) > i :
            result.extend(left)
            break
        if len(right) > j : 
            result.extend(right)
            break
    # print(result)    
    return result
    

def mergeSort(arr) :
    l = len(arr)
    if l <= 1 :
        return arr
    mid = l //2 
    leftArr = mergeSort(arr[:mid])
    rightArr = mergeSort(arr[mid:])
    return merge(leftArr, rightArr)

print(mergeSort(arr))
