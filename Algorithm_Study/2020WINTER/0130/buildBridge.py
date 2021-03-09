
t = int(input())
results = []
for i in range(t) :
  n , m = map(int, input().split())
  mfac = 1
  for i in range(1,m+1) :
    mfac *= i
  nmfac = 1
  for i in range(1,m-n+1):
    nmfac *= i
  nfac = 1 
  for i in range(1,n+1):
    nfac *= i
  result = mfac / (nmfac * nfac)
  results.append(int(result))

for i in results:
  print(i)
