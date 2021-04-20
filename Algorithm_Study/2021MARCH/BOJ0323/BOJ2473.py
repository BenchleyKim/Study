import sys
sys.stdin = open("./Algorithm_Study/BOJ0323/BOJ2473", "r")
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
arr.sort()
ans = [0,1,N-1]
for i in range(N-2) :
  left = i + 1
  right = N-1
  mn = abs(arr[ans[0]] + arr[ans[1]] + arr[ans[2]])
  while left < right : 
    current = abs(arr[i] + arr[left] + arr[right])
    if current < mn :
      mn = current
      ans = [i,left,right]
    if abs(arr[i] + arr[left+1] + arr[right]) < abs(arr[i] + arr[left] + arr[right-1]) :
      left += 1
    else :
      right -= 1
print(arr[ans[0]],arr[ans[1]],arr[ans[2]])
