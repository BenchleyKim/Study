import sys
sys.stdin = open("./Algorithm_Study/BOJ0317/BOJ1806", "r")

N , S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
print(arr)
left = 0 
right = 1

interSum = arr[0]
ans = N

while right < N-1 and left <= right :
  print(left, right , interSum)
  if interSum >= S :
    interSum -= arr[left]
    left += 1 
    ans = min(ans, right-left)
  else :
    right += 1
    interSum += arr[right]

print(ans)