import sys 
sys.stdin = open("./Algorithm_Study/0215/2275", "r")
T = int(input())
for _ in range(T) :
  k = int(input())
  n = int(input())
  l = []
  for x in range(1,((k+1)*n)+1) :
    if x / (k+1) <= 1 :
      l.append(1)
    elif x % (k+1) == 1 :
      l.append((x//(k+1))+1)
    else : 
      l.append(l[x-k-2]+l[-1])
  print(l[-1])




