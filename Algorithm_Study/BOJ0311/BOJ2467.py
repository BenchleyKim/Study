
import sys

sys.stdin = open("./Algorithm_Study/BOJ0311/BOJ2467", "r")

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

left = 0 
right = len(arr)-1
result = [left, right]
mn = arr[left] + arr[right]
while left != right :
  tmp = arr[left] + arr[right]
  if abs(tmp) < abs(mn) :
    mn = tmp 
    result = [left, right]
  if tmp < 0 :
    left += 1
    continue
  elif tmp > 0 :
    right -= 1
  else :
    break
    

print(arr[result[0]],arr[result[1]])
