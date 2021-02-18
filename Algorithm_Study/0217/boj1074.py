import sys
sys.stdin = open('./Algorithm_study/0217/boj1074','r')
N , r, c = map(int, input().split())
l = 2**N
count = 0
def search(n,row,col) :
  global count
  if n == 1 :
    if row > 1 :
      count += 2
    if col > 1 :
      count +=  1
    print(count)
  else : 
    n -= 1
    if row > 2**n :
      count += 2**(2*n+1)
      if col > 2**n :
        count += 2**(2*n) 
        search(n,row-(2**n),col-(2**n))
      else :
        search(n,row-(2**n),col)
    else :
      if col > 2**n :
        count += 2**(2*n) 
        search(n,row,col-(2**n))
      else :
        search(n,row,col)
search(N,r+1,c+1)
