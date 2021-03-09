import sys 
sys.stdin = open("./Algorithm_Study/BOJ/BOJ11726", "r")

N = int(input())
arr = [0] * (N+1)
if N == 1 :
  print(1)
  exit()
if N == 2 :
  print(2)
  exit()
arr[1] = 1
arr[2] = 2
for i in range(3,N+1) :
  arr[i] = arr[i-1] + arr[i-2]
print(arr[N]%10007)


