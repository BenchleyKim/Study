from sys import stdin

# sys.stdin = open('./Algorithm_Study/0214/1003.txt', 'rt')

def fibo(n ) :
  if n == 0 : 
    global zerocount
    zerocount += 1
    return 0
  elif n == 1 :
    global onecount
    onecount += 1
    return 1
  else : 
    return fibo(n-1) + fibo(n-2)

n = int(stdin.readline())
for _ in range(n) :
  onecount = 0
  zerocount = 0
  fibo(int(stdin.readline()))
  print(zerocount, onecount)