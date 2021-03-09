import sys 
sys.stdin = open("./Algorithm_Study/BOJ/BOJ1463", "r")
N = int(input())
DP = [0] * (N+1)
DP[1] = 0
for i in range(2,N+1) :
  candidate = DP[i-1]
  if i%3 == 0 :
    candidate = min(candidate,DP[i//3]) 
  if i%2 == 0 :
    candidate = min(candidate,DP[i//2]) 
  DP[i] = candidate +1
print(DP[N])
  


