import sys 
sys.stdin = open("./Algorithm_Study/BOJ0306/BOJ11053", "r")

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
DP = [0] * N
tmx = 0
for i in range(N) :
  mx = 0
  for j in range(i) :
    if  arr[i] > arr[j]  :
      mx = max(DP[j],mx)
  DP[i] = mx+1
  tmx = max(DP[i],tmx)
print(tmx)