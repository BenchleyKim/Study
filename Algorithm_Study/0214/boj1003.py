
def fibo(n) :
  r5 = 5 ** 0.5
  return int((((1+r5)**n)-((1-r5)**n))/((2**n)*r5))

n = int(input())
for _ in range(n) :
  onecount = 0
  zerocount = 0
  k = int(input())
  if k == 0 :
    print("1 0")
    continue
  print(fibo(k-1), fibo(k))
