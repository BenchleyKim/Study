import sys 
sys.stdin = open("./Algorithm_Study/BOJ/BOJ1780", "r")

N = int(input())
P = [list(map(int, input().split())) for i in range(N)]
count = 0
countList = [0,0,0]
def DAC(x,y, n) :
  global countList
  if n == 1 :
    if P[x-1][y-1] == -1 :
      countList[0] += 1
      return
    if P[x-1][y-1] == 0 :
      countList[1] += 1
      return
    if P[x-1][y-1] == 1:
      countList[2] += 1
      return
  tmp = P[x-1][y-1]
  flag = 0 
  for i in range(x,x-n,-1) :
    for j in range(y,y-n,-1) :
      if P[i-1][j-1] != tmp :
        flag = 1
        break 
  if not flag :
    if tmp == -1 :
      countList[0] += 1
      return
    if tmp == 0 :
      countList[1] += 1
      return
    if tmp == 1:
      countList[2] += 1
      return
  
  n //= 3
  dx,dy = x//3 , y//3
  DAC(x,y,n)
  DAC(x,y-n,n)
  DAC(x,y-(2*n),n)
  DAC(x-n ,y,n)
  DAC( x-n,y-(2*n),n)
  DAC( x-n ,y-n,n)
  DAC( x-(2*n),y,n)
  DAC(x-(2*n),y-(2*n),n)
  DAC(x-(2*n),y-n,n)
  
DAC(N,N,N)

for c in countList :
  print(c)

