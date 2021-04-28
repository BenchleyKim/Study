import sys
sys.stdin = open("./Algorithm_Study/BOJ0317/BOJ1806", "r")

N , S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
# print(arr)
left = 0 
right = 0

interSum = arr[0]
ans = N+2

while right <= N-1 and left <= right :
  if interSum >= S :
    interSum -= arr[left]
    left += 1 
    ans = min(ans, right-left+2)
  else :
    right += 1
    if right > N-1 :
      break
    interSum += arr[right]
if ans == N+2 :
  print(0)
else :
  print(ans)