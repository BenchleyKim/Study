import sys
import math
sys.stdin = open("./Algorithm_Study/BOJ0323/BOJ1016", "r")
input = sys.stdin.readline

mn , mx = map(int, input().split())
arr = [0] * (mx-mn+1)
primeList = []
for i in range(2,int(mx**(1/2))+1) :
  start = math.ceil(mn/(i**2)) 
  start *= i**2
  for j in range(start,mx+1, i**2) :
    arr[j-mn] = 1
cnt = 0
for i in range(mx-mn+1) :
  if arr[i] == 0 :
    cnt += 1
print(cnt)
# for i in range(2,int(mn**(1/2))+1) :
#   start = mn // (i**2)
#   start = (i**2) * mn
#   for j in range(start,mx+1,i**2) :
#     arr[j] = 1 
