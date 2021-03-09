import sys 
sys.stdin = open("./Algorithm_Study/0215/10250.txt", "r")
T = int(input())
for _ in range(T) :
  H, W ,N = list(map(int, input().split()))
  h = N//H+1
  w = N%H 
  if w == 0 : 
    w = H
    h -= 1
  if w >= 10 : 
    print("%02d%02d"%(w,h))
    continue
  print("%01d%02d"%(w,h))
  
    