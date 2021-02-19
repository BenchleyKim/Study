import sys 
sys.stdin = open("./Algorithm_Study/0219/lab02", "r")
MOD = 10**18
S, K = map(int, input().split())
arr = [S//K] * K
if S % K :
  for i in range(S%K) :
    arr[i] += 1
result = 1
for a in arr :
  result *= a
  result %= MOD
print(result)

  

