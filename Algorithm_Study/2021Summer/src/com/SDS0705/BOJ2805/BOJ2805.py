import sys
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/SDS0705/BOJ2805/BOJ2805.in","r")
input = sys.stdin.readline

N, M = map(int , input().split())
arr = list(map(int, input().split()))

left , right = min(arr) , max(arr)
def check(value) :
    result = 0 
    for a in arr :
        if a > value :
            result += a - value
    return result
while left < right :
    mid = (left + right)//2 
    logs = check(mid) 
    if logs == M :
        print(mid)
        break
    if logs < M :
        left, right = left, mid - 1
    else :
        left , right = mid -1  , right
    if left > right :
        print(mid)
        break
    
