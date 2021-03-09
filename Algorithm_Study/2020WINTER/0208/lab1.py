
N = int(input())
arr = []
for _ in range(N) :
    arr.append(int(input()))

def selectSort(arr) : 
    for idx in range(len(arr)) :
        current = arr[idx]  
        tmp = idx
        for jdx in range(idx+1, len(arr)) :
            if current > arr[jdx] :
                current = arr[jdx]
                tmp = jdx
        arr[tmp] = arr[idx]
        arr[idx] = current
    print(arr)
def insertSort(arr) : 
    for end in range(1, len(arr)):
        to_insert = arr[end]
    i = end
    while i > 0 and arr[i - 1] > to_insert:
        arr[i] = arr[i - 1]
        i -= 1
    arr[i] = to_insert
    print(arr)
selectSort(arr)
insertSort(arr)
