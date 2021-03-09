k = int(input())
coin = list(map(int, input().split()))
n = int(input())
INF = 10000000
d = [INF] * (n+1) 
coinZip = list(zip(sorted(coin[1:]),sorted(coin[:-1])))
print(coinZip)
for c, nc in coinZip :
  d[c] == 1
  d[nc] == 1
  d[]
  
for i in range(n) :
  if i > coin[0] :
    for c in coin:
      if d[i] > d[i-c] :
        d[i]= d[i-c]
    continue

  for c, nc in coinZip :
    if i == c : d[i] = 1 ; continue
    if i > c and i < nc : d[i] = d[i-1] + 1 ; continue
    if i == nc : d[i] == 1 ; continue
  
    


print(d[n])