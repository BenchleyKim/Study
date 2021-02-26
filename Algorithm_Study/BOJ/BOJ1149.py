import sys 
sys.stdin = open("./Algorithm_Study/BOJ/BOJ1149", "r")
MIN = 1001
N = int(input())
arr = [[0,0,0]]

for i in range(1,N+1):
  arr.append(list(map(int, input().split())))

sum = 0
DP = [-1] *(N+1)
for i in range(1,N+1) :
  mn = MIN
  tmp = -1 
  for j in range(3) :
    flag_value = -1 
    if DP[i-1] == j :
      for k in range(3) :
        if DP[i-2] != k and DP[i-1] != k :
          if arr[i][j] - arr[i-1][j] + arr[i-1][k] < mn :
            tmp = j
            mn = arr[i][j] - arr[i-1][DP[i-1]] + arr[i-1][k]
            flag_value = k
            flag = True
          continue
      continue
    else : 
      if arr[i][j] < mn :
        tmp = j 
        mn = arr[i][j]
        flag = False
  if flag :
    DP[i-1] = flag_value
  sum += mn 
  DP[i] = tmp
print(sum)

