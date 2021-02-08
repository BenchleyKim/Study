N = int(input())

arr = list(map(int, input().split()))

def merge(left, right) : 
    result = []
    while len(left) > 0 or len(right) > 0 :
        
        if len(left) > 0 and len(right) > 0 :
            if left[0] <= right[0] :
                result.append(left.pop(0))
            else : 
                result.append(right.pop(0))
            continue
        if len(left) > 0 :
            result.extend(left)
            break
        if len(right) > 0 : 
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
