import sys 
import time
sys.stdin = open("./Algorithm_Study/0215/lab04", "r")

N = int(input())
S = int(input())
K = int(input())
R = list(map(int, input().split()))
LeaderBoard = [0] * N
for i in range(N) :
  if i == 0 :
    LeaderBoard[i] = S
    continue
  else :
    prev = (123456789 * LeaderBoard[i-1]) % 1000000009
    score = (prev + 13579) % 1000000009
    LeaderBoard[i] = score

start = time.time()
LeaderBoard.sort(reverse = True)

for r in R :
  print(LeaderBoard[r-1])

print("Second Try : ", time.time()-start)
