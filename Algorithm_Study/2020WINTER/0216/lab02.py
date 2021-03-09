import sys 
sys.stdin = open("./Algorithm_Study/0216/lab02", "r")
N = int(input())

def isDe(n) :
  S = str(n)
  c = 10
  for i in range(len(S)) :
    if int(S[i]) >= c : 
      return False
    c = int(S[i])
  return True
n = 0
k = 1
while k <= N :
  n += 1
  if n // 1000000000 : break
  if isDe(n) :
    print(k," ",n)
    k += 1
print(n)

