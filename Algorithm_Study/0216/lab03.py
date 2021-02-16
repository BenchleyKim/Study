import sys 
sys.stdin = open("./Algorithm_Study/0216/lab03", "r")

N = int(input())
arr = list(map(int, input().split()))
count = 0

# def bubbleSort(v, n ) : 
#   global count
#   for i in range(1, n) : 
#     dirty = False
#     for j in range(0, n-i) : 
#       if v[j] > v[j+1] : 
#         v[i], v[j+1] = v[j+1], v[j]
#         count += 1
#         dirty = True
#     if not dirty  : break

# bubbleSort(arr, N)
# print(count)
# print(arr)

def perform_bubble_sort(v , n):
    swapcount = 0
    for j in range(n):
        for i in range(1, n-j):
            if v[i-1] > v[i]:
                swapcount += 1
                v[i-1], v[i] = v[i], v[i-1]
                # print(v[i-1],v[i])
                # print(arr)
    return  swapcount
count = 0
def merge_sort(v):
    global count 
    count += 1
    if len(v) <= 1:
        return v
    mid = len(v) // 2
    leftv = v[:mid]
    rightv = v[mid:]
    leftv = merge_sort(leftv)
    rightv = merge_sort(rightv)
    return merge(leftv, rightv)
def merge(left, right):
    
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

print(arr)
# print(perform_bubble_sort(arr, N))
print(merge_sort(arr))
print(count)
print(arr)
