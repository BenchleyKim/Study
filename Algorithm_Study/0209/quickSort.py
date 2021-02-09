# N = int(input())
# arr = []
# for _ in range(N) :
#     arr.append(int(input))
arr = [3,4,5,8,7,2,1]

def quickSort(a, b ):
    if a>=b : return
    p = a
    i,j = a+1,b
    while i < j : 
        print(a,b, i,j, p)
        if arr[i] <= arr[p] : 
            i += 1
        else :
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1 
        print(arr)
    arr[p] , arr[j] = arr[j], arr[p]
    p , j = j, p
    quickSort(a,p)
    quickSort(p+1,b)
quickSort(0,len(arr)-1)
print(arr)
    