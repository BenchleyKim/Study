import sys
sys.stdin = open('./Algorithm_study/0217/lab03','r')
MOD =1000000007
N,M= map(int,input().split())
def fibo(n) :
  return int(((1+5**(1/2))**n-(1-5**(1/2))**n)/((2**n)*(5**(1/2))))

fn , fm = fibo(N), fibo(M)
print(fn,fm)
def gcd(m,n):
    while n != 0:
       t = m%n
       (m,n) = (n,t)
    return abs(m)
print(gcd(fn,fm))
print(fibo(gcd(N,M)))