import sys
sys.stdin = open(".\Algorithm_Study\BOJ0527\BOJ2217","r")
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N) : 
    K = int(input())
    arr.append(K)

arr.sort()
print(arr)
mx = 0 
for i in range(len(arr)) :
    mx = max(mx, arr[i] * (N-i))
print(mx)
