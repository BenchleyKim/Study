import sys
sys.stdin = open(".\Algorithm_Study\BOJ0611\BOJ20300","r")
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
mx = 0
if len(arr) % 2 :
    mx = arr.pop()
if len(arr) < 2 :
    mx = arr[0]
else :
    for i in range(len(arr)//2) :
        mx = max(mx, arr[i] + arr[-(i+1)])
print(mx)
