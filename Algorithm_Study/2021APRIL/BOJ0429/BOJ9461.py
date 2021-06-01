import sys 
sys.stdin = open("./Algorithm_Study/BOJ0429/BOJ9461","r")
input = sys.stdin.readline

# 1 1 1 1+1 , 1+1, 1+2, 1+3, 1+4, 2+5, 2+7, 3+9 , 4+ 12, 5+ 16

T = int(input())
arr = [1,1,1,2,2]
for t in range(T) :
    N = int(input())
    if N <= len(arr) :
        print(arr[N-1])
        continue
    t = len(arr)
    while len(arr) <= N :
        arr.append(arr[t-5] + arr[t-1])
        t += 1
    print(arr[N-1])
        

