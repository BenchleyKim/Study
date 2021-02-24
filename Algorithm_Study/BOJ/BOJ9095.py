import sys
sys.stdin = open("./Algorithm_Study/BOJ/BOJ9095", "r")

T = int(sys.stdin.readline())

def backtracking(n) :
  global count
  if n == 1 :
    count += 1
    return
  if n == 2 :
    count += 2
    return
  if n == 3 :
    count += 4
    return
  if n > 3 :
    backtracking(n-1)
    backtracking(n-2)
    backtracking(n-3)

for _ in range(T) :
  count = 0
  N = int(sys.stdin.readline())
  backtracking(N)
  print(count)
