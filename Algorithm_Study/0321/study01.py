
import sys 
sys.stdin = open("./Algorithm_Study/0321/study01", "r")
input = sys.stdin.readline

arr = list(map(int, input().split()))ß
for i in range(len(arr)) :
    mn_idx = i
    for j in range(i, len(arr)) :
        if arr[mn_idx] > arr[j] :
            mn_idx = j 
    arr[i], arr[mn_idx] = arr[mn_idx], arr[i]
print(arr)
