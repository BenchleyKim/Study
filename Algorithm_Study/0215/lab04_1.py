import sys 
sys.stdin = open("./Algorithm_Study/0215/lab04", "r")

import time
N = int(input())
S = int(input())
K = int(input())
R = list(map(int, input().split()))
arr = [0] * N
for i in range(N) :
  if i == 0 :
    arr[i] = S
    continue
  else :
    prev = (123456789 * arr[i-1]) % 1000000009
    score = (prev + 13579) % 1000000009
    arr[i] = score

def find(low, high,idx):
    if high <= low:
        # print(high)
        return
    mid = partition(low, high)
    if mid == idx : 
        return 
    elif mid <= idx : 
        find(mid, high,idx)
    else :
        find(low, mid - 1,idx)
def partition(low, high):
    pivot = arr[(low + high) // 2]
    while low <= high:
        while arr[low] > pivot:
            low += 1
        while arr[high] < pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low + 1, high - 1
    return low


start = time.time()

for r in R :
    find(0,N-1, r-1)
    print(arr[r-1])

print("First Try : ",time.time()-start)

start = time.time()
arr.sort(reverse = True)
for r in R :
    print(arr[r-1])
print("Second Try : ", time.time()-start)
